#include <main.h>

static void arbiter(cpBody *body, cpArbiter *arbiter, bool *data) {
    const cpVect normal = cpArbiterGetContactPointSet(arbiter).normal;
    const cpVect gravity = cpvnormalize(cpSpaceGetGravity(cpBodyGetSpace(body)));

    if (fabs(normal.x - gravity.x) < M_PI / 4 && fabs(normal.y - gravity.y) < M_PI / 4)
        *data = true;
}

static int vect(Base *self, PyObject *args, double *a, double *b, double *c, double *d) {
    *c = *d = 0;

    if (!self -> length) {
        PyErr_SetString(PyExc_AttributeError, "must be added to a physics engine");
        return -1;
    }

    return PyArg_ParseTuple(args, "dd|dd", a, b, c, d) ? 0 : -1;
}

static void pos(Base *self) {
    cpBodySetPosition(self -> body, cpv(self -> pos[x], self -> pos[y]));
}

static int other(PyObject *other, vec2 pos) {
    if (Py_TYPE(other) == &CursorType) {
        vec value = cursorPos();

        pos[0] = value[x];
        pos[1] = value[y];
    }

    else if (PyObject_IsInstance(other, (PyObject *) &BaseType)) {
        pos[0] = ((Base *) other) -> pos[x];
        pos[1] = ((Base *) other) -> pos[y];
    }

    else if (PySequence_Check(other)) {
        PyObject *seq = PySequence_Fast(other, NULL);

        if (PySequence_Fast_GET_SIZE(seq) < 2) {
            PyErr_SetString(PyExc_ValueError, "sequence must contain 2 values");
            Py_DECREF(seq);
            return -1;
        }

        FOR(uint8_t, 2) {
            pos[i] = PyFloat_AsDouble(PySequence_Fast_GET_ITEM(seq, i));

            if (ERR(pos[i])) {
                Py_DECREF(seq);
                return -1;
            }
        }

        Py_DECREF(seq);
    }

    else {
        format(PyExc_TypeError, "must be Base, cursor or sequence not %s", Py_TYPE(other) -> tp_name);
        return -1;
    }

    return 0;
}

static PyObject *Base_getX(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> pos[x]);
}

static int Base_setX(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> pos[x] = PyFloat_AsDouble(value);
    return ERR(self -> pos[x]) ? -1 : pos(self), 0;
}

static PyObject *Base_getY(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> pos[y]);
}

static int Base_setY(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> pos[y] = PyFloat_AsDouble(value);
    return ERR(self -> pos[y]) ? -1 : pos(self), 0;
}

static double Base_vecPos(Base *self, uint8_t index) {
    return self -> pos[index];
}

static PyObject *Base_getPos(Base *self, void *Py_UNUSED(closure)) {
    Vector *pos = vectorNew((PyObject *) self, (Getter) Base_vecPos, 2);

    pos -> data[x].set = (setter) Base_setX;
    pos -> data[y].set = (setter) Base_setY;
    pos -> data[x].name = "x";
    pos -> data[y].name = "y";

    return (PyObject *) pos;
}

static int Base_setPos(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    return vectorSet(value, self -> pos, 2) ? -1 : pos(self), 0;
}

static int Base_setScaleX(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> scale[x] = PyFloat_AsDouble(value);
    return ERR(self -> scale[x]) ? -1 : 0;
}

static int Base_setScaleY(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> scale[y] = PyFloat_AsDouble(value);
    return ERR(self -> scale[y]) ? -1 : 0;
}

static double Base_vecScale(Base *self, uint8_t index) {
    return self -> scale[index];
}

static PyObject *Base_getScale(Base *self, void *Py_UNUSED(closure)) {
    Vector *scale = vectorNew((PyObject *) self, (Getter) Base_vecScale, 2);

    scale -> data[x].set = (setter) Base_setScaleX;
    scale -> data[y].set = (setter) Base_setScaleY;
    scale -> data[x].name = "x";
    scale -> data[y].name = "y";

    return (PyObject *) scale;
}

static int Base_setScale(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    return vectorSet(value, self -> scale, 2) ? -1 : 0;
}

static int Base_setAnchorX(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> anchor[x] = PyFloat_AsDouble(value);
    return ERR(self -> anchor[x]) ? -1 : 0;
}

