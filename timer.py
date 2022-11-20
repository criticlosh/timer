import time
seconds = input('enter time in seconds')
def timer(seconds):
    while seconds > 0:
        min = seconds/60
        sec = seconds%60
        timer = f"{min}:{sec}"
        print(timer)
        seconds -= 1
    print('time up')

timer(int(seconds))