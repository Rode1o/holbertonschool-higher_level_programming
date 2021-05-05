#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 *
 * @head: Linked list.
 * @number: New value.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux1, *_nodo, *aux2;

	_nodo = malloc(sizeof(listint_t));
	_nodo->n = number;

	aux1 = *head;
	aux2 = NULL;

	while((aux1 != NULL) && (aux1->n < number))
	{
		aux2 = aux1;
		aux1 = aux1->next;
	}
	if(aux2)
	{
		aux2->next = _nodo;
	}
	else
	{
		*head = _nodo;
	}

	_nodo->next = aux1;

	return(aux1);
	
}
