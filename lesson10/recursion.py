

def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)

def one_of_nine(num):
    total = 0

    if (num > 9):
        total = num - 1
    
    if (num < 9):
        total = num + 1

    if (num == 9):
        return num
    
    print(total)

    return one_of_nine(total)

mynewtotal = one_of_nine(0)
print(mynewtotal)

mynewtotal = one_of_nine(23)
print(mynewtotal)

    
    
