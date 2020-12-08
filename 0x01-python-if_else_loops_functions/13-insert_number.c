#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: pointer to head node
  * @number: number to add
  * Return: address of the new node, or NULL if it failed
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new, *last;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}

	while (current->next != NULL)
	{
		if (number <= current->n && number <= current->next->n)
		{
			last->next = new;
			new->next = current;
			break;
		}
		last = current;
		current = current->next;
	}
	return (new);
}
