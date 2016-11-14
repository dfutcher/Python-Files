#Python Program
import time
fruit = "fruit"
bed = "bed"
sleep = "sleep"
why = "why"
stop="stop"
team = "liverpool"
town = "manchester"
dance = "dance"
print("Hello, my name is Jack\n")
while True:
    answer = input("What would you like me to do? ").lower()
    time.sleep(2)
    words=answer.split()

    if fruit in words:
        print()
        print("Why do i need fruit?")
        print()
    elif bed in words:
        print()
        print("Why do I need to go to bed?")
        print()
    elif sleep in words:
        print()
        print("Why do I need to go to sleep?")
        print()
    elif why in words:
        print()
        print ("I don't know why I like why")
        print()
    elif team in words:
        print()
        print ("Nothing wrong with Liverpool...it's just Manchester Utd are better")
        print()
    elif town in words:
        print()
        print ("I will only hear good things about Manchester!")
        print()
    elif dance in words:
        print()
        print ("I learned my best moves from daddy")
        print()
    elif stop in words:
        print()
        print("OK")
        print()
        break
    else:   
        print()
        print ("Why?")
        print()
    time.sleep(1)

