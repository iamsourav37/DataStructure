package single_linked_list;

public class Runner {
    public static void main(String[] args) {
        System.out.println("Single LinkedList implementation in Java");
        SingleLinkedList list = new SingleLinkedList();

        list.insertLast(12);
        list.insertLast(7);
        list.insertLast(77);
        list.insertLast(89);
        list.insertAt(3, 445);
        list.insertBefore(89, 87);
        list.insertAfter(77, 88);
        list.insertAfter(12, 21);
        list.insertBefore(21, 20);
        list.insertFirst(399);

        System.out.println("Size of list is : "+list.getLength());
        list.showList();

        // remove method testing
        System.out.println("Delete operation :");

        list.removeFirst();
        list.removeLast();
        list.removeAt(2);
        list.removeAt(0);
        list.removeAt(5);
        list.remove(88);
        list.remove(7);
        list.removeFirst();
        list.removeLast();
        list.remove(77);



        System.out.println("Size of list is : "+list.getLength());
        list.showList();

    }
}
