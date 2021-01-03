#include <iostream>
using namespace std;

#define STACK_SIZE 10 // Size of array

class Stack
{

private:
    int top;
    int stack_array[STACK_SIZE];

public:
    Stack()
    { // default constructor
        top = -1;
    }
    bool isEmpty()
    {
        if (top == -1)
            return true;
        else
            return false;
    }
    bool isFull()
    {
        if (top == STACK_SIZE - 1)
            return true;
        else
            return false;
    }
    void push(int data)
    {
        if (isFull())
        {
            cout << "\n\t Stack is overflow\n";
            return;
        }

        top = top + 1;
        stack_array[top] = data;
    }
    int peek()
    {
        if (isEmpty())
        {
            cout << "\n\t Stack is underflow\n";
            return -1;
        }
        return stack_array[top];
    }
    int pop()
    {
        if (isEmpty())
        {
            cout << "\n\t Stack is underflow\n";
            return -1;
        }
        return stack_array[top--];
    }

    void display()
    {
        if (isEmpty())
        {
            cout << "\n\t Stack is underflow\n";
            return;
        }

        cout << "\nStack : " << endl;
        for (int i = top; i >= 0; i--)
        {
            cout << "\t" << stack_array[i] << endl;
        }

        cout << endl;
    }
};

int main()
{
    Stack stack = Stack();

    stack.push(12);
    stack.push(20);
    stack.push(9);
    stack.push(17);
    stack.push(33);
    stack.display();
    cout << "\nPoped element is : " << stack.pop();
    stack.display();
    cout << "\nPoped element is : " << stack.pop();
    cout << "\nPoped element is : " << stack.pop();
    cout << "\nPoped element is : " << stack.pop();
    cout << "\nPoped element is : " << stack.pop();
    cout << "\nPoped element is : " << stack.pop();
    cout << "\nPoped element is : " << stack.pop();

    return 0;
}
