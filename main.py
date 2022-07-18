import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("'\r{0}".format(timer), end='')
        time.sleep(1)
        t -= 1

    print('\nTimer Completed!')


t = input('Enter the time in seconds: ')

countdown(int(t))
