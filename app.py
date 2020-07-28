import time, subprocess, random
while True:
    with open('/home/pi/code/commit-bot/.commit-bot.txt','a') as file:
        file.write('0' * random.randint(0,100))
        file.close()
    #time.sleep(3600 * 12)

    subprocess.run(['git','add','.'])
    subprocess.run(['git', 'commit', '-m', 'commit-bot'])
    subprocess.run(['git', 'push'])
    time.sleep(3600*12)
