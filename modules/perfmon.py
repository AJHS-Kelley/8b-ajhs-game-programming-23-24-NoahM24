# Python Performance MonitoringModule by Noah Mulder, v1
import time

def exec_start():
    start_time = time.time()
    return start_time

def exec_stop():
    stop_time = time.time()
    return stop_time

def exec_time(start_time, stop_time):
    return f"Execution Time: {start_time - stop_time} seconds.\n"