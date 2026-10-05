#include <Python.h>
#include <stdio.h>
#include <sys/stat.h>

static PyObject* save_to_file(PyObject* self, PyObject* args) {
    const char *path;
    const char *filename;
    const char *content;

    // Parse Python arguments
    if (!PyArg_ParseTuple(args, "sss", &path, &filename, &content)) {
        return NULL;  // PyArg_ParseTuple already sets the error
    }

    // Check if path exists and is a directory
    struct stat st;
    if (stat(path, &st) != 0 || !S_ISDIR(st.st_mode)) {
        char errbuf[1024];
        snprintf(errbuf, sizeof(errbuf), "%s is not a directory", path);
        PyErr_SetString(PyExc_NotADirectoryError, errbuf);
        return NULL;
    }

    // Build full file path
    char fullpath[1024];
    snprintf(fullpath, sizeof(fullpath), "%s\\%s", path, filename);

    // Attempt to open the file for appending but only if the file exists
    FILE *file = fopen(fullpath, "r+");

    if (file == NULL) {
        PyErr_SetFromErrnoWithFilename(PyExc_FileNotFoundError, filename);
        return NULL;
    }

    fseek(file, 0, SEEK_END);  /* Move to end for appending */

    // Write content
    if (fprintf(file, "%s", content) < 0) {
        fclose(file);
        PyErr_SetString(PyExc_IOError, "Failed to write to file.");
        return NULL;
    }

    fclose(file);

    // Return None on success
    Py_RETURN_NONE;
}

static PyMethodDef MyFileSaveModuleMethods[] = {
    {"save_to_file", save_to_file, METH_VARARGS, "Saves content to a file"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef filesavemodule = {
    PyModuleDef_HEAD_INIT,
    "filesavemodule",
    "A simple module that manages files",
    -1,
    MyFileSaveModuleMethods
};

PyMODINIT_FUNC PyInit_filesavemodule(void) {
    return PyModule_Create(&filesavemodule);
}


