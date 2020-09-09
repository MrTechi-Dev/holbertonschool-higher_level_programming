#include "lists.h"
/**
 * is_palindrome - check if the string is palindrome.
 * @head: is the list.
 * Return: 1 if is palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	int s[2048];
	int i = 0, j;

	if (!*head || !head)
		return (1);
	while (*head)
	{
		s[i] = (*head)->n;
		head = &(*head)->next;
		i++;
	}
	i--;
	for (j = 0; j < i; j++, i--)
		if (s[j] != s[i])
			return (0);
	return (1);
}
