import sys

def average(values):
    if not values:
        return 0
    return sum(values) / len(values)


if __name__ == "__main__":
    args =  sys.argv[1:]
    values = [float(arg) for arg in args]
    result = average(values)
    print("Average is:", result)
       
