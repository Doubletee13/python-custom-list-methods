from typing import Any, List


class Array:
    def __init__(self,array:List[Any]):
        self.array:List[Any] = array

    def add_item(self,item: Any) -> None:
        if not isinstance(self.array,list):
            print(f"{type(self.array)} has no method add_item")
        else:
            self.array = self.array + [item]

    def insert_item(self,index,item:Any) -> None:
        if not isinstance(self.array,list):
            print(f"{type(self.array)} has no method insert_item")
        else:
            self.array = self.array[:index] + [item] + self.array[index:]

    def pop_item(self, index:int = -1) -> Any:
        if not isinstance(self.array,list):
            return f"{type(self.array)} has no method pop_item"
        if len(self.array) != 0:
            if index >= len(self.array) or index < -len(self.array):
                return "IndexError: list index out of range"
            elif index == -1:
                item = self.array[index]
                self.array = self.array[:index]
                return item
            else:
                item = self.array[index]
                self.array = self.array[:index] + self.array[index+1:]
                return item
        else:
            return "IndexError: pop out of empty list"

    def remove_item(self,item:Any) -> Any:
        if not isinstance(self.array,list):
            return f"{type(self.array)} has no method remove_item"

        for index in range(len(self.array)):
            if item == self.array[index]:
                self.array = self.array[:index] + self.array[index+1:]
                return item
        return "ValueError: item not in list"
    def clear_items(self) -> list:
        if not isinstance(self.array,list):
            return f"{type(self.array)} has no method clear_items"
        self.array = []
        return self.array

    def __repr__(self) -> str:
        return repr(self.array)




