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
	if (*head == NULL || (*head)->n >= new_list->n)
	{
		new_list->next = *head;
		*head = new_list;
		return (new_list);
	}
	while (current->next != NULL && current->next->n < new_list->n)
		current = current->next;
	new_list->next = current->next;
	current->next = new_list;
	return (new_list);
}
