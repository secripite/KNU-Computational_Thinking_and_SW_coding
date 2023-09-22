class el():
    def turnOn():
        print('on')

    def turnOff():
        print('off')

class TV(el):
    _num = 1
    def __init__(self):
        self.num = TV._num
        self.channel = TV._num
        self.volume = TV._num
        TV._num+=1

    def setChannel(self, x):
        self.channel = x

    def setVolume(self, y):
        self.volume = y

ss_num = int(input())
lg_num = int(input())

ss_arr = []
lg_arr = []

for i in range(0,ss_num+1):
    globals()["SS{}".format(i)] = TV()

TV._num = 1

for i in range(0,lg_num+1):
    globals()["LG{}".format(i)] = TV()

for i in globals():
    if i.find('SS') != -1:
        ss_arr.append(i)
    elif i.find('LG') != -1:
        lg_arr.append(i)

while True:
    cmd = input()
    if cmd.find("END") != -1:
        break
    cmd = list(cmd.split())
    
    if cmd[0] == 'SS':
        if cmd[2] == 'volume':
            eval(ss_arr[int(cmd[1])-1]).setVolume(int(cmd[3]))
        elif cmd[2] == 'channel':
            eval(ss_arr[int(cmd[1])-1]).setChannel(int(cmd[3]))

    elif cmd[0] == 'LG':
        if cmd[2] == 'volume':
            eval(lg_arr[int(cmd[1])-1]).setVolume(int(cmd[3]))
        elif cmd[2] == 'channel':
            eval(lg_arr[int(cmd[1])-1]).setChannel(int(cmd[3]))

    elif cmd[0] == 'PP':
        if cmd[1] == 'SS':
            if cmd[3] == 'volume':
                print(eval(ss_arr[int(cmd[2])-1]).volume)
            elif cmd[3] == 'channel':
                print(eval(ss_arr[int(cmd[2])-1]).channel)
                
        elif cmd[1] == 'LG':
            if cmd[3] == 'volume':
                print(eval(lg_arr[int(cmd[2])-1]).volume)
            elif cmd[3] == 'channel':
                print(eval(lg_arr[int(cmd[2])-1]).channel)