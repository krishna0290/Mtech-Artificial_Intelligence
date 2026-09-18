#include <stdio.h>

#define MAX 5

int stack[MAX];
int top = -1;

// PUSH - Insertion
void push(int value)
{
    if (top == MAX - 1)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        top++;
        stack[top] = value;
        printf("%d inserted\n", value);
    }
}

// POP - Deletion
void pop()
{
    if (top == -1)
    {
        printf("Stack Underflow\n");
    }
    else
    {
        printf("%d deleted\n", stack[top]);
        top--;
    }
}

// Display stack
void display()
{
    if (top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Stack: ");

        for (int i = top; i >= 0; i--)
        {
            printf("%d ", stack[i]);
        }

        printf("\n");
    }
}

int main()
{
    
    push(1);
    push(2);
    push(3);

    display();

    pop();
    display();

    return 0;
}