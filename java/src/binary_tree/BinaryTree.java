package binary_tree;
import java.util.LinkedList;
import java.util.Queue;

public class BinaryTree {
    TreeNode root;

    public BinaryTree(){
        root = null;
    }

    public void insert(int data){
        this.root = this.insert(data, root);
    }

    private TreeNode insert(int data, TreeNode node){ // using recursion
        if(node == null)
            node = new TreeNode(data);
        else{
            if(data<=node.getData()){
                node.setLeft(insert(data, node.getLeft()));
            }else{
                node.setRight(insert(data, node.getRight()));
            }
        }
        return node;
    }

    public int countNodes(){
        return this.countNodes(this.root);
    }
    private int countNodes(TreeNode node){
        if(node==null)
            return 0;
        else{
            int count = 1;
            count += countNodes(node.getLeft());
            count += countNodes(node.getRight());
            return count;
        }
    }
    public int countLeaf(){
        return countLeaf(this.root);
    }
    private int countLeaf(TreeNode node){
        if (node == null)
            return 0;
        if (node.getLeft() == null && node.getRight() == null)
            return 1;
        else
            return countLeaf(node.getLeft()) + countLeaf(node.getRight());
    }

    public boolean search(int value){
        return this.search(root, value);
    }
    private boolean search(TreeNode node, int value){
        if(node == null)
            return false;
        if(node.getData() == value)
            return true;

        // search in left subtree
        boolean leftFlag = search(node.getLeft(), value);

        // if flag is true then key is matching , return flag
        if(leftFlag)
            return true;

        // if not matching then search in right subtree
        boolean rightFlag = search(node.getRight(), value);

        return rightFlag;
    }
    public void preorder(){
        preorder(root);
        System.out.println();

    }
    private void preorder(TreeNode node){
        if(node != null){
            System.out.print(node.getData()+" ");
            preorder(node.getLeft());
            preorder(node.getRight());
        }
    }
    public void postorder(){
        postorder(root);
        System.out.println();
    }
    private void postorder(TreeNode node){
        if(node != null){
            postorder(node.getLeft());
            postorder(node.getRight());
            System.out.print(node.getData()+" ");
        }

    }
    public void inorder(){
        inorder(root);
        System.out.println();

    }
    private void inorder(TreeNode node){
        if(node != null){
            inorder(node.getLeft());
            System.out.print(node.getData()+" ");
            inorder(node.getRight());
        }
    }

    public void levelorder(){
        this.levelorder(this.root);
    }
    private void levelorder(TreeNode node){
        if(node == null)
            return;
        Queue<TreeNode> queue = new LinkedList<>();
        TreeNode temp ;

        queue.add(node);
        while(!queue.isEmpty()){
            temp = queue.poll();
            System.out.print(temp.getData()+" ");
            if(temp.getLeft() != null)
                queue.add(temp.getLeft());
            if(temp.getRight() != null)
                queue.add(temp.getRight());
        }
    }

}
