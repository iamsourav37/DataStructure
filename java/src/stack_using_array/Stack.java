package stack_using_array;

public class Stack {
    private int stack[];
    final private int capacity;
    private int top;
    Stack(int capacity){
        this.capacity = capacity;
        this.stack = new int[capacity];
        this.top = -1;
    }
    private boolean isEmpty(){
        return this.top == -1;
    }
    private boolean isFull(){
        return this.top == this.capacity-1;
    }
    public void push(int data){
        if(this.isFull()){
            System.out.println("Stack is overflow");
            return;
        }

        this.top++;
        this.stack[this.top] = data;
    }
    public int pop(){
        if(this.isEmpty()){
            System.out.println("Stack is underflow");
            return -1;
        }
        return this.stack[this.top--];
    }
    public int peek(){
        if(this.isEmpty()){
            System.out.println("Stack is underflow");
            return -1;
        }
        return this.stack[this.top];
    }
    public void display(){
        if(this.isEmpty()){
            System.out.println("Stack is underflow");
            return;
        }
        for(int i = this.top; i>=0; i--){
            System.out.println(this.stack[i]);
        }
    }

    public int getSize(){
        return this.top+1;
    }
}
