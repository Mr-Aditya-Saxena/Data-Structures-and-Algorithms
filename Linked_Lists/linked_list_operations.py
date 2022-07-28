#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# [SCRIPT DESCRIPTION]
# Simple Python Linked List Operations
# @author   : Aditya Saxena
# @version  : 1.0
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# [STEP 1] - Creating the classes to create a linked list
# [Class Definition] Defining the Node class
class Node:
	# Function to initialize the node object
	def __init__(self, data):
		self.data = data    # Assign data
		self.next = None    # Initialize next as null

# [Class Definition] Linked List class
class LinkedList:
	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints contents of linked list starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next

# [STEP 2] - Creating a linked list using the above classes
# [Inline Test Statement] print('Name of the current module is : '+__name__)
if __name__=='__main__':
    # creating a blank linked list
    transaction_list = LinkedList()

    # creating some nodes
    element_1 = Node(1)
    element_2 = Node(2)
    element_3 = Node(3)
    element_4 = Node(4)
    element_5 = Node(5)

    # setting one of the nodes at the head of the linked list
    transaction_list.head = element_1

    # linking the nodes together
    element_1.next = element_2
    element_2.next = element_3
    element_3.next = element_4
    element_4.next = element_5

# [STEP 3] - Printing the list to see its components
    transaction_list.printList()