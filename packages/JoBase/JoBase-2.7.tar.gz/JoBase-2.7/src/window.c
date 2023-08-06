#include <main.h>

static void clear() {
    glClearColor(
        (GLfloat) window -> color[r],
        (GLfloat) window -> color[g],
        (GLfloat) window -> color[b], 1);
}

static void windowRefreshCallback(GLFWwindow *Py_UNUSED(window)) {
    if (ready && !PyErr_Occurred()) update();
}

static void windowSizeCallback(GLFWwindow *Py_UNUSED(window), int Py_UNUSED(width), int Py_UNUSED(height)) {
    window -> resize = true;
}

static void framebufferSizeCallback(GLFWwindow *Py_UNUSED(window), int width, int height) {
    glViewport(0, 0, width, height);
}

static void cursorPosCallback(GLFWwindow *Py_UNUSED(window), double Py_UNUSED(x), double Py_UNUSED(y)) {
    cursor -> move = true;
}

static void cursorEnterCallback(GLFWwindow *Py_UNUSED(window), int entered) {
    entered ? (cursor -> enter = true) : (cursor -> leave = true);
}

static void mouseButtonCallback(GLFWwindow *Py_UNUSED(window), int button, int action, int Py_UNUSED(mods)) {
    if (action == GLFW_PRESS) {
        cursor -> press = true;
        cursor -> buttons[button].press = true;
        cursor -> buttons[button].hold = true;
    }

    else if (action == GLFW_RELEASE) {
        cursor -> release = true;
        cursor -> buttons[button].release = true;
        cursor -> buttons[button].hold = false;
    }
}

static void keyCallback(GLFWwindow *Py_UNUSED(window), int type, int Py_UNUSED(scancode), int action, int Py_UNUSED(mods)) {
    if (action == GLFW_PRESS) {
        key -> press = true;
        key -> keys[type].press = true;
        key -> keys[type].hold = true;
    }

    else if (action == GLFW_RELEASE) {
        key -> release = true;
        key -> keys[type].release = true;
        key -> keys[type].hold = false;
    }

    else if (action == GLFW_REPEAT) {
        key -> repeat = true;
        key -> keys[type].repeat = true;
    }
}

static PyObject *Window_getCaption(Window *self, void *Py_UNUSED(closure)) {
    return PyUnicode_FromString(self -> caption);
}

static int Window_setCaption(Window *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const char *caption = PyUnicode_AsUTF8(value);
    if (!caption) return -1;

    free(self -> caption);
    self -> caption = strdup(caption);

    return glfwSetWindowTitle(self -> glfw, self -> caption), 0;
}

static PyObject *Window_getRed(Window *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[r]);
}

static int Window_setRed(Window *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[r] = PyFloat_AsDouble(value);
    return ERR(self -> color[r]) ? -1 : clear(), 0;
}

static PyObject *Window_getGreen(Window *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[g]);
}

static int Window_setGreen(Window *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[g] = PyFloat_AsDouble(value);
    return ERR(self -> color[g]) ? -1 : clear(), 0;
}

static PyObject *Window_getBlue(Window *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[b]);
}

static int Window_setBlue(Window *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[b] = PyFloat_AsDouble(value);
    return ERR(self -> color[b]) ? -1 : clear(), 0;
}

static double Window_vecColor(Window *self, uint8_t index) {
    return self -> color[index];
}

static PyObject *Window_getColor(Window *self, void *Py_UNUSED(closure)) {
    Vector *color = vectorNew((PyObject *) self, (Getter) Window_vecColor, 3);

    color -> data[r].set = (setter) Window_setRed;
    color -> data[g].set = (setter) Window_setGreen;
    color -> data[b].set = (setter) Window_setBlue;
    color -> data[r].name = "r";
    color -> data[g].name = "g";
    color -> data[b].name = "b";

    return (PyObject *) color;
}

static int Window_setColor(Window *self, PyObject *value, void *Py_UNUSED(closure)) {
    return vectorSet(value, self -> color, 3) ? -1 : clear(), 0;
}

static PyObject *Window_getWidth(Window *Py_UNUSED(self), void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(windowSize()[x]);
}

static int Window_setWidth(Window *Py_UNUSED(self), PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const int width = (int) PyFloat_AsDouble(value);
    if (ERR(width)) return -1;

    start();
    glfwSetWindowSize(window -> glfw, width, (int) windowSize()[y]);
    return end(), 0;
}

static PyObject *Window_getHeight(Window *Py_UNUSED(self), void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(windowSize()[y]);
}

static int Window_setHeight(Window *Py_UNUSED(self), PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const int height = (int) PyFloat_AsDouble(value);
    if (ERR(height)) return -1;

    start();
    glfwSetWindowSize(window -> glfw, (int) windowSize()[x], height);
    return end(), 0;
}

static double Window_vecSize(Window *Py_UNUSED(self), uint8_t index) {
    return windowSize()[index];
}

static PyObject *Window_getSize(Window *self, void *Py_UNUSED(closure)) {
    Vector *size = vectorNew((PyObject *) self, (Getter) Window_vecSize, 2);

    size -> data[x].name = "x";
    size -> data[y].name = "y";

    return (PyObject *) size;
}

static int Window_setSize(Window *Py_UNUSED(self), PyObject *value, void *Py_UNUSED(closure)) {
    const vec size = windowSize();

    if (vectorSet(value, size, 2))
        return -1;

    start();
    glfwSetWindowSize(window -> glfw, (int) size[x], (int) size[y]);
    return end(), 0;
}

