import threading
import time

# Function for each timer
def timer_function(timer_name, duration):
    for i in range(1, duration + 1):
        time.sleep(1)
        print(f"{timer_name}: (i) second(s) passed")
    print(f"{timer_name} completed!\n")

# Main execution
if __name__== "__main__":
    # Creating threads for multiple timer
    thread1 = threading.Thread(target=timer_function, args=("Timer 1", 5))
    thread2 = threading.Thread(target=timer_function, args=("Timer 2", 3))
    thread3 = threading.Thread(target=timer_function, args=("Timer 3", 4))

    # Start all timers
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all timer to complete
    thread1.join()
    thread2.join()
    thread3.join()

    print("All timers have finished!")