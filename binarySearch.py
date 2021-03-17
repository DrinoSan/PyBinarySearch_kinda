import random

class Node:
    def __init__(self, element = None, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

    def find_element_with_number(self, obj, num):
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
        #If the next node is None then wie have not found the element and our whole life makes no sense anymore ;)
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


    def pre_order(self, start):
        print(start.element)
        if start.left:
            self.pre_order(start.left)
        if start.right:
            self.pre_order(start.right)



    def __str__(self):
        return str(self.element)

    def __lt__(self, element):
        return self.element < element
    def __gt__(self, element):
        return self.element > element




#MAGIC.... tbh took it from stack overflow could not be botherd to write that too
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
  
    # Process left child  
    print2DUtil(root.left, space)  
  
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)  

##### MAGIC ENDS


if __name__ == "__main__":
    rootNode = Node(50)
    l = random.sample(range(1, 100), 10)
    for i in l:
        rootNode.insertNode(Node(i))

    print("The root node always starts with 50")
    print("The additional nodes are bellow:")
    print(l)
    print("-"*40)
    print2D(rootNode)
    while True:
        print("-"*40)
        print("If you want to check if node is in the tree please input your number you are searching for:")
        print("If you want to leave type q")
        print("If you want to draw the graph again type g")
        n = input("NUMBER: ")
        print("-"*40)
        if n == "q":
            break
        if n == "g":
            print2D(rootNode)
        else:
            print("-"*40)
            rootNode.find_element_with_number(rootNode, int(n))
            print("-"*40)
    # random_numbers = [random.randint(0, 100) for x in range(30)]
    # print(random_numbers)
