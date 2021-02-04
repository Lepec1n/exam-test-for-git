author = 'Kseniya'
world = 'World'

def world1():
    print(f"Hello, {world}! This is {author}!", file=open('../result.txt',"w"))

def world2():
    print(f"Hello, World! This is {author}!", file=open('../result.txt',"w"))
