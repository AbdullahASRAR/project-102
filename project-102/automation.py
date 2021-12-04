import time
start_time = time.time()
def alarm():
    print("it is time to dring water")
def main():
    while(True):
        if ((time.time() - start_time) >= 3600):
            alarm()
main()