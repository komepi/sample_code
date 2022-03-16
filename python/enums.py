from enum import Enum

class Test(Enum):
    
    END = ("end","method_end")
    REV = ("rev","method_rev")
    
    def __init__(self, action, method):
        self._action = action
        self._method = method
    
    @property
    def action(self):
        return self._action
    
    @property
    def method(self):
        return self._method
    
    @classmethod
    def get_method_from_typelist(cls, type_list):
        for a in cls.__members__.values():
            if a.action in type_list:
                return a.method

if __name__ == "__main__":
    print(Test.END.method)
    print(Test.get_method_from_typelist(['Announce', 'rev']))