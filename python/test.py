class Test1:
    mode = "b"
    def get_mode(self):
        print("mode:{}".format(self.mode))
class Test1_1(Test1):
    mode = "c"
    def get_mode(self):
        print("mode:{}".format(self.mode))

class Test2(Test1_1):
    mode = "a"
    
    def get_mode(self):
        super(Test1_1,self).get_mode()

Test2().get_mode()