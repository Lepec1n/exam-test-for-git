author = 'Kseniya'
world = 'World'

def world1():
    print(f"Hello, {world}! This is {author}!", file=open('../result.txt',"w"))

def world2():
    print(f"Hello, World! This is {author}!", file=open('../result.txt',"w"))

def func1():
    var1 = 5
    var2 = 6
    print(inc_and_sum(var1,var2, 2))

def func2():
    var1 = 3
    var2 = 4
    print(inc_and_sum(var1,var2, 2))

def inc_and_sum(var1, var2, inc):
    var1 = var1 + inc
    var2 = var2 + inc
    return var1 + var2
