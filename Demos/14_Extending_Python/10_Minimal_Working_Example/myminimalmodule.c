#include <Python.h>

static PyObject* hello_world(PyObject* self, PyObject* args) {
    printf("Hello from C!\n");
    Py_RETURN_NONE;
}

static PyMethodDef MyModuleMethods[] = {
    {"hello_world", hello_world, METH_NOARGS, "Prints greeting"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef myminimalmodule = {
    PyModuleDef_HEAD_INIT,
    "myminimalmodule",
    NULL,
    -1,
    MyModuleMethods
};

PyMODINIT_FUNC PyInit_myminimalmodule(void) {
    return PyModule_Create(&myminimalmodule);
}