import random
import timeit
import matplotlib.pyplot as plt


# ========== 1. РЕАЛИЗАЦИЯ АЛГОРИТМОВ (К1) ==========

def linear_search(arr, target):
    """Линейный поиск. O(n)."""
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def binary_search(arr, target):
    """
    Бинарный поиск. O(log n).
    ВАЖНО: arr должен быть ОТСОРТИРОВАН!
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Находим середину
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Нашли!
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return -1  # Не нашли


# ========== 3. ТЕСТ НА 100 ЭЛЕМЕНТАХ (К3) ==========

def run_test_100_elements():
    """Создание списка из 100 чисел, сортировка и поиск."""
    # 1. Создаем список случайных чисел
    random_list = [random.randint(1, 1000) for _ in range(100)]

    # 2. КРИТИЧЕСКИ ВАЖНО для бинарного поиска: сортируем список
    sorted_list = sorted(random_list)

    # 3. Выбираем значения для поиска
    target_in_list = sorted_list[50]  # Точно есть (берем 50-й элемент)
    target_missing = -999  # Точно нет

    results = []
    results.append("=== Результаты поиска в ОТСОРТИРОВАННОМ списке из 100 элементов ===")

    # Ищем существующий элемент
    idx_bin_found = binary_search(sorted_list, target_in_list)
    idx_lin_found = linear_search(sorted_list, target_in_list)
    results.append(f"Ищем {target_in_list} (есть): Бинарный = {idx_bin_found}, Линейный = {idx_lin_found}")

    # Ищем отсутствующий элемент
    idx_bin_miss = binary_search(sorted_list, target_missing)
    idx_lin_miss = linear_search(sorted_list, target_missing)
    results.append(f"Ищем {target_missing} (нет): Бинарный = {idx_bin_miss}, Линейный = {idx_lin_miss}\n")

    return results


# ========== 4. СРАВНЕНИЕ СКОРОСТИ И ГРАФИК (К4) ==========

def run_timing_and_plot():
    """Сравнение времени выполнения для обоих алгоритмов."""
    # Размеры списков
    sizes = [10, 100, 1000, 5000, 10000, 50000, 100000]

    times_linear = []
    times_binary = []

    results = []
    results.append("=== Сравнение времени выполнения (худший случай) ===")
    results.append(f"{'Размер':>8} | {'Линейный (сек)':>15} | {'Бинарный (сек)':>15}")
    results.append("-" * 46)

    for size in sizes:
        # Создаем отсортированный список
        arr = list(range(size))
        target = -1  # Ищем то, чего нет (худший случай для обоих)

        # Замеряем линейный поиск
        time_lin = timeit.timeit(lambda: linear_search(arr, target), number=100) / 100
        # Замеряем бинарный поиск
        time_bin = timeit.timeit(lambda: binary_search(arr, target), number=100) / 100

        times_linear.append(time_lin)
        times_binary.append(time_bin)

        results.append(f"{size:>8} | {time_lin:>15.8f} | {time_bin:>15.8f}")

    # Построение графика
    plt.figure(figsize=(10, 6))

    # Ось X (размеры) и ось Y (время)
    plt.plot(sizes, times_linear, marker='o', linestyle='-', color='red', label='Линейный поиск (O(n))')
    plt.plot(sizes, times_binary, marker='s', linestyle='-', color='blue', label='Бинарный поиск (O(log n))')

    plt.title('Сравнение линейного и бинарного поиска')
    plt.xlabel('Размер списка (n)')
    plt.ylabel('Время выполнения (секунды)')
    plt.legend()
    plt.grid(True)

    # Сохраняем график
    plt.savefig('plot_comparison.png')
    plt.close()

    return results


# ========== ГЛАВНЫЙ БЛОК ==========
if __name__ == "__main__":
    all_results = []

    all_results.extend(run_test_100_elements())
    all_results.extend(run_timing_and_plot())

    # Запись в файл
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(all_results))

    # Вывод в консоль
    print("\n".join(all_results))
    print("\n✅ График сохранен в файл plot_comparison.png")