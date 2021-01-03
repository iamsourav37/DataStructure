#include <iostream>
using namespace std;

class Stack
{
private:
    int top;
    int length;
    int *stack_array;
    void initArray()
    {
        stack_array = new int[1];
        length = 1;
    }
    void doubleArray()
    {

        int *temp = new int[length * 2];

        if (temp == NULL)
        {
            cout << "\n\n\tStack Overflow";
            exit(0);
        }
        length *= 2;
        for (int i = 0; i < length / 2; i++)
        {
            temp[i] = stack_array[i];
        }
        stack_array = temp;
    }

    void shrinkArray()
    {
        int *temp = new int[length / 2];

        length /= 2;
        for (int i = 0; i < length; i++)
        {
            temp[i] = stack_array[i];
        }
        stack_array = temp;
    }
    bool isEmpty()
    {
        if (top == -1)
            return true;
        else
            return false;
    }

public:
    Stack()
    { // default constructor
        top = -1;
        length = 0;
        stack_array = NULL;
    }

    void push(int data)
    {
        if (length == 0)
            initArray();
        if (top == length - 1)
            doubleArray();
        top = top + 1;
        stack_array[top] = data;
    }
    void pop()
    {
        if (isEmpty())
        {
            cout << "\n\n\t Stack underflow";
            return;
        }
        top = top - 1; // 1 2 0 0
        if (top == (length / 2) - 1)
            shrinkArray();
    }
    int peek()
    {
        if (isEmpty())
        {
            cout << "\n\n\t Stack underflow";
            return -1;
        }
        return stack_array[top];
    }
    void display()
    {
        if (isEmpty())
        {
            cout << "\n\n\t Stack underflow";
            return;
        }
        cout << "\n\n\t Stack Length : " << top + 1;
        cout << "\n\n\t Length : " << length;
        cout << "\n\n Stack : \n";
        for (int i = top; i >= 0; i--)
        {
            cout << "\t" << stack_array[i] << endl;
        }
    }
};

int main()
{
    int choice;
    Stack stack = Stack();
    while (true)
    {
        cout << "\n\t 1. Push" << endl;
        cout << "\n\t 2. Pop" << endl;
        cout << "\n\t 3. Peek" << endl;
        cout << "\n\t 4. Display" << endl;
        cout << "\n\t 5. Exit" << endl;
        cout << "\n\n\t Enter Your Choice : " << endl;
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "\n\n\t Enter data : ";
            int data;
            cin >> data;
            stack.push(data);
            break;
        case 2:
            stack.pop();
            break;
        case 3:
            cout << "\n\n\t Peek : " << stack.peek();
            break;
        case 4:
            stack.display();
            break;
        case 5:
            exit(0);
            break;

        default:
            cout << "\n\n\t Wrong Choice";
            break;
        }
    }

    return 0;
}