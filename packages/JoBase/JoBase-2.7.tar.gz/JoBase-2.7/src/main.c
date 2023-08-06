#define OBJ(e) return format(PyExc_TypeError,"must be Base or cursor, not %s",Py_TYPE(e)->tp_name),NULL;
#include <main.h>

Window *window;
Cursor *cursor;
Camera *camera;
Key *key;

FT_Library library;
PyObject *loop;
Texture *textures;
Font *fonts;

char *path;
size_t length;
bool ready;
GLuint program;
GLuint mesh;
GLint uniform[7];

static bool circleCircle(vec2 p1, double r1, vec2 p2, double r2) {
    return hypot(p2[x] - p1[x], p2[y] - p1[y]) < r1 + r2;
}

static bool circlePoint(vec2 pos, double radius, vec2 point) {
    return hypot(point[x] - pos[x], point[y] - pos[y]) < radius;
}

static bool segmentPoint(vec2 p1, vec2 p2, vec2 point) {
    const double d1 = hypot(point[x] - p1[x], point[y] - p1[y]);
    const double d2 = hypot(point[x] - p2[x], point[y] - p2[y]);
    const double length = hypot(p1[x] - p2[x], p1[y] - p2[y]);

    return d1 + d2 >= length - 0.1 && d1 + d2 <= length + 0.1;
}

static bool segmentSegment(vec2 p1, vec2 p2, vec2 p3, vec2 p4) {
    const double value = (p4[y] - p3[y]) * (p2[x] - p1[x]) - (p4[x] - p3[x]) * (p2[y] - p1[y]);
    const double u1 = ((p4[x] - p3[x]) * (p1[y] - p3[y]) - (p4[y] - p3[y]) * (p1[x] - p3[x])) / value;
    const double u2 = ((p2[x] - p1[x]) * (p1[y] - p3[y]) - (p2[y] - p1[y]) * (p1[x] - p3[x])) / value;

    return u1 >= 0 && u1 <= 1 && u2 >= 0 && u2 <= 1;
}

static bool segmentCircle(vec2 p1, vec2 p2, vec2 pos, double radius) {
    if (circlePoint(pos, radius, p1) || circlePoint(pos, radius, p2))
        return true;

    const double length = hypot(p1[x] - p2[x], p1[y] - p2[y]);
    const double dot = ((pos[x] - p1[x]) * (p2[x] - p1[x]) + (pos[y] - p1[y]) * (p2[y] - p1[y])) / pow(length, 2);

    vec2 point = {p1[x] + dot * (p2[x] - p1[x]), p1[y] + dot * (p2[y] - p1[y])};
    return segmentPoint(p1, p2, point) ? hypot(point[x] - pos[x], point[y] - pos[y]) <= radius : 0;
}

static bool polySegment(poly poly, size_t size, vec2 p1, vec2 p2) {
    FOR(size_t, size) if (segmentSegment(p1, p2, poly[i], poly[i + 1 == size ? 0 : i + 1]))
        return true;

    return false;
}

static bool polyPoint(poly poly, size_t size, vec2 point) {
    bool hit = false;

    FOR(size_t, size) {
        vec a = poly[i];
        vec b = poly[i + 1 == size ? 0 : i + 1];

        if ((point[x] < (b[x] - a[x]) * (point[y] - a[y]) / (b[y] - a[y]) + a[x]) &&
            ((a[y] > point[y] && b[y] < point[y]) ||
            (a[y] < point[y] && b[y] > point[y]))) hit = !hit;
    }

    return hit;
}

static bool polyPoly(poly p1, size_t s1, poly p2, size_t s2) {
    if (polyPoint(p1, s1, p2[0]) || polyPoint(p2, s2, p1[0]))
        return true;

    FOR(size_t, s1) if (polySegment(p2, s2, p1[i], p1[i + 1 == s1 ? 0 : i + 1]))
        return true;

    return false;
}

static bool polyCircle(poly poly, size_t size, vec2 pos, double radius) {
    FOR(size_t, size) if (segmentCircle(poly[i], poly[i + 1 == size ? 0 : i + 1], pos, radius))
        return true;
    
    return false;
}

static bool linePoint(poly line, size_t size, double radius, vec2 point) {
    FOR(size_t, size - 1) if (segmentCircle(line[i], line[i + 1], point, radius))
        return true;

    return false;
}

static bool linePoly(poly line, size_t s1, double radius, poly poly, size_t s2) {
    if (polyPoint(poly, s1, line[0]))
        return true;

    for (size_t j = 1; j < s1; j ++)
        FOR(size_t, s2) {
            const bool a = segmentCircle(line[j], line[j - 1], poly[i], radius);
            const bool b = segmentCircle(poly[i], poly[i + 1 == s2 ? 0 : i + 1], line[j], radius);
            if (a || b) return true;
        }

    return false;
}

