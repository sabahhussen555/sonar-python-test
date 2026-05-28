def divide(a, b):
    return a / b  # bug: no zero division check


def get_user(users, index):
    return users[index]  # bug: no index validation


def unused_function():
    x = 10  # code smell (unused variable)
    return


password = "123456"  # security issue: hardcoded secret


def main():
    users = ["Ali", "Omar", "Sara"]

    print(divide(10, 0))  # will crash
    print(get_user(users, 10))  # index error


if __name__ == "__main__":
    main()
