# 9
from threading import Thread
import time
def thread_function(name):
    print("Thread ", name, " starting:")
    for i in range(1, 11)[::-1]:
        print("Thread ", name, ": ", i)
        time.sleep(1)
    print("Thread ", name, ": finishing")

x = threading.Thread(target=thread_function, args=(1,))
time.sleep(0.05)
y = threading.Thread(target=thread_function, args=(2,))
print("Работа начата")
x.start()
y.start()
x.join()
y.join()
print("Работа завершена")
