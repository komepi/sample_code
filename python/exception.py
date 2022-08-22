
def main():
    try:
        raise Exception({"error_id":1})
    except Exception as ex:
        print(ex.args[0])
    print("after error")


if __name__ == "__main__":
    main()
