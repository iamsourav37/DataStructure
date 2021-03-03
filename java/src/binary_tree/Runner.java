package binary_tree;

public class Runner {
    public static void main(String[] args) {
        BinaryTree t = new BinaryTree();
        t.insert(12);
        t.insert(72);
        t.insert(24);
        t.insert(6);
        t.insert(74);

//        12
//      6       72
//           24   74

        System.out.println("Leaf node : "+t.countLeaf());
        System.out.println("No of node : "+t.countNodes());

        System.out.println("Preorder : ");
        t.preorder();
        System.out.println("Postorder : ");
        t.postorder();
        System.out.println("Inorder : ");
        t.inorder();

        // searching
        System.out.println(t.search(12));

        if(!t.search(10))
            t.insert(10);
        t.insert(7);

//   after inserting 10 and 7
//         12
//     6       72
//       10   24   74
//     7


        System.out.println("Leaf node : "+t.countLeaf());
        System.out.println("No of node : "+t.countNodes());

        System.out.println("Preorder : ");
        t.preorder();
        System.out.println("Postorder : ");
        t.postorder();
        System.out.println("Inorder : ");
        t.inorder();
        System.out.println("Level order travarsal : ");
        t.levelorder();



    }
}
