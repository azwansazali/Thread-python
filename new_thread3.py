import threading
import time

# Function for print a task status
def perform_task(task_name, delay, repetitions):
    for i in range(repetitions):
        time.sleep(delay)
        print(f"{task_name}: Task step {i + 1} completed")
    print(f"{task_name} finished!\n")

# Main execution
if __name__== "__main__":
    # Creating threads for different tasks
    thread1 = threading.Thread(target=perform_task, args=("Task A", 1, 5))
    thread2 = threading.Thread(target=perform_task, args=("Task B", 0.7, 6))
    thread3 = threading.Thread(target=perform_task, args=("Task C", 0.5, 8))

    # Start thread
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all task complete
    thread1.join()
    thread2.join()
    thread3.join()

    print("All timers have finished!")