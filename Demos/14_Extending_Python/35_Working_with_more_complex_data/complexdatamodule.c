#include <Python.h>
#include <stdio.h>

static PyObject* sum_balances(PyObject* self, PyObject* args) {

PyErr_SetString(...)
PyErr_SetFromErrno(...)

    PyObject *list;
    double total = 0;

    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &list)) {
        return NULL;
    }

    Py_ssize_t size = PyList_Size(list);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(list, i);  // borrowed
        total += PyFloat_AsDouble(item);
    }

    return PyFloat_FromDouble(total);
}

static PyMethodDef BankMethods[] = {
    {"sum_balances", sum_balances, METH_VARARGS, "Summates balances"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef complexdatamodule = {
    PyModuleDef_HEAD_INIT,
    "complexdatamodule",
    "Banking summate bank balances",
    -1,
    BankMethods
};

PyMODINIT_FUNC PyInit_complexdatamodule(void) {
    return PyModule_Create(&complexdatamodule);
}

