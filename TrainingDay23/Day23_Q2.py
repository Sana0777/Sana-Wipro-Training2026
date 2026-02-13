import math
import time
from multiprocessing import Pool, cpu_count

numbers = [50000, 60000, 55000, 45000, 70000]

def compute_factorial(n):
    return math.factorial(n)

if __name__ == "__main__":

    starttime1 = time.time()
    seq_results = []

    for num in numbers:
        result = compute_factorial(num)
        seq_results.append(result)
        print(f"Sequential: Factorial {num} calculated")

    seqtime = time.time() - starttime1
    print(f"\nSequential Time: {seqtime}")


    starttime2 = time.time()

    with Pool(cpu_count()) as pool:
        parallel_results = pool.map(compute_factorial, numbers)

    for num in numbers:
        print(f"Multiprocessing: Factorial {num} calculated")

    paralleltime = time.time() - starttime2
    print(f"\nParallel Time: {paralleltime}")
