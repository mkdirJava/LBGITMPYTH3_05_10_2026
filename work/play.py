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

