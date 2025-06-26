import time

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

start_time = time.perf_counter()
result = fib(35)
end_time = time.perf_counter() - start_time

print("Результат вычислений:", result)
print(f"Время выполнения: {end_time:.4f}")