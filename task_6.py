
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо за співвідношенням калорій до вартості
    sorted_items = sorted(
        items.items(),
        key=lambda item: (
            item[1]["calories"] / item[1]["cost"]
        ),
        reverse=True
    )

    selected = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    # dp[i][b] — максимум калорій для перших i страв
    # за бюджету b
    dp = [
        [0] * (budget + 1)
        for _ in range(n + 1)
    ]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]

            if cost <= b:
                dp[i][b] = max(
                    dp[i][b],
                    dp[i - 1][b - cost] + calories
                )

    # Відновлюємо вибрані страви
    selected = []
    remaining_budget = budget

    for i in range(n, 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            name = names[i - 1]
            selected.append(name)
            remaining_budget -= items[name]["cost"]

    selected.reverse()

    total_cost = sum(
        items[name]["cost"] for name in selected
    )

    total_calories = dp[n][budget]

    return selected, total_cost, total_calories


def main():
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(f"Бюджет: {budget}\n")

    print("Жадібний алгоритм:")
    print("Страви:", greedy_result[0])
    print("Вартість:", greedy_result[1])
    print("Калорії:", greedy_result[2])

    print("\nДинамічне програмування:")
    print("Страви:", dp_result[0])
    print("Вартість:", dp_result[1])
    print("Калорії:", dp_result[2])


if __name__ == "__main__":
    main()
