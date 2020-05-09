import datetime
import random
import time
import msvcrt

# Play a waiting game where you try to approximate the amount of time given
def wait(rang, duration):
    count = 0
    while count <= duration:
        rand = random.randint(rang[0], rang[1])
        print(f"Your goal is {rand} seconds.")
        time.sleep(0.5)
        print('Press the enter key to start and end.')
        while True:
            input1 = input("")
            now = datetime.datetime.now()
            break
        while True:
            input2 = input("")
            then = datetime.datetime.now()
            break
        diff = then-now
        seconds = diff.seconds
        microseconds = diff.microseconds
        time.sleep(0.5)
        print(f'You did {seconds} seconds and {microseconds} microseconds.')
        count = count + 1
        time.sleep(0.5)
        print(f'The goal was {rand} seconds.')
        time.sleep(1.5)
        if count == duration:
            print('Finished.')
            break
        else:
            print('Restarting in...')
            time.sleep(0.5)
            print('3')
            time.sleep(0.5)
            print('2')
            time.sleep(0.5)
            print('1')
            time.sleep(0.5)


min = input('What is the minimum time allowed?  ')
max = input('What is the maximum time allowed?  ')
num = input("How many times would you like to play?  ")
wait([min, max], num)
