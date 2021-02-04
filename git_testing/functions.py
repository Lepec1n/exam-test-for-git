author = 'Kseniya'
world = 'World'

def world():
    print(f"Hello, {world}! This is {author}!", file=open('../result.txt',"w"))