static int Base_setAnchorY(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> anchor[y] = PyFloat_AsDouble(value);
    return ERR(self -> anchor[y]) ? -1 : 0;
}

static double Base_vecAnchor(Base *self, uint8_t index) {
    return self -> anchor[index];
}

static PyObject *Base_getAnchor(Base *self, void *Py_UNUSED(closure)) {
    Vector *anchor = vectorNew((PyObject *) self, (Getter) Base_vecAnchor, 2);

    anchor -> data[x].set = (setter) Base_setAnchorX;
    anchor -> data[y].set = (setter) Base_setAnchorY;
    anchor -> data[x].name = "x";
    anchor -> data[y].name = "y";

    return (PyObject *) anchor;
}

static int Base_setAnchor(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    return vectorSet(value, self -> anchor, 2);
}

static PyObject *Base_getAngle(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(cpBodyGetAngle(self -> body) * 180 / M_PI);
}

static int Base_setAngle(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const double angle = PyFloat_AsDouble(value);
    return ERR(angle) ? -1 : cpBodySetAngle(self -> body, angle * M_PI / 180), 0;
}

static PyObject *Base_getRed(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[r]);
}

static int Base_setRed(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[r] = PyFloat_AsDouble(value);
    return ERR(self -> color[r]) ? -1 : 0;
}

static PyObject *Base_getGreen(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[g]);
}

static int Base_setGreen(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[g] = PyFloat_AsDouble(value);
    return ERR(self -> color[g]) ? -1 : 0;
}

static PyObject *Base_getBlue(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[b]);
}

static int Base_setBlue(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[b] = PyFloat_AsDouble(value);
    return ERR(self -> color[b]) ? -1 : 0;
}

static PyObject *Base_getAlpha(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> color[a]);
}

static int Base_setAlpha(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> color[a] = PyFloat_AsDouble(value);
    return ERR(self -> color[a]) ? -1 : 0;
}

static double Base_vecColor(Base *self, uint8_t index) {
    return self -> color[index];
}

static PyObject *Base_getColor(Base *self, void *Py_UNUSED(closure)) {
    Vector *color = vectorNew((PyObject *) self, (Getter) Base_vecColor, 4);

    color -> data[r].set = (setter) Base_setRed;
    color -> data[g].set = (setter) Base_setGreen;
    color -> data[b].set = (setter) Base_setBlue;
    color -> data[a].set = (setter) Base_setAlpha;
    color -> data[r].name = "r";
    color -> data[g].name = "g";
    color -> data[b].name = "b";
    color -> data[a].name = "a";

    return (PyObject *) color;
}

static int Base_setColor(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    return vectorSet(value, self -> color, 4);
}

static PyObject *Base_getLeft(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> left(self));
}

static int Base_setLeft(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)
    
    const double result = PyFloat_AsDouble(value);
    if (ERR(result)) return -1;

    self -> pos[x] += result - self -> left(self);
    return pos(self), 0;
}

static PyObject *Base_getTop(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> top(self));
}

static int Base_setTop(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)
    
    const double result = PyFloat_AsDouble(value);
    if (ERR(result)) return -1;

    self -> pos[y] += result - self -> top(self);
    return pos(self), 0;
}

static PyObject *Base_getRight(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> right(self));
}

static int Base_setRight(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)
    
    const double result = PyFloat_AsDouble(value);
    if (ERR(result)) return -1;

    self -> pos[x] += result - self -> right(self);
    return pos(self), 0;
}

static PyObject *Base_getBottom(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> bottom(self));
}

static int Base_setBottom(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)
    
    const double result = PyFloat_AsDouble(value);
    if (ERR(result)) return -1;

    self -> pos[y] += result - self -> bottom(self);
    return pos(self), 0;
}

static PyObject *Base_getType(Base *self, void *Py_UNUSED(closure)) {
    return PyLong_FromLong(cpBodyGetType(self -> body));
}

static int Base_setType(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const long type = PyLong_AsLong(value);
    if (ERR(type)) return -1;

    if (type != CP_BODY_TYPE_DYNAMIC && type != CP_BODY_TYPE_KINEMATIC) {
        PyErr_SetString(PyExc_ValueError, "type must be DYNAMIC or STATIC");
        return -1;
    }

    return cpBodySetType(self -> body, type), baseMoment(self), 0;
}

