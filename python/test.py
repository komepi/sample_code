
def test():
    try:
        raise ValueError("test error")
    except ValueError as e:
        print(e)

    print(True)


try:
    test()
except ValueError:
    print("raise error")