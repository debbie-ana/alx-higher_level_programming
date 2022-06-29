#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_list;
	listint_t *current;

	new_list = malloc(sizeof(listint_t));
	current = *head;
	if (new_list == NULL)
		return (NULL);
	new_list->n = number;
	new_list->next = NULL;
	while (current != NULL)
	{
		while (current->n < number && current->next != NULL)
			current = current->next;
		if (current->next == NULL)
			current->next = new_list;
		else
		{
			new_list->next = current->next;
			current->next = new_list->next;
		}
	}
	return (new_list);
}
