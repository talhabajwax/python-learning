import time
seconds = int(input("enter the number of seconds you want to set timer for: "))
while seconds > 0:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    print(f"{hours}:{minutes}:{remaining_seconds}")
    seconds = seconds - 1
    time.sleep(1)

print("Time's up!")