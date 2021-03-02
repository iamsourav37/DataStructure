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

}
