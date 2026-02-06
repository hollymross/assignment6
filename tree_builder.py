class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        #Empty Tree
        if self.root is None:
            print("Tree is empty, cant insert without root")
        #Start from root
        if current_node is None:
            current_node = self.root
        #Found the manager node
        if current_node.value == manager_name:
            if side == "left" and current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                return True
            else:
                print(f"{manager_name} already has a {side} subordinate")
                return True
            
        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(manager_name, employee_name, side, current_node.left)

        if current_node.right and not found_left:
            found_right = self.insert(manager_name, employee_name, side, current_node.right)

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return
            
        indent = "    " * level
        print(f"{indent}-{node.value}")

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)
# Test your code here

company_directory = TeamTree()
company_directory.root = EmployeeNode("Jordan")
company_directory.insert("Jordan", "Taylor", "right")
company_directory.insert("Jordan", "Riley", "left")
company_directory.insert("Riley", "Dana", "right")
company_directory.insert("Riley", "Morgan", "left")
company_directory.print_tree()





# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")