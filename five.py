from threading import Thread
def bomb():
    t1 = Thread(target=bomb).start()
    t2 = Thread(target=bomb).start()
    t1.join()
    t2.join()
bomb()
