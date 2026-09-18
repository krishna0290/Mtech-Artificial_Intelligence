#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Node *top = NULL;

// PUSH - Insertion
void push(int value)
{
    struct Node *newNode;

    newNode = (struct Node *)malloc(sizeof(struct Node));

    if (newNode == NULL)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        newNode->data = value;
        newNode->next = top;
        top = newNode;

        printf("%d inserted\n", value);
    }
}

// POP - Deletion
void pop()
{
    struct Node *temp;

    if (top == NULL)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        temp = top;

        printf("%d deleted\n", top->data);

        top = top->next;

        free(temp);
    }
}

// Display stack
void display()
{
    struct Node *temp = top;

    if (top == NULL)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Stack: ");

        while (temp != NULL)
        {
            printf("%d ", temp->data);
            temp = temp->next;
        }

        printf("\n");
    }
}

int main()
{
    push(1);
    push(2);
    push(3);
    push(5);

    display();

    pop();
    pop();
    display();

    return 0;
}