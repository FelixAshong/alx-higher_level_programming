#include "lists.h"
/**
 * check_cycle - check if loop exists in cycle
 * @list: struct to be checked
 *
 * Return: 1 if it is, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *hare = list;

	if (list == NULL)
		return (0);
	while (turtle != NULL && hare != NULL && hare->next != NULL)
	{
		turtle = turtle->next;
		hare = (hare->next)->next;
		if (turtle == hare)
			return (1);
	}
	return (0);
}
