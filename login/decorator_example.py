
global data

def foil(func):
    def infoil(x):
        
        
        print("before execution",x)
        x=10
        res=func(x)
    
        print("after execution",x)
        return res
    return infoil

@foil
def hello(x):
    print("I am hello() ",x)



hello(5)