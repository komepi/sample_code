import pickle

# オブジェクトのpickle化と非pickle化
print("---------------object------------------")
data_list = ["value1", 2, 3]
data_dir = {"key1":"value1", "key2":2, "key3":[1,2,3], "key4": data_list}

with open('pickled_dir_and_list.pkl', 'wb') as f:
    pickle.dump(data_list, f)
    pickle.dump(data_dir, f)

with open('pickled_dir_and_list.pkl', 'rb') as f:
    data_list2 = pickle.load(f)
    data_dir2 = pickle.load(f)

print("data_list2: {}".format(data_list2))
print("data_dir2: {}".format(data_dir2))


# クラス、メソッドのpickle化、非pickle化
print("---------------class and method---------------")
class Foo:
    vf = "this is class field"
    def __init__(self, v1):
        self.v1 = v1
    
    def equal_v1(self, v2):
        print("{v1} equal {v2}".format(v1=self.v1, v2=v2))
    
    @classmethod
    def print_vf(cls):
        print("vf: {vf}".format(vf=cls.vf))

def hello(to):
    print("hello to {to}".format(to=to))

with open('pickle_class_and_method.pkl', "wb") as f:
    pickle.dump(Foo, f)
    pickle.dump(hello, f)

with open('pickle_class_and_method.pkl', "rb") as f:
    Boo = pickle.load(f)
    greet = pickle.load(f)
boo = Boo("value1")
boo.equal_v1("value2")
Boo.print_vf()
greet("person")

## 非pickle環境にpickle化したクラスがない場合
del Foo
try:
    with open('pickle_class_and_method.pkl', "rb") as f:
        Boo = pickle.load(f)
        greet = pickle.load(f)
except AttributeError as e:
    print(e)
## 同じ名前の別のクラスが定義されている場合
class Foo:
    def __init__(self,v1):
        pass

with open("pickle_class_and_method.pkl", "rb") as f:
    Goo = pickle.load(f)
    sreet = pickle.load(f)
goo = Goo(1)
### Gooクラスは新しいFooクラスの構造をしてしまっている
try:
    goo.equal_v1(2)
except AttributeError as e:
    print(e)


# インスタンスのpickle化、非pickle化
print("-----------------instance------------------")
class Foo:
    vf = "this is class field"
    def __init__(self, v1):
        self.v1 = v1
    
    def equal_v1(self, v2):
        print("{v1} equal {v2}".format(v1=self.v1, v2=v2))
    
    @classmethod
    def print_vf(cls):
        print("vf: {vf}".format(vf=cls.vf))
foo = Foo("value1")

with open("pickled_instance.pkl", "wb") as f:
    pickle.dump(foo, f)
del foo
with open('pickled_instance.pkl', 'rb') as f:
    foo = pickle.load(f)

print("foo.v1: {v1}".format(v1=foo.v1))

##  クラスが定義されていないインスタンスを非pickle化するとAttributeErrorを吐く

del Foo, foo
try:
    with open('pickled_instance.pkl',"rb") as f:
        foo = pickle.load(f)
except AttributeError:
    print("AttributeError is occured.")

class Foo:
    def __init__(self, vx, v1):
        self.vx = vx
        self.v1 = v1
with open('pickled_instance.pkl', "rb") as f:
    foo = pickle.load(f)

print(foo.v1)
try:
    print(foo.vx)
except AttributeError as e:
    print(e)

try:
    foo.equal_v1(2)
except AttributeError as e:
    print(e)
# ファイルに出力しないpickle化、非pickle化
print("---------------dumps, loads-----------------")

data_list = ["value1", 2, 3]
data_dir = {"key1":"value1", "key2":2, "key3":[1,2,3], "key4": data_list}

pickled = pickle.dumps(data_dir)
print("pickled: {}".format(pickled))
data_unpickled = pickle.loads(pickled)
print("unpickled: {}".format(data_unpickled))


class Foo:
    attr = 'A class attribute'
    @classmethod
    def printh(cls):
        print("hello")

picklestring = pickle.dumps(Foo)
del Foo
pickle.loads(picklestring).printh()
print(pickle.loads(picklestring).attr)