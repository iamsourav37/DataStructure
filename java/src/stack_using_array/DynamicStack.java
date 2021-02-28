package stack_using_array;

public class DynamicStack {
    private int capacity;
    private int[] stack_array;
    private int top;

    public DynamicStack(){
        capacity = 0;
        stack_array = null;
        top = -1;
    }
    private void initArray(){
        this.capacity = 1;
        this.stack_array = new int[capacity];
    }
    private boolean isEmpty(){
        return this.top == -1;
    }
    private void doubleArray(){
        // double the array
    }
    private void shrinkArray(){
        // half the array
    }
    public void push(int data){
        if(this.capacity == 0)
            this.initArray();
        else if(this.top == this.capacity-1)
            this.doubleArray();

        this.top++;
        this.stack_array[this.top] = data;
    }
    public int pop(){
        if(this.isEmpty()){
            System.out.println("Stack is underflow");
            return -1;
        }
        int popData = this.stack_array[this.top];
        this.top--;

        if(this.top == this.capacity/2-1)
            this.shrinkArray();

        return popData;
    }
    public int peek(){
        if(this.isEmpty()){
            System.out.println("Stack is underflow");
            return -1;
        }
        return this.stack_array[this.top];
    }
    public void display(){
        if(this.isEmpty()){
            System.out.println("Stack is underflow");
            return;
        }
        for (int i= this.top; i>=0; i--)
            System.out.println(this.stack_array[i]);
    }
    public int getSize(){
        return this.top+1;
    }
}
