package binary_tree;

public class BinaryTree {
    TreeNode root;

    public BinaryTree(){
        root = null;
    }

    public void insert(int data){
        TreeNode node = new TreeNode(data);

        if(root == null){
            root = node;
        }else{
            TreeNode current = root, parent;

            while(true){
                parent = current;
                if(data<current.getData()){
                    current = current.getLeft();
                    if(current == null){
                        parent = node;
                        return;
                    }
                }else{
                    current = current.getRight();
                    if(current == null){
                        parent = node;
                        return;
                    }
                }
            }
        }
    }

}