static PyObject *Base_getMass(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(cpBodyGetMass(self -> body));
}

static int Base_setMass(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const double mass = PyFloat_AsDouble(value);
    return ERR(mass) ? -1 : cpBodySetMass(self -> body, mass), baseMoment(self), 0;
}

static PyObject *Base_getElasticity(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> elasticity);
}

static int Base_setElasticity(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    if (ERR(self -> elasticity = PyFloat_AsDouble(value))) return -1;
    FOR(size_t, self -> length) cpShapeSetElasticity(self -> shapes[i], self -> elasticity);

    return 0;
}

static PyObject *Base_getFriction(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(self -> friction);
}

static int Base_setFriction(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    if (ERR(self -> friction = PyFloat_AsDouble(value))) return -1;
    FOR(size_t, self -> length) cpShapeSetFriction(self -> shapes[i], self -> friction);

    return 0;
}

static int Base_setVelocityX(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> vel[x] = PyFloat_AsDouble(value);
    return ERR(self -> vel[x]) ? -1 : cpBodySetVelocity(self -> body, cpv(self -> vel[x], self -> vel[y])), 0;
}

static int Base_setVelocityY(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    self -> vel[y] = PyFloat_AsDouble(value);
    return ERR(self -> vel[y]) ? -1 : cpBodySetVelocity(self -> body, cpv(self -> vel[x], self -> vel[y])), 0;
}

static double Base_vecVelocity(Base *self, uint8_t index) {
    return self -> vel[index];
}

static PyObject *Base_getVelocity(Base *self, void *Py_UNUSED(closure)) {
    Vector *speed = vectorNew((PyObject *) self, (Getter) Base_vecVelocity, 2);

    speed -> data[x].set = (setter) Base_setVelocityX;
    speed -> data[y].set = (setter) Base_setVelocityY;
    speed -> data[x].name = "x";
    speed -> data[y].name = "y";

    return (PyObject *) speed;
}

static int Base_setVelocity(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    return vectorSet(value, self -> vel, 2) ? -1 : cpBodySetVelocity(self -> body, cpv(self -> vel[x], self -> vel[y])), 0;
}

static PyObject *Base_getAngularVelocity(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(cpBodyGetAngularVelocity(self -> body) * 180 / M_PI);
}

static int Base_setAngularVelocity(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const double velocity = PyFloat_AsDouble(value);
    return ERR(velocity) ? -1 : cpBodySetAngularVelocity(self -> body, velocity * M_PI / 180), 0;
}

static PyObject *Base_getTorque(Base *self, void *Py_UNUSED(closure)) {
    return PyFloat_FromDouble(cpBodyGetTorque(self -> body));
}

static int Base_setTorque(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const double torque = PyFloat_AsDouble(value);
    return ERR(torque) ? -1 : cpBodySetTorque(self -> body, torque), 0;
}

static PyObject *Base_getRotate(Base *self, void *Py_UNUSED(closure)) {
    return PyBool_FromLong(self -> rotate);
}

static int Base_setRotate(Base *self, PyObject *value, void *Py_UNUSED(closure)) {
    DEL(value)

    const int result = PyObject_IsTrue(value);
    if (result == -1) return -1;
    
    self -> rotate = result;
    return baseMoment(self), 0;
}

static PyObject *Base_getGrounded(Base *self, void *Py_UNUSED(closure)) {
    bool grounded = false;

    cpBodyEachArbiter(self -> body, (cpBodyArbiterIteratorFunc) arbiter, &grounded);
    return PyBool_FromLong(grounded);
}

static PyObject *Base_lookAt(Base *self, PyObject *object) {
    vec2 pos;
    
    if (other(object, pos)) return NULL;
    const double value = atan2(pos[y] - self -> pos[y], pos[x] - self -> pos[x]);

    cpBodySetAngle(self -> body, value * 180 / M_PI);
    Py_RETURN_NONE;
}

static PyObject *Base_moveToward(Base *self, PyObject *args) {
    if (baseToward(self -> pos, args)) return NULL;
    pos(self);

    Py_RETURN_NONE;
}

