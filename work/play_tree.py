
class Node[str]():
    def __init__(self, value:str):
        self.left = None
        self.right = None
        self.value =value
    
    def _update_left(self, incoming_node: "Node"):
        if self.left is None:
            self.left = incoming_node
            return
    
        # insertion
        if self.left.value < incoming_node.value  and self.value < incoming_node.value :
            incoming_node = self.left
            self.left = incoming_node
            return 
        self.left._update_left(incoming_node=incoming_node)
        
    
    def _update_right(self, incoming_node: "Node"):
        if self.right is None:
            self.right = incoming_node
            return
    
        # insertion
        if self.right.value > incoming_node.value  and self.value > incoming_node.value :
            incoming_node = self.right
            self.right = incoming_node
            return 
    
        self.right._update_right(incoming_node=incoming_node)
    
    def add_node(self,incoming_node: "Node"):
        if len(incoming_node.value) <= len(self.value):
            self._update_left(incoming_node)
        else:
            self._update_right(incoming_node)


node1 = Node("home")
node2 = Node("1")
node3 = Node("12121")
node4 = Node("12121123")

node1.add_node(node2)
node1.add_node(node3)
node1.add_node(node4)

# print(node1.left.value)
print(node1.right.right.value)


    
