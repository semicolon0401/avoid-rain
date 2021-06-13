import os, threading, random, time, keyboard

x = os.get_terminal_size().columns - 1
y = os.get_terminal_size().lines - 1
count1 = 0
count2 = 0
move1 = 0
move2 = 0
move3 = 0
move4 = 0
speed1 = 0
speed2 = 0
speed3 = 0
speed4 = 0

position = x // 2

printing = []

def default_value():
    global x, y
    for i in range(y):
        printing.append([])
        for j in range(x):
            printing[-1].append(' ')

def show_screen():
    global y
    while True:
        for i in range(y):
            print(''.join(printing[i]))
        os.system('cls')

def rain_make1():
    global move1, speed1
    for i in range(x):
        printing[-1][i] = '='
    time.sleep(random.uniform(0.0, 2.0))  
    while True:
        move1 = random.randint(0, x - 2)
        speed1 = random.uniform(0.03, 0.1)
        for i in range(y - 2):
            printing[i][move1] = '|'
            printing[i + 1][move1] = '|'
            if i > 0:
                printing[i - 1][move1] = ' '
            time.sleep(speed1)
        printing[-2][move1] = ' '
        printing[-3][move1] = ' '

def rain_make2():
    global move2, speed2
    time.sleep(random.uniform(0, 2))  
    
    while True:
        move2 = random.randint(0, x - 2)
        speed2 = random.uniform(0.03, 0.1)
        for i in range(y - 2):
            printing[i][move2] = '|'
            printing[i + 1][move2] = '|'
            if i > 0:
                printing[i - 1][move2] = ' '
            time.sleep(speed2)
        printing[-2][move2] = ' '
        printing[-3][move2] = ' '

def rain_make3():
    global move3, speed3
    time.sleep(random.uniform(0.0, 2.0))
    
    while True:
        move3 = random.randint(0, x - 2)
        speed3 = random.uniform(0.03, 0.1)
        for i in range(y - 2):
            printing[i][move3] = '|'
            printing[i + 1][move3] = '|'
            if i > 0:
                printing[i - 1][move3] = ' '
            time.sleep(speed3)
        printing[-2][move3] = ' '
        printing[-3][move3] = ' '

def rain_make4():
    global move4, speed4
    time.sleep(random.uniform(0.0, 2.0))
    
    while True:
        move4 = random.randint(0, x - 2)
        speed4 = random.uniform(0.03, 0.1)
        for i in range(y - 2):
            printing[i][move4] = '|'
            printing[i + 1][move4] = '|'
            if i > 0:
                printing[i - 1][move4] = ' '
            time.sleep(speed4)
        printing[-2][move4] = ' '
        printing[-3][move4] = ' '

def person_position():
    global position
    printing[-2][position] = '%'
    printing[-3][position] = '%'
    while True:
        if keyboard.is_pressed("right") and position < x - 1:
            printing[-2][position] = ' '
            printing[-3][position] = ' '
            position += 1
            printing[-2][position] = '%'
            printing[-3][position] = '%'
        if keyboard.is_pressed("left") and position > 0:
            printing[-2][position] = ' '
            printing[-3][position] = ' '
            position -= 1
            printing[-2][position] = '%'
            printing[-3][position] = '%'
        time.sleep(0.025)

def count_score():
    global count1, count2
    count1 = 0
    while True:
        count1 += 0.1
        count2 = "%.1f" %count1
        for i in range(1, (len(count2) + 1)):
            printing[0][-i] = count2[-i]
        time.sleep(0.1)

threading.Thread(target=default_value).start()
threading.Thread(target=show_screen).start()
threading.Thread(target=rain_make1).start()
threading.Thread(target=rain_make2).start()
threading.Thread(target=rain_make3).start()
threading.Thread(target=rain_make4).start()
threading.Thread(target=person_position).start()
threading.Thread(target=count_score).start()