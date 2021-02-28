package single_linked_list;

interface InsertMethods{
    void insertFirst(int data);
    void insertLast(int data);
    void insertAt(int index, int data) throws Exception;
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
    public void insertAt(int index, int data) throws Exception {
        if(index<0 || index>this.getLength()){
            throw new Exception("Out of range index");
        }
        else if(index == 0){
            this.insertFirst(data);
            return;
        }else if(index == this.getLength()){
            this.insertLast(data);
            return;
        }
        int count = 0;
        Node tmp_forward= this.head;
        Node tmp_before = this.head;

        while(tmp_forward != null){
            if(count == index){
                // insert the element
                Node newNode = new Node(data, tmp_forward);
                tmp_before.setNext(newNode);
                return;
            }

            count++;
            tmp_before = tmp_forward;
            tmp_forward = tmp_forward.getNext();
        }
    }


    public int getLength(){
        Node node = this.head;
        int count = 0;
        while(node != null){
            count ++;
            node = node.getNext();
        }
        return count;
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
