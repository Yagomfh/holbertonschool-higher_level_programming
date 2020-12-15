#include "lists.h"

/**
  * len_l - calculates len of linked list
  * @head: pointer to head node
  * Return: len or 0 is NULL
  */

int len_l(listint_t *head)
{
	int res = 0;

	while (head)
	{
		res++;
		head = head->next;
	}
	return (res);
}

/**
  * get_int_at_idx - gets int at node list[idx]
  * @head: pointer to head node
  * @idx: index where to retrieve int
  * Return: int value at node list[idx]
  */

int get_int_at_idx(listint_t *head, int idx)
{
	int res;

	while (idx >= 0)
	{
		res = head->n;
		idx--;
		head = head->next;
	}
	return (res);
}

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to head node
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	int len, node1, node2, i = 0;

	if (*head == NULL)
		return (1);

	len = len_l(*head);
	while (i <= len)
	{
		node1 = get_int_at_idx(*head, i);
		node2 = get_int_at_idx(*head, len - 1);
		if (node1 != node2)
			return (0);
		i++;
		len--;
	}
	return (1);
}
