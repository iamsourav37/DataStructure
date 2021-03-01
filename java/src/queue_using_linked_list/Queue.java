package queue_using_linked_list;

public class Queue {
    private QNode head;
    private int size;


    public Queue(){
        head = null;
        size = 0;
    }
    public void enqueue(int data){
        QNode qNode = new QNode(data);
        qNode.setNext(this.head);
        this.head = qNode;
        this.size++;
    }
    public int dequeue(){
        if(this.head == null){
            System.out.println("Queue is empty");
            return -1;
        }
        QNode tmp = this.head;
        // if list has only one element
        if(this.head.getNext() == null){
            this.size = 0;
            int data = this.head.getData();
            this.head = null;
            return data;
        }

        // list has atleast two element
        while (tmp.getNext().getNext() != null){
            tmp = tmp.getNext();
        }
        this.size--;
        int data = tmp.getNext().getData();
        tmp.setNext(null);
        return data;
    }
    public void display(){
        if(this.head == null){
            System.out.println("Queue is empty");
            return;
        }
        QNode tmp = this.head;
        while (tmp != null){
            System.out.print(tmp.getData()+" ");
            tmp = tmp.getNext();
        }
        System.out.println();
    }
    public int peek(){
        if(this.head == null)
            return -1;
        else{
            QNode tmp = this.head;
            while (tmp.getNext().getNext() != null){
                tmp = tmp.getNext();
            }
            return tmp.getNext().getData();
        }

    }
    public int getSize(){
        return this.size;
    }
}
