package single_linked_list;

public class Runner {
    public static void main(String[] args) {
        System.out.println("Single LinkedList implementation in Java");
        SingleLinkedList list = new SingleLinkedList();

        list.insertFirst(12);
        list.insertFirst(22);
        list.insertFirst(21);
        list.insertFirst(56);
        list.insertFirst(37);
        list.insertLast(7);
        list.insertAfter(56, 567);
        list.insertAt(0, 100);
        list.insertAt(4, 340);
        list.insertAt(9, 989);

        list.insertBefore(37, 23);

        list.insertAfter(567, 101);
        list.insertBefore(12, 112);



        list.showList();

    }
}
