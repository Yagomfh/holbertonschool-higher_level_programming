#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int len;
	int i;
	PyObject *type;

	if (!p)
		return;
	len = (int)PyList_Size(p);
	i = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n[*] Allocated = %d\n", len, i);
	i = 0;
	while (i < len)
	{
		type = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(type)->tp_name);
		i++;
	}
}
