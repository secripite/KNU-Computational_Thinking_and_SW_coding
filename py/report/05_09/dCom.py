class t1():
    def t1f(self):
        print('t1f')
class t2(t1):
    def t2f(self):
        print('t2f')
        
p1 = t1()
p1.t1f()

c1 = t2()
c1.t2f()
c1.t1f()