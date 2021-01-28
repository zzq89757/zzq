import random
import string
import time
level = int(input('please choose the level you want to play(1-5):'))
times = int(input('please choose the times that you wanna play:'))
if level not in range(1, 6):
    print('you must be kidding me')
else:
    for i in range(1, times+1):
        length = random.randint(2*level-1, 2*level+1)
        word = ''.join(random.sample(string.ascii_lowercase, length))
        print(word)
        while 1:
            start = time.time()
            ipt = input('well,you have to input |--%s--|:' % word)
            if ipt == word:
                break
    print('------Game Over,Well Done!!!------')
    end = time.time()
    print('you done level %d %d times spend %.2f s' % (level, times, (end-start)))
