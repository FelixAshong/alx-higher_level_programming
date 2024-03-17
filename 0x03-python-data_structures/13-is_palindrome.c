#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int check_size(listint_t *head);

/**
 * is_palindrome - check if the linked list is a palindrome
 * @head: list to be checked
 *
 * Return: 0 if it isnt and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int size = check_size(temp), i = 0;
	int check_A[12700];

	if (check_A == NULL)
		return (0);
	if (size == 0)
	{
		return (1);
	}
	while (temp != NULL)
	{
		check_A[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = 0; i < size; i++)
	{
		if (check_A[i] != check_A[(size - 1) - i])
		{
			return (0);
		}
	}
	return (1);
}

/**
 * check_size - return size of list
 * @head: list to be checked
 *
 * Return: size of list
 */

int check_size(listint_t *head)
{
	int i = 0;

	while (head != NULL)
	{
		i++;
		head = head->next;
	}
	return (i);
}
