def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append((item, details))
            total_cost += details["cost"]
            total_calories += details["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    # Ініціалізуємо масив dp, де dp[i] - максимальна калорійність для бюджету i
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, details in items.items():
        cost = details["cost"]
        calories = details["calories"]
        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + calories > dp[b]:
                dp[b] = dp[b - cost] + calories
                item_selection[b] = item_selection[b - cost] + [(item, details)]

    max_calories = dp[budget]
    selected_items = item_selection[budget]

    return selected_items, budget, max_calories


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 100

    items1, total_cost1, total_calories1 = greedy_algorithm(items, budget)
    print("Вибрані страви (жадібний алгоритм):")
    for item, details in items1:
        print(f"{item}: вартість = {details['cost']}, калорійність = {details['calories']}")
    print("Загальна вартість:", total_cost1)
    print("Загальна калорійність:", total_calories1)
    print()

    items2, total_cost2, total_calories2 = dynamic_programming(items, budget)
    print("Вибрані страви (динамічне програмування):")
    for item, details in items2:
        print(f"{item}: вартість = {details['cost']}, калорійність = {details['calories']}")
    print("Загальна вартість:", total_cost2)
    print("Загальна калорійність:", total_calories2)

if __name__ == "__main__":
    main()
