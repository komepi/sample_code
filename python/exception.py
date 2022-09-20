import sys
def main():
    try:
        # raise ValueError({"error_id":1})
        raise ValueError("test error")
    except Exception as ex:
        print(ex)
        print(ex.args)
        print(sys.exc_info()[0])
        print(type(sys.exc_info()))
    print("after error")


if __name__ == "__main__":
    main()