static PyObject *Window_getResize(Window *self, void *Py_UNUSED(closure)) {
    return PyBool_FromLong(self -> resize);
}

static PyObject *Window_close(Window *self, PyObject *Py_UNUSED(ignored)) {
    glfwSetWindowShouldClose(self -> glfw, GLFW_TRUE);
    Py_RETURN_NONE;
}

static PyObject *Window_maximize(Window *self, PyObject *Py_UNUSED(ignored)) {
    glfwMaximizeWindow(self -> glfw);
    Py_RETURN_NONE;
}

static PyObject *Window_minimize(Window *self, PyObject *Py_UNUSED(ignored)) {
    glfwIconifyWindow(self -> glfw);
    Py_RETURN_NONE;
}

static PyObject *Window_restore(Window *self, PyObject *Py_UNUSED(ignored)) {
    glfwRestoreWindow(self -> glfw);
    Py_RETURN_NONE;
}

static PyObject *Window_focus(Window *self, PyObject *Py_UNUSED(ignored)) {
    glfwFocusWindow(self -> glfw);
    Py_RETURN_NONE;
}

static PyObject *Window_new(PyTypeObject *type, PyObject *Py_UNUSED(args), PyObject *Py_UNUSED(kwds)) {
    window = (Window *) type -> tp_alloc(type, 0);

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
    glfwWindowHint(GLFW_SAMPLES, 4);

    if (!(window -> glfw = glfwCreateWindow(640, 480, "JoBase", NULL, NULL))) {
        PyErr_SetString(PyExc_OSError, "failed to create window");
        return glfwTerminate(), NULL;
    }

    glfwMakeContextCurrent(window -> glfw);
    glfwSetWindowRefreshCallback(window -> glfw, windowRefreshCallback);
    glfwSetWindowSizeCallback(window -> glfw, windowSizeCallback);
    glfwSetFramebufferSizeCallback(window -> glfw, framebufferSizeCallback);
    glfwSetCursorPosCallback(window -> glfw, cursorPosCallback);
    glfwSetCursorEnterCallback(window -> glfw, cursorEnterCallback);
    glfwSetMouseButtonCallback(window -> glfw, mouseButtonCallback);
    glfwSetKeyCallback(window -> glfw, keyCallback);
    glfwSwapInterval(1);

#ifndef __EMSCRIPTEN__
    if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress)) {
        PyErr_SetString(PyExc_OSError, "failed to load OpenGL");
        return glfwTerminate(), NULL;
    }
#endif

    Py_XINCREF(window);
    return (PyObject *) window;
}

static int Window_init(Window *self, PyObject *args, PyObject *kwds) {
    static char *kwlist[] = {"caption", "width", "height", "color", NULL};
    const char *caption = "JoBase";

    int width = 640, height = 480;
    PyObject *color = NULL;

    self -> color[r] = 1;
    self -> color[g] = 1;
    self -> color[b] = 1;
    self -> resize = true;

    if (!PyArg_ParseTupleAndKeywords(
        args, kwds, "|siiO", kwlist, &caption,  &width, &height, &color) ||
        (color && vectorSet(color, self -> color, 3))) return -1;

    self -> caption = strdup(caption);
    glfwSetWindowTitle(self -> glfw, self -> caption);
    glfwSetWindowSize(self -> glfw, width, height);

    return clear(), 0;
}

static void Window_dealloc(Window *self) {
    free(self -> caption);
    Py_TYPE(self) -> tp_free((PyObject *) self);
}

static PyGetSetDef WindowGetSetters[] = {
    {"caption", (getter) Window_getCaption, (setter) Window_setCaption, "name of the window", NULL},
    {"red", (getter) Window_getRed, (setter) Window_setRed, "red color of the window", NULL},
    {"green", (getter) Window_getGreen, (setter) Window_setGreen, "green color of the window", NULL},
    {"blue", (getter) Window_getBlue, (setter) Window_setBlue, "blue color of the window", NULL},
    {"color", (getter) Window_getColor, (setter) Window_setColor, "color of the window", NULL},
    {"width", (getter) Window_getWidth, (setter) Window_setWidth, "width of the window", NULL},
    {"height", (getter) Window_getHeight, (setter) Window_setHeight, "height of the window", NULL},
    {"size", (getter) Window_getSize, (setter) Window_setSize, "dimensions of the window", NULL},
    {"resize", (getter) Window_getResize, NULL, "the window is resized", NULL},
    {NULL}
};

static PyMethodDef WindowMethods[] = {
    {"close", (PyCFunction) Window_close, METH_NOARGS, "close the window"},
    {"maximize", (PyCFunction) Window_maximize, METH_NOARGS, "maximize the window"},
    {"minimize", (PyCFunction) Window_minimize, METH_NOARGS, "minimize the window"},
    {"restore", (PyCFunction) Window_restore, METH_NOARGS, "restore the window from maximized or minimized"},
    {"focus", (PyCFunction) Window_focus, METH_NOARGS, "bring the window to the front"},
    {NULL}
};

vec windowSize() {
    static vec2 size;
    int width, height;

    glfwGetWindowSize(window -> glfw, &width, &height);
    size[x] = width;
    size[y] = height;

    return size;
}

PyTypeObject WindowType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "Window",
    .tp_doc = "the main window",
    .tp_basicsize = sizeof(Window),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = Window_new,
    .tp_init = (initproc) Window_init,
    .tp_dealloc = (destructor) Window_dealloc,
    .tp_getset = WindowGetSetters,
    .tp_methods = WindowMethods
};