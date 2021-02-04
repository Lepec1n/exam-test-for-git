author = 'Kseniya'
world = 'World'

def world1():
    print(f"Hello, {world}! This is {author}!", file=open('../result.txt',"w"))

def world2():
    print(f"Hello, World! This is {author}!", file=open('../result.txt',"w"))

def func1():
    var1 = 5
    var2 = 6
    var1 = var1 + 1
    var2 = var2 + 1
    print(inc_and_sum(var1,var2))

def func2():
    var1 = 3
    var2 = 4
    var1 = var1 + 1
    var2 = var2 + 1
    print(inc_and_sum(var1,var2))

def inc_and_sum(var1, var2):
    var1 = var1 + 1
    var2 = var2 + 1
    return var1 + var2
