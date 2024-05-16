from datetime import datetime

def timeLogger(func):
    def benchmark_func(*args):
        print(f"{func} started at {datetime.now()}.")
        func(*args)
        print(f"{func} completed at {datetime.now()}.")
    return benchmark_func

@timeLogger
def valueDoubler(n):
    values = [x * 2 for x in range(n)]
    print(values)

valueDoubler(10)