#include "lists.h"
/**
 * palindrome - using recursion to check for palindrome
 * @l: pointer to list
 * @r: list
 *
 * Return: 1 if its a palindrome, 0 otherwise
 */
int palindrome(listint_t **l, listint_t *r)
{
	int res;

	if (r != NULL)
	{
		res = palindrome(l, r->next);
		if (res != 0)
		{
			res = (r->n == (*l)->n);
			*l = (*l)->next;
			return (res);
		}
		return (0);
	}
	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list
 *
 * Return: 1 if its a palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
		return (0);
	return (palindrome(head, *head));
}
