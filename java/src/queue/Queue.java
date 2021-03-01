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
        return this.front == this.capacity-1;
    }
    private boolean isEmpty(){
        return this.rear == -1;
    }

    public void enqueue(int data){
        if(isFull()){
            System.out.println("Queue is full");
            return;
        }
        if(rear == -1){
           rear = front = 0;
        }else{
            front++;
        }
        this.queue[front] = data;
    }
    public int dequeue(){
        if(isEmpty()){
            System.out.println("Queue is empty");
            return -1;
        }
        int delete_data = this.queue[rear];
        rear++;
        return delete_data;
    }

    public void display(){
        if(isEmpty()){
            System.out.println("Queue is empty");
            return;
        }
        for(int i=rear; i<=front; i++){
            System.out.print(this.queue[i]+" ");
        }
        System.out.println();
    }
    public int getSize(){
        return this.front - this.rear +1;
    }

}
