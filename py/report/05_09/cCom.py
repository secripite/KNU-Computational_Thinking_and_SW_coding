class car ():
    num = 0

    def __init__(self, _cc, _tire=4, _man=4):
        self.cc = _cc
        self.tire = _tire
        self.man = _man
        car.num +=1
        self.id = car.num

    def run(self):
        print('run')
    
    def stop(self):
        print('stop')

    def __del__(self):
        print('del')

c1 = car(3000)
print(c1.id)
c2 = car(4000,4,6)
print(c2.id)
c3 = car(2000)
print(c3.id)

print(c1.tire)
print(c1.cc)
c1.run()
c1.stop()

del c1