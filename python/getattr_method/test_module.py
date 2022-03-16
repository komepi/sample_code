import sys

def select_method(method_name):
    method = getattr(sys.modules[__name__],"print_"+method_name)
    method()
    
def print_name():
    print("called print_name")
    
def print_age():
    print("called print_age")