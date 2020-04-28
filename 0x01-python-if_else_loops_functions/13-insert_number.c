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
	listint_t *cpy, *tmp = *head;

	cpy = malloc(sizeof(listint_t));
	if (!cpy)
		return (NULL);

	cpy->n = val;
	cpy->next = NULL;
	while (tmp)
	{
		if (tmp == NULL || cpy->n < tmp->next->n)
		{
			cpy->next = tmp->next;
			tmp->next = cpy;
			return (tmp);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
