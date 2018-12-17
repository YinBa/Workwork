import time
i = 0
while True:
    try:
        print("Writing the %dth Message" % i)

        f = open("TheOrigin.txt", "a")
        f.write("Hello! This is the %dth message\n" % i)
        f.close()
        time.sleep(1)

        i = i + 1

        if i == 50000:
            break
    except:
        print("error")
        break