static PyObject *Base_moveSmooth(Base *self, PyObject *args) {
    if (baseSmooth(self -> pos, args)) return NULL;
    pos(self);

    Py_RETURN_NONE;
}

static PyObject *Base_force(Base *self, PyObject *args) {
    cpVect pos, force;

    if (vect(self, args, &force.x, &force.y, &pos.x, &pos.y))
        return NULL;

    cpBodyApplyForceAtLocalPoint(self -> body, force, pos);
    Py_RETURN_NONE;
}

static PyObject *Base_impulse(Base *self, PyObject *args) {
    cpVect pos, impulse;

    if (vect(self, args, &impulse.x, &impulse.y, &pos.x, &pos.y))
        return NULL;

    cpBodyApplyImpulseAtLocalPoint(self -> body, impulse, pos);
    Py_RETURN_NONE;
}

static PyGetSetDef BaseGetSetters[] = {
    {"x", (getter) Base_getX, (setter) Base_setX, "x position of the object", NULL},
    {"y", (getter) Base_getY, (setter) Base_setY, "y position of the object", NULL},
    {"position", (getter) Base_getPos, (setter) Base_setPos, "position of the object", NULL},
    {"pos", (getter) Base_getPos, (setter) Base_setPos, "position of the object", NULL},
    {"scale", (getter) Base_getScale, (setter) Base_setScale, "scale of the object", NULL},
    {"anchor", (getter) Base_getAnchor, (setter) Base_setAnchor, "rotation origin of the object", NULL},
    {"angle", (getter) Base_getAngle, (setter) Base_setAngle, "angle of the object", NULL},
    {"red", (getter) Base_getRed, (setter) Base_setRed, "red color of the object", NULL},
    {"green", (getter) Base_getGreen, (setter) Base_setGreen, "green color of the object", NULL},
    {"blue", (getter) Base_getBlue, (setter) Base_setBlue, "blue color of the object", NULL},
    {"alpha", (getter) Base_getAlpha, (setter) Base_setAlpha, "opacity of the object", NULL},
    {"color", (getter) Base_getColor, (setter) Base_setColor, "color of the object", NULL},
    {"left", (getter) Base_getLeft, (setter) Base_setLeft, "left position of the object", NULL},
    {"top", (getter) Base_getTop, (setter) Base_setTop, "top position of the object", NULL},
    {"right", (getter) Base_getRight, (setter) Base_setRight, "right position of the object", NULL},
    {"bottom", (getter) Base_getBottom, (setter) Base_setBottom, "bottom position of the object", NULL},
    {"type", (getter) Base_getType, (setter) Base_setType, "physics body of the object", NULL},
    {"mass", (getter) Base_getMass, (setter) Base_setMass, "weight of the object", NULL},
    {"weight", (getter) Base_getMass, (setter) Base_setMass, "weight of the object", NULL},
    {"elasticity", (getter) Base_getElasticity, (setter) Base_setElasticity, "bounciness of the object", NULL},
    {"friction", (getter) Base_getFriction, (setter) Base_setFriction, "roughness of the object", NULL},
    {"velocity", (getter) Base_getVelocity, (setter) Base_setVelocity, "physics speed of the object", NULL},
    {"speed", (getter) Base_getVelocity, (setter) Base_setVelocity, "physics speed of the object", NULL},
    {"angular_velocity", (getter) Base_getAngularVelocity, (setter) Base_setAngularVelocity, "physics rotation speed of the object", NULL},
    {"rotate_speed", (getter) Base_getAngularVelocity, (setter) Base_setAngularVelocity, "physics rotation speed of the object", NULL},
    {"rotate", (getter) Base_getRotate, (setter) Base_setRotate, "the object is able to rotate in a physics engine", NULL},
    {"torque", (getter) Base_getTorque, (setter) Base_setTorque, "rotational force for the next physics frame", NULL},
    {"grounded", (getter) Base_getGrounded, NULL, "the physics body is touching the ground", NULL},
    {NULL}
};

