#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a node into the begging of a list
 * @head: pointer to the head of the list
 * @val: val to add to new member
 * Return: member added
 */
listint_t *insert_node(listint_t **head, int val)
{
	listint_t *cpy, *tmp;

	cpy = malloc(sizeof(listint_t));
	if (!cpy)
		return (NULL);

	cpy->n = val;
	cpy->next = *head;
	if (head == NULL || val <= (*head)->n)
	{
		*head = cpy;
		return (cpy);
	}
	tmp = *head;
	cpy->next = tmp->next;
	while (tmp->next != NULL)
	{
		if (tmp->n <= val && cpy->next->n >= val)
		{
			tmp->next = cpy;
			return (cpy);
		}
		tmp = tmp->next;
		cpy->next = tmp->next;
	}
	tmp->next = cpy;
	return (cpy);
}
