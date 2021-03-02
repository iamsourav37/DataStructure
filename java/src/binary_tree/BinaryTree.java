package binary_tree;

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

}
