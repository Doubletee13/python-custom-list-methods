from my_array import Array


container = Array([])

container.add_item(1)
container.add_item("mango")
container.add_item("guava")
container.insert_item(1,"kiwi")
print(container.remove_item("mango"))
print(container.pop_item(10))
print(container.clear_items())
#print(container)

