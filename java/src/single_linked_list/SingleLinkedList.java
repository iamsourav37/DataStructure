package single_linked_list;

interface InsertMethods{
    void insertFirst(int data);
    void insertLast(int data);
    void insertAt(int index, int data);
    void insertAfter(int key, int data);
    void insertBefore(int key, int data);
}
interface DeleteMethods{
    void removeFirst();
    void removeLast();
    void removeAt(int index);
    void remove(int data);
}

abstract public class SingleLinkedList implements InsertMethods,DeleteMethods {
    private Node head;

    SingleLinkedList(){ // default constructor
        this.head = null;
    }

    public void insertFirst(int data){
        this.head = new Node(data, this.head);
    }

    public void insertLast(int data){
        Node tmp = this.head;

        while (tmp.getNext() != null)
            tmp = tmp.getNext();

        Node newNode = new Node(data, null);
        tmp.setNext(newNode);
    }



    public void showList(){
        if (this.head == null){
            System.out.println("List is empty");
            return;
        }

        Node tmp = this.head;
        System.out.println("List items are : ");
        String listData = "";
        while (tmp != null){
            listData = listData.concat(String.valueOf(tmp.getData()) + "-->");
            tmp = tmp.getNext();
        }
        System.out.println(listData+"null");
    }


}
