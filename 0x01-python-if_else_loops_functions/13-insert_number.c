#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert node
 * @head: pointer
 * @number: num
 * Return: void
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		if (current->n > number)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		while (current->next)
		{
			if ((current->next)->n > number)
			{
				break;
			}
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
