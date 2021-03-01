package queue_using_linked_list;

public class Runner {
    public static void main(String[] args) {
        Queue q = new Queue();

        q.enqueue(12);
        q.enqueue(22);
        q.enqueue(32);
        q.enqueue(36);
        q.enqueue(71);
        q.enqueue(90);
        q.enqueue(121);
        q.enqueue(768);

        System.out.println("Size of the queue : "+ q.getSize());

        System.out.println("Delete element : "+q.dequeue());
        System.out.println("Delete element : "+q.dequeue());

        System.out.println("After deleting 2 elements size of the queue : "+ q.getSize());
        q.dequeue();
        System.out.println("Peek element : "+ q.peek());
        q.display();

    }
}
