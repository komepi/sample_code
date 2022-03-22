# https://qiita.com/y518gaku/items/07961c61f5efef13cccc


class TestSpecialMethod():
    def __init__(self, value, boo, leng):
        self.value = value
        self.boo = boo
        self.str = "テスト"
        self.leng = leng
        self.dicts = {"key1":"value1","key2":"value2","key3":"value3"}

    def __add__(self, other):
        # +演算子使用時
        return self.value + other.value
    
    def __sub__(self, other):
        # -演算子使用時
        return self.value - other.value
    
    def __mul__(self, other):
        # *演算子使用時
        return self.value * other.value
    
    def __truediv__(self, other):
        # /演算子使用時
        return self.value / other.value
    
    def __floordiv__(self, other):
        # //演算子使用時
        return self.value // other.value
    
    def __and__(self, other):
        # &演算子使用時
        return self.boo & other.boo


    def __or__(self, other):
        # |演算子使用時
        return self.boo | other.boo

    def __eq__(self,other):
        # ==演算子使用時
        return self.value == other.value

    def __ne__(self,other):
        # !=演算子使用時
        return self.value != other.value

    def __lt__(self,other):
        # <演算子使用時
        return self.value < other.value

    def __gt__(self,other):
        # >演算子使用時
        return self.value > other.value
    
    
    def __int__(self):
        # int()関数使用時
        return int(self.value)
    
    def __float__(self):
        # float()関数使用時
        return float(self.value)
    
    def __str__(self):
        # str()関数使用時
        return str(self.value)
    
    def __repr__(self):
        # repr()関数使用時
        return repr(self.value)
    
    def __bytes__(self):
        # bytes()関数使用時
        return bytes(self.value)
    
    def __format__(self, from_spec):
        # format()関数使用時
        return self.str
    
    def __len__(self):
        # len()関数使用時
        return self.leng
    
    def __getitem__(self, key):
        # 辞書型、list型のようにobject[xx]で取得する時
        if key=="no_key":
            raise Exception("no exist key.")
        return self.dicts[key]
    
    def __setitem__(self, key, value):
        # 辞書型に追加するようにobject[xx]=value
        self.dicts[key] = value
    
    def __delitem__(self, key):
        # del 文が使用されたとき
        print("{}の要素を削除".format(key))

    def __contains__(self, param):
        # 比較演算子in使用時
        return True if param in self.dicts.keys() else False

if __name__ == "__main__":
    t1 = TestSpecialMethod(10,True,2)
    t2 = TestSpecialMethod(20,False,3)
    
    print("t1+t2 = ", t1+t2)
    print("t1-t2 = ", t1-t2)
    print("t1*t2 = ", t1*t2)
    print("t1/t2 = ", t1/t2)
    print("t1//t2 = ", t1//t2)
    
    print("t1&t2 = ", t1&t2)
    print("t1|t2 = ", t1|t2)
    
    print("t1==t2 = ", t1==t2)
    print("t1!=t2 = ", t1!=t2)
    print("t1<t2 = ", t1<t2)
    print("t1>t2 = ", t1>t2)
    
    print("int(t1) = ", int(t1))
    print("float(t1) = ", float(t1))
    print("str(t1) = ", str(t1))
    print("print(t1): ",t1)
    print("\"{}\".format(t1,0) = ","{}".format(t1,0))
    repr(t1)
    
    print("len(t1) = ", len(t1))
    print("t1[\"key1\"] = ", t1["key1"])
    try:
        print("t1[\"no_key\"] = ", t1["no_key"])
    except Exception as e:
        print("t1[\"no_key\"] = ", e)
    print("t1.dicts = ", t1.dicts)
    t1["key4"] = "value4"
    print("t1.dicts = ", t1.dicts)
    
    del t1["key4"]
    
    print("\"key1\" in t1: ", "key1" in t1)
    print("\"keyx\" in t1: ", "keyx" in t1)