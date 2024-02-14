class SquareEquation: #ax^2+bx+c=0
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        if (b*b-4*a*c < 0):
            raise (Exception("D<0!"))
    @property    
    def D(self):
        return self.b*self.b-4*self.a*self.c
    @property
    def x1(self):
        return (-self.b+self.D**.5)/(2*self.a)
    @property
    def x2(self):
        return (-self.b-self.D**.5)/(2*self.a)

if __name__=="__main__":
    se = SquareEquation(1,4,1)
    print(se.D)
    print(se.x1)
    print(se.x2)