static PyMethodDef BaseMethods[] = {
    {"collides_with", collide, METH_O, "check if the object collides with another object"},
    {"collide", collide, METH_O, "check if the object collides with another object"},
    {"look_at", (PyCFunction) Base_lookAt, METH_O, "rotate the object so that it points to another object"},
    {"move_toward", (PyCFunction) Base_moveToward, METH_VARARGS, "move the object toward another object"},
    {"move_smooth", (PyCFunction) Base_moveSmooth, METH_VARARGS, "move the object smoothly toward another object"},
    {"force", (PyCFunction) Base_force, METH_VARARGS, "apply a force to the object body"},
    {"impulse", (PyCFunction) Base_impulse, METH_VARARGS, "apply an impulse to the object body"},
    {NULL}
};

void baseUniform(mat matrix, vec4 vec) {
    glUniformMatrix4fv(uniform[obj], 1, GL_FALSE, matrix);
    glUniform4f(uniform[color], (GLfloat) vec[r], (GLfloat) vec[g], (GLfloat) vec[b], (GLfloat) vec[a]);
}

void baseDealloc(Base *self) {
    cpBodyFree(self -> body);
    free(self -> shapes);

    Py_TYPE(self) -> tp_free((PyObject *) self);
}

int baseToward(vec2 this, PyObject *args) {
    double speed = 1;
    PyObject *object;
    vec2 pos;

    if (!PyArg_ParseTuple(args, "O|d", &object, &speed) || other(object, pos))
        return -1;

    const double px = pos[x] - this[x];
    const double py = pos[y] - this[y];

    if (hypot(px, py) < speed) {
        this[x] += px;
        this[y] += py;
    }

    else {
        const double angle = atan2(py, px);

        this[x] += cos(angle) * speed;
        this[y] += sin(angle) * speed;
    }
    
    return 0;
}

int baseSmooth(vec2 this, PyObject *args) {
    double speed = .1;
    PyObject *object;
    vec2 pos;

    if (!PyArg_ParseTuple(args, "O|d", &object, &speed) || other(object, pos))
        return -1;

    this[x] += (pos[x] - this[x]) * speed;
    this[y] += (pos[y] - this[y]) * speed;
    
    return 0;
}

void baseInit(Base *self) {
    self -> pos[x] = self -> pos[y] = 0;
    self -> vel[x] = self -> vel[y] = 0;
    self -> anchor[x] = self -> anchor[y] = 0;
    self -> scale[x] = self -> scale[y] = 1;

    self -> color[r] = self -> color[g] = self -> color[b] = 0;
    self -> color[a] = 1;

    self -> rotate = 1;
    self -> elasticity = .5;
    self -> friction = .5;
}

void baseStart(Base *self, double angle) {
    cpBodySetMass(self -> body, 1);
    cpBodySetAngle(self -> body, angle);
    cpBodySetAngularVelocity(self -> body, 0);
    cpBodySetType(self -> body, CP_BODY_TYPE_DYNAMIC);
}

void baseMatrix(Base *self, double px, double py) {
    const double sine = sin(cpBodyGetAngle(self -> body));
    const double cosine = cos(cpBodyGetAngle(self -> body));
    const double sx = px * self -> scale[x];
    const double sy = py * self -> scale[y];

    mat matrix = {
        (GLfloat) sx * cosine, (GLfloat) sx * sine, 0, 0,
        (GLfloat) sy * -sine, (GLfloat) sy * cosine, 0, 0, 0, 0, 1, 0,
        (GLfloat) self -> anchor[x] * cosine + self -> anchor[y] * -sine + self -> pos[x],
        (GLfloat) self -> anchor[x] * sine + self -> anchor[y] * cosine + self -> pos[y], 0, 1
    };

    baseUniform(matrix, self -> color);
}

void baseMoment(Base *self) {
    if (cpBodyGetType(self -> body) == CP_BODY_TYPE_DYNAMIC)
        cpBodySetMoment(self -> body, self -> rotate ? self -> moment(self) : INFINITY);
}

PyObject *baseNew(PyTypeObject *type, size_t length) {
    Base *self = (Base *) type -> tp_alloc(type, 0);

    self -> body = cpBodyNew(0, 0);
    self -> shapes = malloc(length * sizeof NULL);

    return (PyObject *) self;
}

PyTypeObject BaseType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "Base",
    .tp_doc = "base class for drawing things",
    .tp_basicsize = sizeof(Base),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = PyType_GenericNew,
    .tp_dealloc = (destructor) baseDealloc,
    .tp_getset = BaseGetSetters,
    .tp_methods = BaseMethods
};
