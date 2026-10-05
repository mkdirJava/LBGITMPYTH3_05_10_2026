#include <Python.h>

static PyObject* square(PyObject* self, PyObject* args) {
    int x;
    if (!PyArg_ParseTuple(args, "i", &x)) {
        return NULL;
    }
    int result = x * x;
    return PyLong_FromLong(result);
}

static PyObject* power(PyObject* self, PyObject* args) {
    int base, exponent;
    if (!PyArg_ParseTuple(args, "ii", &base, &exponent)) {
        return NULL;
    }
    long long result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return PyLong_FromLong(result);
}

static PyObject *join(PyObject *self, PyObject *args)
{
    PyObject *tuple1;
    PyObject *tuple2;

    if(!PyArg_ParseTuple(args, "O!O!", //"O!" means: “Expect an object of a specific type”
                     &PyTuple_Type, &tuple1,
                     &PyTuple_Type, &tuple2))
        return NULL;

    // Ensure both arguments are actually Python tuples
    if (!PyTuple_Check(tuple1) || !PyTuple_Check(tuple2)) {
        PyErr_SetString(PyExc_TypeError, "Both arguments must be tuples.");
        return NULL;
    }

    // Concatenate them together and assign to a new variable
    PyObject* new_tuple = PySequence_Concat(tuple1, tuple2);
    return new_tuple;
}

static PyObject* save(PyObject* self, PyObject* args) {
    int base, exponent;
    if (!PyArg_ParseTuple(args, "ii", &base, &exponent)) {
        return NULL;
    }
    long long result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return PyLong_FromLong(result);
}

static PyMethodDef MyMathsModuleMethods[] = {
    {"square", square, METH_VARARGS, "Squares a number"},
    {"power", power, METH_VARARGS, "raises an exponent to a power"},
    {"join", join, METH_VARARGS, "Joins two tuples"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mymathsmodule = {
    PyModuleDef_HEAD_INIT,
    "mymathsmodule",
    "A simple maths extension module",
    -1,
    MyMathsModuleMethods
};

PyMODINIT_FUNC PyInit_mymathsmodule(void) {
    return PyModule_Create(&mymathsmodule);
}


