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

public class SingleLinkedList implements InsertMethods {
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
    public void insertAt(int index, int data){
        if(index<0 || index>this.getLength()){
            System.out.println("Out of range index");
            return;
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

    public void insertAfter(int key, int data){

        // first find out the index of the key
        // if found then call insertAt method with index+1
        // if not found then show key not found message
        int index = 0;
        Node tmp = this.head;
        while(tmp != null){
            if(tmp.getData() == key){
                this.insertAt(index+1, data);
                return;
            }
            index++;
            tmp = tmp.getNext();
        }
        System.out.println(key+" is not found in the list");
    }

    public void insertBefore(int key, int data){

        // first find out the index of the key
        // if found then call insertAt method with index
        // if not found then show key not found message
        int index = 0;
        Node tmp = this.head;
        while(tmp != null){
            if(tmp.getData() == key){
                this.insertAt(index, data);
                return;
            }
            index++;
            tmp = tmp.getNext();
        }
        System.out.println(key+" is not found in the list");
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