void buffers(GLuint *vao, GLuint *vbo, GLuint *ibo) {
    glGenVertexArrays(1, vao);
    glBindVertexArray(*vao);
    glGenBuffers(1, vbo);
    glBindBuffer(GL_ARRAY_BUFFER, *vbo);
    glGenBuffers(1, ibo);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, *ibo);

    glVertexAttribPointer(uniform[vert], 2, GL_FLOAT, GL_FALSE, 0, 0);
    glEnableVertexAttribArray(uniform[vert]);
    glBindVertexArray(0);
}

void rotate(poly poly, size_t size, double angle, vec2 pos) {
    const double cosine = cos(angle);
    const double sine = sin(angle);

    FOR(size_t, size) {
        const double px = poly[i][x];
        const double py = poly[i][y];

        poly[i][x] = px * cosine - py * sine + pos[x];
        poly[i][y] = px * sine + py * cosine + pos[y];
    }
}

void parameters() {
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
}

void format(PyObject *error, const char *format, ...) {
    va_list args;
    va_start(args, format);

    int size = vsnprintf(NULL, 0, format, args);
    char *buffer = malloc(size + 1);
    va_end(args);

    va_start(args, format);
    vsprintf(buffer, format, args);
    PyErr_SetString(error, buffer);

    va_end(args);
    free(buffer);
}

void start() {
    ready = false;
    glfwPollEvents();
}

void end() {
    glfwWaitEventsTimeout(.1);
    ready = true;
}

const char *filepath(const char *file) {
    return path[length] = 0, strcat(path, file);
}

int update() {
    const vec size = windowSize();

    mat matrix = {
        (GLfloat) 2 / size[x], 0, 0, 0, 0,
        (GLfloat) 2 / size[y], 0, 0, 0, 0, -2, 0,
        (GLfloat) -camera -> pos[x] * 2 / size[x],
        (GLfloat) -camera -> pos[y] * 2 / size[y], -1, 1
    };
    
    glUniformMatrix4fv(uniform[view], 1, GL_FALSE, matrix);
    glClear(GL_COLOR_BUFFER_BIT);

    if (loop && !PyObject_CallObject(loop, NULL)) {
        Py_DECREF(loop);
        return -1;
    }

    window -> resize = false;
    cursor -> move = false;
    cursor -> enter = false;
    cursor -> leave = false;
    cursor -> press = false;
    cursor -> release = false;
    key -> press = false;
    key -> release = false;
    key -> repeat = false;

    FOR(uint16_t, GLFW_KEY_LAST) {
        key -> keys[i].press = false;
        key -> keys[i].release = false;
        key -> keys[i].repeat = false;
    }

    FOR(uint8_t, GLFW_MOUSE_BUTTON_LAST) {
        cursor -> buttons[i].press = false;
        cursor -> buttons[i].release = false;
    }

    return glfwSwapBuffers(window -> glfw), 0;
}

