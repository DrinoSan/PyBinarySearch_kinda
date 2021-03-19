import random
import time




# The following is the definition of Binary Search Tree(BST) according to Wikipedia ( https://en.wikipedia.org/wiki/Binary_search_tree )
# Binary Search Tree is a node-based binary tree data structure which has the following properties:  

# The left subtree of a node contains only nodes with keys lesser than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree. 
# There must be no duplicate nodes.

class Node:
    """
    A class to represent a Node.
    It was a first try to implement a binary search with some extras

    Attributes
    ----------

    element: int --> this is sometimes called key
    left: Node --> is again a Node but on the left hand side
    right: Node --> is again a Node but on the right hand side
    """
    def __init__(self, element = None, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right


    def find_element_with_number(self, obj, num):
        """
        Basic implementation of a binary search.

        Parameters:
        ----------
        obj: Node --> is the start node (root_node)
        num: int --> the value we are searching for
        """
        #If the next node is None then wie have not found the element and our whole life makes no sense anymore ;)
        if obj == None:
            print("NOT FOUND")
            return False

        if obj.element == num:
            print("FOUND IT")
            return True
        elif obj.element > num:
            obj.find_element_with_number(obj.left, num)
        else:
            obj.find_element_with_number(obj.right, num)



    def find_element_with_node(self, obj):
        """
        This function was created before the ( find_element_with_number  ) and it was just to test if the logic was right.
        This Functions will not be used!
        So dont look at it
        """
        #If the next node is None then we have not found the element and our whole life makes no sense anymore ;)
        if obj == None:
            print("NOT FOUND")
            return False

        if self.element == obj.element:
            print("FOUND IT")
            return True
        elif self.element > obj.element:
            self.find_element_with_node(obj.left)
        else:
            self.find_element_with_node(obj.right)




    def insertNode(self, node):
        """
        A quick way to insert a node.
        1.) Comparing the Parent node value(parent.element) with the new node value(node.element)
        2.) If the parent node value is higher then we go to the left child.node || If it is lower it goes to the right child.node
        IMPORTANT:
        - A new node is always inserted at the leaf
        - We start from the root node and search untill we find a leaf.  Once a leaf node is found, the new node is added as a child of the leaf node.
        """
        if self == None:
            self = node
        # print(self.element)
        # print(node.element)
        if self.element > node.element:
            # print("Links")
            if self.left == None:
                self.left = node
            self.left.insertNode(node)
        elif self.element < node.element:
            if self.right == None:
                self.right = node
            # print("Rechts")
            self.right.insertNode(node)
        return True


    @staticmethod
    def pre_order(node):
        """
        Preorder (Root, Left, Right)
        Breadth first and Postorder will also follow in future
        """
        print(node.element)
        if node.left:
            Node.pre_order(node.left)
        if node.right:
            Node.pre_order(node.right)


    # def pre_order(self, start):
    #     print(start.element)
    #     if start.left:
    #         self.pre_order(start.left)
    #     if start.right:
    #         self.pre_order(start.right)


    @staticmethod
    def depth(node):
        """
        - Get the max depth of left subtree recursively
        - Get the max depth of right subtree recursively
        - Get the max of max depths of left and right subtrees and add 1 to it for the current node.
          max_depth = max(max dept of left subtree,  max depth of right subtree) + 1
        - Return max_depth
        """
        if node == None:
            return False
        left_node_depth = Node.depth(node.left)
        right_node_depth = Node.depth(node.right)
        # print("left: ", left_node_depth)
        # print("right: ",right_node_depth)
        if left_node_depth > right_node_depth:
            return left_node_depth + 1
        else:
            return right_node_depth + 1



    """
    Artefacts
    """
    def __str__(self):
        return str(self.element)

    def __lt__(self, element):
        return self.element < element
    def __gt__(self, element):
        return self.element > element




#MAGIC.... tbh took it from stack overflow could not be botherd to write that too
#But it was quite nice and easy to understand
COUNT = [10]  
# Function to print binary tree in 2D  
# It does reverse inorder traversal  
def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.element)  
    # time.sleep(2)
  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  

##### MAGIC ENDS


if __name__ == "__main__":
    # rootNode = Node(50)
    # rootNode.insertNode(Node(10000))
    # rootNode.insertNode(Node(10))
    # rootNode.insertNode(Node(15))
    # l = random.sample(range(1, 100), 10)
    # for i in l:
    #     rootNode.insertNode(Node(i))
    # rootNode.insertNode(Node(60))
    # rootNode.insertNode(Node(20))
    # print(Node.depth(rootNode))
    # print2D(rootNode)
    # rootNode.pre_order(rootNode)
    # Node.pre_order(rootNode)
    # rootNode.insertNode(Node(10))
    # rootNode.insertNode(Node(60))
    # rootNode.insertNode(Node(15))

    # Node.depth(rootNode)
    # # print("The root node always starts with 50")
    # # print("The additional nodes are bellow:")
    # # print(l)
    # # print("-"*40)
    # print2D(rootNode)
    




    ###################
    while True:
        """
        Getting values for the root_node and how many nodes should be in the graph
        The range of the values in the graph are range(1,100)
        """
        root_Node_value = input("Please enter the Value of the root node: ")
        rootNode = Node(int(root_Node_value))
        n_nodes = input("Please enter the number of Nodes you want to have in the graph: ")
        l = random.sample(range(1, 100), int(n_nodes))
        for i in l:
            rootNode.insertNode(Node(i))
        print("Now we need some super heavy calculation for the graph! :D")
        for i in range(1,4):
            print("Calculating" + "."*i)
            time.sleep(0.5)
        print("Your graph looks like this: ")



        """
        Asking for a number to use the binarySearch algo
        Asking to draw graph again
        """
        print2D(rootNode)
        print("###########################")
        print("## MAX DEPTH OF TREE = " + str(Node.depth(rootNode)) + " ##")
        print("###########################")
        print("-"*40)
        print("-"*40)
        while True:
            # print("If you want to check if node is in the tree please input your number you are searching for: ")
            # print("-"*40)
            # print("If you want to draw the graph again type g (q for quit): ")
            print("Type n to search a number: ")
            print("Type g to draw again: ")
            # print("Hit Enter to Continue: ")
            print("If you want to change the values of the Root Node and the amount of nodes type c: (Otherwise enter): ")
            print("Type q to QUIT: ")
            n = input(">>>")
            print("-"*40)
            if n == "q":
                exit()
            if n == "g":
                print2D(rootNode)
            if n == "n":
                print("-"*40)
                print("Please enter the Number you want to search for :D")
                n = input(">>>")
                print("")
                print("-"*40)
                print("-"*40)
                print("-"*40)
                rootNode.find_element_with_number(rootNode, int(n))
            if n == "c":
                break
            print("-"*40)
            print("-"*40)
            print("-"*40)
            print("")
    ###################

    # random_numbers = [random.randint(0, 100) for x in range(30)]
    # print(random_numbers)
