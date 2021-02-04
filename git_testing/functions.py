author = 'Kseniya'
world = 'World'

def world1():
    print(f"Hello, {world}! This is {author}!", file=open('../result.txt',"w"))

def world2():
    print(f"Hello, World! This is {author}!", file=open('../result.txt',"w"))

def func1():
    var1 = 5
    var2 = 6
    var1 = var1 + 2
    var2 = var2 + 2
    print(var1+var2)