PyObject *collide(PyObject *self, PyObject *other) {
    bool result;

    if (BASE(self, RectangleType)) {
        vec2 rect[4];
        rectanglePoly((Rectangle *) self, rect);

        if (BASE(other, RectangleType)) {
            vec2 poly[4];

            rectanglePoly((Rectangle *) other, poly);
            result = polyPoly(rect, 4, poly, 4);
        }

        else if (BASE(other, CircleType)) {
            Circle *circle = (Circle *) other;
            vec2 pos = {circleX(circle), circleY(circle)};
            result = polyCircle(rect, 4, pos, circle -> radius);
        }

        else if (BASE(other, ShapeType)) {
            Shape *shape = (Shape *) other;
            vec2 *poly = shapePoly(shape);

            result = polyPoly(rect, 4, poly, shape -> vertex);
            free(poly);
        }

        else if (BASE(other, LineType)) {
            Line *line = (Line *) other;
            vec2 *poly = shapePoly((Shape *) line);

            result = linePoly(poly, line -> shape.vertex, line -> width / 2, rect, 4);
            free(poly);
        }

        else if (other == (PyObject *) cursor)
            result = polyPoint(rect, 4, cursorPos());

        else OBJ(other)
    }

    else if (BASE(self, CircleType)) {
        Circle *circle = (Circle *) self;
        vec2 pos = {circleX(circle), circleY(circle)};
        const double size = circle -> radius;

        if (BASE(other, RectangleType)) {
            vec2 rect[4];

            rectanglePoly((Rectangle *) other, rect);
            result = polyCircle(rect, 4, pos, size);
        }

        else if (BASE(other, CircleType)) {
            Circle *object = (Circle *) other;
            vec2 point = {circleX(object), circleY(object)};
            result = circleCircle(pos, size, point, object -> radius);
        }

        else if (BASE(other, ShapeType)) {
            Shape *shape = (Shape *) other;
            vec2 *poly = shapePoly(shape);

            result = polyCircle(poly, shape -> vertex, pos, size);
            free(poly);
        }

        else if (BASE(other, LineType)) {
            Line *line = (Line *) other;
            vec2 *poly = shapePoly((Shape *) line);

            result = linePoint(poly, line -> shape.vertex, line -> width / 2 + size, pos);
            free(poly);
        }

        else if (other == (PyObject *) cursor)
            result = circlePoint(pos, size, cursorPos());

        else OBJ(other)
    }

    else if (BASE(self, ShapeType)) {
        Shape *shape = (Shape *) self;
        vec2 *poly = shapePoly(shape);

        if (BASE(other, RectangleType)) {
            vec2 rect[4];

            rectanglePoly((Rectangle *) other, rect);
            result = polyPoly(poly, shape -> vertex, rect, 4);
        }

        else if (BASE(other, CircleType)) {
            Circle *circle = (Circle *) other;
            vec2 pos = {circleX(circle), circleY(circle)};
            result = polyCircle(poly, shape -> vertex, pos, circle -> radius);
        }

        else if (BASE(other, ShapeType)) {
            Shape *object = (Shape *) other;
            vec2 *mesh = shapePoly(object);

            result = polyPoly(poly, shape -> vertex, mesh, object -> vertex);
            free(mesh);
        }

        else if (BASE(other, LineType)) {
            Line *line = (Line *) other;
            vec2 *mesh = shapePoly((Shape *) line);

            result = linePoly(mesh, line -> shape.vertex, line -> width / 2, poly, shape -> vertex);
            free(poly);
        }

        else if (other == (PyObject *) cursor)
            result = polyPoint(poly, shape -> vertex, cursorPos());

        else {
            free(poly);
            OBJ(other)
        }

        free(poly);
    }

    else if (BASE(self, LineType)) {
        Line *line = (Line *) self;
        vec2 *poly = shapePoly((Shape *) line);

        if (BASE(other, RectangleType)) {
            vec2 rect[4];

            rectanglePoly((Rectangle *) other, rect);
            result = linePoly(poly, line -> shape.vertex, line -> width / 2, rect, 4);
        }

        else if (BASE(other, CircleType)) {
            Circle *circle = (Circle *) other;
            vec2 pos = {circleX(circle), circleY(circle)};
            result = linePoint(poly, line -> shape.vertex, line -> width / 2 + circle -> radius, pos);
        }

        else if (BASE(other, ShapeType)) {
            Shape *object = (Shape *) other;
            vec2 *mesh = shapePoly(object);

            result = linePoly(poly, line -> shape.vertex, line -> width / 2, mesh, object -> vertex);
            free(mesh);
        }

        else if (other == (PyObject *) cursor)
            result = linePoint(poly, line -> shape.vertex, line -> width / 2, cursorPos());

        else {
            free(poly);
            OBJ(other)
        }

        free(poly);
    }

    else if (self == (PyObject *) cursor) {
        if (BASE(other, RectangleType)) {
            vec2 rect[4];

            rectanglePoly((Rectangle *) other, rect);
            result = polyPoint(rect, 4, cursorPos());
        }

        else if (BASE(other, CircleType)) {
            Circle *circle = (Circle *) other;
            vec2 pos = {circleX(circle), circleY(circle)};
            result = circlePoint(pos, circle -> radius, cursorPos());
        }

        else if (BASE(other, ShapeType)) {
            Shape *shape = (Shape *) other;
            vec2 *poly = shapePoly(shape);

            result = polyPoint(poly, shape -> vertex, cursorPos());
            free(poly);
        }

        else if (BASE(self, LineType)) {
            Line *line = (Line *) other;
            vec2 *poly = shapePoly((Shape *) line);

            result = linePoint(poly, line -> shape.vertex, line -> width / 2, cursorPos());
            free(poly);
        }

        else if (other == (PyObject *) cursor)
            Py_RETURN_TRUE;

        else OBJ(other)
    }

    else OBJ(self)
    return PyBool_FromLong(result);
}

double getLeft(poly poly, size_t size) {
    double left = poly[0][x];

    for (size_t i = 1; i < size; i ++)
        if (poly[i][x] < left) left = poly[i][x];

    return left;
}

double getTop(poly poly, size_t size) {
    double top = poly[0][y];

    for (size_t i = 1; i < size; i ++)
        if (poly[i][y] > top) top = poly[i][y];

    return top;
}

double getRight(poly poly, size_t size) {
    double right = poly[0][x];

    for (size_t i = 1; i < size; i ++)
        if (poly[i][x] > right) right = poly[i][x];

    return right;
}

double getBottom(poly poly, size_t size) {
    double bottom = poly[0][y];

    for (size_t i = 1; i < size; i ++)
        if (poly[i][y] < bottom) bottom = poly[i][y];

    return bottom;
}
