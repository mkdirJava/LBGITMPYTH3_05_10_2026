class Thing():
    def __init__(self,name:str,last_name: str,age:str):
        self.name =name 
        self.age =age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

test_json = {
    "name": "Tom",
    "age": 1
}

thing = Thing(last_name="here",**test_json)
print(thing)

play:list[int] =[1,2,3,4,5]

even = list(filter(lambda item: item % 2 == 0,play))
print(even)


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
    
        self._update_left(incoming_node=incoming_node.left)


    
    def _update_right(self, incoming_node: "Node"):
        if self.right is None:
            self.right = incoming_node
            return
    
        # insertion
        if self.right.value < incoming_node.value  and self.value < incoming_node.value :
            incoming_node = self.right
            self.right = incoming_node
            return 
    
        self._update_right(incoming_node=incoming_node.right)        
    
    def add_node(self,incoming_node: "Node"):
        if len(incoming_node.value) >= len(self.value):
            self._update_left(incoming_node)
        else:
            self.right = incoming_node
            self._update_right(incoming_node)


node1 = Node("home")
node2 = Node("1")

node1.add_node(node2)

print(node1)


    
