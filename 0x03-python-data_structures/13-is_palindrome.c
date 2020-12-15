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
  * get_int - gets int at node list[idx]
  * @head: pointer to head node
  * @idx: index where to retrieve int
  * Return: int value at node list[idx]
  */

int get_int(listint_t *head, int idx)
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
	int len, i = 0;

	if (*head == NULL)
		return (1);

	len = len_l(*head);
	while (i < len)
	{
		if ((*head)->n != get_int(*head, len - 1 - i))
			return (0);
		i++;
		len--;
		*head = (*head)->next;
	}
	return (1);
}
