import threading
import time

# Function to count from 1 to 100
def count_1_to_100():
    for i in range(1, 101):
        print(f"Count 1 to 100: {i}")
        time.sleep(0.1)  # Delay for demonstration

# Function to count from 2 to 200 (step of 2)
def count_2_to_200():
    for i in range(2, 201, 2):
        print(f"Count 2 to 200: {i}")
        time.sleep(0.1)  # Delay for demonstration

# Create threads for both loops
thread1 = threading.Thread(target=count_1_to_100)
thread2 = threading.Thread(target=count_2_to_200)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both loops are done!")
