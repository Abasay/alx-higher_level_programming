#include "lists.h"

/**
 * check_cycle - ch3ck if a linked lists contains a circle
 * @list: linked list to ch3ck
 * Return: 1 if it has a cycle and 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
