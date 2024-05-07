def message(name):
    print(f"Glad to have you here, {name}!")

def greet():
    name = input("Hello! What is your name?\n")
    return name

def dictionary(d):
    print(d)

def dicKey():
    key = input("Input a key: >")
    return key

def dicValu(key):
    val = input(f"Input the value for {key}: >")
    return val

def proceed():
    print("Do you want to continue adding to the dictionary? y/n")
    ans = input("").lower()

    if ans == "y":
        return False
    else:
        return True

dic=dict()
nm=greet()
dic['name'] = nm
message(nm)

flag = False

while (flag != True):
    k = dicKey()
    v = dicValu(k)
    dic[k] = v

    flag = proceed()

dictionary(dic)
