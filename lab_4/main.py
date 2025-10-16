import timeit
import matplotlib.pyplot as plt
from typing import List, Tuple


def fact_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n - 1)


def fact_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def benchmark_factorial() -> Tuple[List[int], List[float], List[float]]:
    n_values = [5, 10, 15, 20]
    num_runs = 100

    recursive_times = []
    iterative_times = []

    for n in n_values:
        recursive_time = timeit.timeit(
            stmt=f"fact_recursive({n})",
            setup="from __main__ import fact_recursive",
            number=num_runs
        ) / num_runs
        recursive_times.append(recursive_time)

        iterative_time = timeit.timeit(
            stmt=f"fact_iterative({n})",
            setup="from __main__ import fact_iterative",
            number=num_runs
        ) / num_runs
        iterative_times.append(iterative_time)

    return n_values, recursive_times, iterative_times


def plot_results(n_values: List[int], recursive_times: List[float], iterative_times: List[float]) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, recursive_times, label='Рекурсивная', marker='o', color='red')
    plt.plot(n_values, iterative_times, label='Итеративная', marker='s', color='blue')
    plt.xlabel('n')
    plt.ylabel('Время (сек)')
    plt.title('Сравнение времени выполнения')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    n_values, recursive_times, iterative_times = benchmark_factorial()

    print("Результаты бенчмарка:")
    print("n\tРекурсивная (сек)\tИтеративная (сек)")
    for n, rec, it in zip(n_values, recursive_times, iterative_times):
        print(f"{n}\t{rec:.8f}\t\t{it:.8f}")

    plot_results(n_values, recursive_times, iterative_times)