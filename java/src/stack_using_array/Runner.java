package stack_using_array;

public class Runner {
    public static void main(String[] args) {
        Stack s = new Stack(4);

        s.push(12);
        s.push(21);
        s.push(34);

        s.push(90);
        s.push(211);
        s.push(98);

        s.display();
        System.out.println("Size of the stack now is : "+s.getSize());

        // pop
        System.out.println("Pop elements : ");
        System.out.println(s.pop());
        System.out.println(s.pop());
        System.out.println("Size of the stack now is : "+s.getSize());
        System.out.println(s.pop());
        System.out.println(s.pop());
        System.out.println(s.pop());
        System.out.println(s.pop());
    }
}
