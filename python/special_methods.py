# https://qiita.com/y518gaku/items/07961c61f5efef13cccc


class TestSpecialMethod():
    def __init__(self, value, boo):
        self.value = value
        self.boo = boo
        self.str = "テスト"
        
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        return self.value / other.value
    
    def __floordiv__(self, other):
        return self.value // other.value
    
    def __and__(self, other):
        return self.boo & other.boo


    def __or__(self, other):
        return self.boo | other.boo


    def __eq__(self,other):
        return self.value == other.value

    def __ne__(self,other):
        return self.value != other.value

    def __lt__(self,other):
        return self.value < other.value

    def __gt__(self,other):
        return self.value > other.value
    
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return repr(self.value)
    
    def __bytes__(self):
        return bytes(self.value)
    
    def __format__(self, from_spec):
        return self.str
    
        


if __name__ == "__main__":
    t1 = TestSpecialMethod(10,True)
    t2 = TestSpecialMethod(20,False)
    
    print(t1+t2)
    print(t1-t2)
    print(t1*t2)
    print(t1/t2)
    print(t1//t2)
    
    print(t1&t2)
    print(t1|t2)
    
    print(t1==t2)
    print(t1!=t2)
    print(t1<t2)
    print(t1>t2)
    
    print(int(t1))
    print(float(t1))
    print(str(t1))
    print(t1)
    print("{}".format(t1,0))
    repr(t1)