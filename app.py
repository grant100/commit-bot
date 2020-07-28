import time, subprocess
while True:
    with open('/home/pi/code/commit-bot/.commit-bot.txt','a') as file:
        file.write(' ' * 5)
        file.close()
    time.sleep(5)

    subprocess.run(['git','add','.'])
    subprocess.run(['git', 'commit', '-m', 'commit-bot'])
    subprocess.run(['git', 'push'])
