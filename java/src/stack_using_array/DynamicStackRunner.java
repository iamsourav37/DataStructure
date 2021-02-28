package stack_using_array;

public class DynamicStackRunner {
    public static void main(String[] args) {
        DynamicStack ds = new DynamicStack();

        ds.push(12);
        System.out.println("Size of the Stack : "+ds.getSize());
        System.out.println("Capacity : "+ds.getCapacity());
        ds.push(21);
        System.out.println("Size of the Stack : "+ds.getSize());
        System.out.println("Capacity : "+ds.getCapacity());
        ds.push(37);
        System.out.println("Size of the Stack : "+ds.getSize());
        System.out.println("Capacity : "+ds.getCapacity());
        ds.push(345);
        ds.push(34);
        ds.push(98);
        System.out.println("Size of the Stack : "+ds.getSize());
        System.out.println("Capacity : "+ds.getCapacity());

        ds.display();
        System.out.println("Pop operation :");

        ds.pop();
        ds.pop();
        ds.pop();
        ds.pop();
        System.out.println("Size of the Stack : "+ds.getSize());
        System.out.println("Capacity : "+ds.getCapacity());
        ds.display();

    }
}
