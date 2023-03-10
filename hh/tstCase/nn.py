vv={}
global x
def set_globle(x):
    # global x
    pass

if __name__ == '__main__':
    vv["toke"]=1
    z='{"username":"123","password":vv["toke"]}'
    print(eval(z))