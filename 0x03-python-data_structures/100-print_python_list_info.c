#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - shows info about python lists
 * @p: object
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int size, a, i;

	i = 0;
	PyObject *obj;

	size = PyList_Size(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", a);
	while (i < size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
