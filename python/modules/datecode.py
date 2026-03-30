from datetime import datetime
import time
from functools import wraps

current_time = datetime.now()   
print("Current date and time:", current_time)
current_date = datetime.now().date()
print("Current date:", current_date)
current_time_only = datetime.now().time()
print("Current time:", current_time_only)
customtime_format = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
customtime_format1 = datetime.now().strftime("%d:%m:%Y")
print("Custom formatted date and time:", customtime_format)
print("Custom formatted date and time:", customtime_format1)

start = datetime.now()

# Code block to measure execution time
time.sleep(30)
end = datetime.now()
execution_time = (end - start).total_seconds()
print("Execution time in seconds:", execution_time)
print("Execution time in minutes:", execution_time / 60)

# trace the transaction , connnection , timeout, 