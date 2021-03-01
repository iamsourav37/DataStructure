package queue;public class QueueRunner{
    public static void main(String[] args) {
        Queue q = new Queue(5);

        q.enqueue(12);
        q.enqueue(22);
        q.enqueue(72);
        q.enqueue(189);
        q.enqueue(91);

        System.out.println("Delete element : "+q.dequeue());
        System.out.println("Delete element : "+q.dequeue());
        System.out.println("Delete element : "+q.dequeue());

        q.display();
    }

}
