#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: linked list
 *
 * Return: 0 if false and 2 if it has a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
