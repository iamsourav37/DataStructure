package queue;public class QueueRunner{
    public static void main(String[] args) {
        Queue q = new Queue(5);

        q.enqueue(12);
        System.out.println("Size of the queue : "+q.getSize());
        q.enqueue(22);
        System.out.println("Size of the queue : "+q.getSize());
        q.enqueue(72);
        System.out.println("Size of the queue : "+q.getSize());
        q.enqueue(189);
        System.out.println("Size of the queue : "+q.getSize());
        q.enqueue(91);
        System.out.println("Size of the queue : "+q.getSize());


        System.out.println("Delete element : "+q.dequeue());
        System.out.println("Delete element : "+q.dequeue());
        System.out.println("After delete two element size of the queue : "+q.getSize());

        System.out.println("Delete element : "+q.dequeue());

        q.display();
    }

}
