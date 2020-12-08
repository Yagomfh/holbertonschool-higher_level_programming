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
	listint_t *current, *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else if (number < current->n)
	{
		new->next =*head;
		*head = new;
	}
	else
	{
		while (current->next != NULL && number > current->next->n)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
