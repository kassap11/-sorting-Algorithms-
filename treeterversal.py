class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
      
def inorder(node):
    if node!=None:
        inorder(node.left)
        print(node.data,end=" ")
        inorder(node.right)
        
def postorder(node):
    if node!=None:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end=" ")
        
def preorder(node):
    if node!=None:
        print(node.data,end=" ")
        preorder(node.left)
        preorder(node.right)
        
            
                        
if __name__ == "__main__":
    # Create a sample tree
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    
    print("Inorder Traversal:")
    inorder(root)
    print("\nPreorder Traversal:")
    preorder(root)
    print("\nPostorder Traversal:")
    postorder(root)
        
        
