#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
int rec_ispal(listint_t **left, listint_t *right);
/**
 * rev - reverse linked list
 * @h: head of list
 * Return: head of list
 */
listint_t *rev(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*h)
	{
		next = (*h)->next;
		(*h)->next = prev;
		prev = *h;
		*h = next;
	}
	*h = prev;
	return (*h);
}

/**
 * is_palindrome - checks if list is palindrome
 * @head: head of list
 * Return: 1 if true
 */
int is_palindrome(listint_t **head)
{
	if (!*head)
		return (1);
	return (rec_ispal(head, *head));
}
/**
 * rec_ispal - checks for palindrome recursively
 * @left: left pointer
 * @right: right pointer
 * Return: 1 if palindrome
 */
int rec_ispal(listint_t **left, listint_t *right)
{
	int res = 1;
	int res1 = 1;

	if (!right)
		return (1);

	res = rec_ispal(left, right->next);
	if (res == 0)
		return (0);

	res1 = ((*left)->n == right->n);
	(*left) = (*left)->next;
	return (res1);
}

