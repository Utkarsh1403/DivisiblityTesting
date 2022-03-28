def divby5(a):
    if a %5 ==0:
        return True
    else:
        return  False


def divby7(a):
    if a % 7 == 0:
        return True
    else:
        return False

def divby9(a):
    if a % 9 == 0:
        return True
    else:
        return False

def divby11(a):
    if a % 11 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("Enter the number: "))
    n1 = divby5(a)
    n2 = divby7(a)
    n3 = divby9(a)
    n4 = divby11(a)
    print(n1)
    print(n2)
    print(n3)
    print(n4)










