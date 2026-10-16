import threading
import time

def monitor_task(task_name, duration):
    print(f"{task_name} started")

    for second in range(1, duration + 1):
        time.sleep(1)
        print(f"{task_name}: {second}/{duration} seconds")

    print(f"{task_name} completed")

task1 = threading.Thread(
    target=monitor_task,
    args=("Download Task", 3)
)

task2 = threading.Thread(
    target=monitor_task,
    args=("Upload Task", 5)
)

task1.start()
task2.start()

task1.join()
task2.join()

print("All tasks completed!")
