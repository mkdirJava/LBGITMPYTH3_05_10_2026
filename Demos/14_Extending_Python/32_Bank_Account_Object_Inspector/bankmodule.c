#include <Python.h>

static PyObject* process_account(PyObject* self, PyObject* args) {
    PyObject *account;

    // 1. Parse input (expects any Python object)
    if (!PyArg_ParseTuple(args, "O", &account)) {
        return NULL;
    }

    // 🔹 Show we received a borrowed reference
    printf("Received account object\n");

    // 🔹 Increment reference count
    Py_INCREF(account);
    printf("After Py_INCREF\n");

    // 2. Verify it is actually a dictionary
    if (!PyDict_Check(account)) {
        PyErr_SetString(PyExc_TypeError, "Arg must be a dictionary.");
        return NULL;
    }

    // 3. Look up the "balance" key (borrowed reference, do not decref)
    PyObject* balance_obj = PyDict_GetItemString(account, "balance");
    if (balance_obj == NULL) {
        PyErr_SetString(PyExc_KeyError, "Key 'balance' not found.");
        return NULL;
    }

    // 4. Convert the Python int to a standard C long long
    long long current_balance = PyLong_AsLongLong(balance_obj);
    if (current_balance == -1 && PyErr_Occurred()) {
        return NULL; // Balance was not a valid integer type
    }

    // 5. Add 100 to the value
    current_balance += 100;

    // 6. Create a new Python integer object (new reference)
    PyObject* new_balance_obj = PyLong_FromLongLong(current_balance);
    if (new_balance_obj == NULL) {
        return NULL;
    }

    // 7. Update the dictionary with the new object
    // PyDict_SetItemString steals a reference to new_balance_obj in modern versions,
    // but manually decref'ing it is standard practice to avoid memory leaks.
    if (PyDict_SetItemString(account, "balance", new_balance_obj) < 0) {
        Py_DECREF(new_balance_obj);
        return NULL;
    }

    Py_DECREF(new_balance_obj); // Clean up our reference

    // 🔹 Decrement reference count
    Py_DECREF(account);
    printf("After Py_DECREF\n");

    // 🔹 Return the original object
    // excluding the increment will result in the python client apparently
    // running OK but terminating with a message like the following:
    // Process finished with exit code -1073741819 (0xC0000005)
    // which means that the Python script crashed due to a
    // Windows STATUS_ACCESS_VIOLATION (Segmentation Fault).
    // This is a low-level critical crash. It occurs when a program
    // tries to read or write to a restricted or invalid memory location.
    // Because pure Python code manages its own memory, it almost never throws this error.
    // Seeing this error indicates a problem with native compiled code interacting with Python.
    //Py_INCREF(account);  // must increment before returning

    return account;
}

static PyMethodDef BankMethods[] = {
    {"process_account", process_account, METH_VARARGS, "Process account objects"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef bankmodule = {
    PyModuleDef_HEAD_INIT,
    "bankmodule",
    "Banking reference count demo",
    -1,
    BankMethods
};

PyMODINIT_FUNC PyInit_bankmodule(void) {
    return PyModule_Create(&bankmodule);
}


