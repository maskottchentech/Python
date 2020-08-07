import threading
import time
def helloworld():
    while True:
        print("Hello World")
        time.sleep(1)


def hiworld():
    while True:
        print("Hi World")
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=helloworld)
    t2 = threading.Thread(target=hiworld)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Main Thread")
