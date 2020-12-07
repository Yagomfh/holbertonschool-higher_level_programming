#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: the singly linked list
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
