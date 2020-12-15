#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome
  * @head: pointer to head node
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome
  */

int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, elem[5024];

	if (*head == NULL)
		return (1);

	while (*head)
	{
		elem[len] = (*head)->n;
		*head = (*head)->next;
		len++;
	}
	while (i < len)
	{
		if (elem[i] != elem[len - 1])
			return (0);
		i++;
		len--;
	}
	return (1);
}
