package queue;

public class Queue {
    private int capacity;
    private int[] queue;
    private int front;
    private int rear;

    public Queue(int capacity){
        this.capacity = capacity;
        this.queue = new int[this.capacity];
        this.front = -1;
        this.rear = -1;
    }

    private boolean isFull(){
        return this.rear == this.capacity-1;
    }
    private boolean isEmpty(){
        return this.front == -1;
    }

    public void enqueue(int data){
        if(isFull()){
            System.out.println("Queue is full");
            return;
        }
        if(rear == -1){
           rear = front = 0;
        }else{
            rear++;
        }
        this.queue[rear] = data;
    }
    public int dequeue(){
        if(isEmpty()){
            System.out.println("Queue is empty");
            return -1;
        }
        int delete_data = this.queue[front];
        front++;
        return delete_data;
    }

    public void display(){
        if(isEmpty()){
            System.out.println("Queue is empty");
            return;
        }
        for(int i=front; i<=rear; i++){
            System.out.print(this.queue[i]+" ");
        }
        System.out.println();
    }
    public int getSize(){
        return this.rear - this.front +1;
    }

}
