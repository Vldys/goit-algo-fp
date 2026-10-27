
import random
from collections import Counter

import matplotlib.pyplot as plt


def monte_carlo_simulation(num_rolls):
    """Моделювання кидків двох гральних кубиків."""
    results = Counter()

    for _ in range(num_rolls):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)

        total = die_1 + die_2
        results[total] += 1

    probabilities = {
        total: results[total] / num_rolls * 100
        for total in range(2, 13)
    }

    return probabilities


def theoretical_probabilities():
    """Аналітичні ймовірності сум двох кубиків."""
    return {
        total: (6 - abs(7 - total)) / 36 * 100
        for total in range(2, 13)
    }


def visualize_results(simulated, theoretical):
    sums = list(range(2, 13))

    simulated_values = [simulated[s] for s in sums]
    theoretical_values = [theoretical[s] for s in sums]

    plt.figure(figsize=(11, 6))

    plt.bar(
        [s - 0.2 for s in sums],
        simulated_values,
        width=0.4,
        label="Monte Carlo"
    )

    plt.bar(
        [s + 0.2 for s in sums],
        theoretical_values,
        width=0.4,
        label="Theoretical"
    )

    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability (%)")
    plt.title("Monte Carlo vs Theoretical Probabilities")
    plt.xticks(sums)
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    plt.show()


def main():
    num_rolls = 100000

    simulated = monte_carlo_simulation(num_rolls)
    theoretical = theoretical_probabilities()

    print(f"Кількість кидків: {num_rolls}")
    print()
    print(
        f"{'Сума':<8}"
        f"{'Монте-Карло':<18}"
        f"{'Теоретична':<18}"
        f"{'Різниця'}"
    )

    for total in range(2, 13):
        sim = simulated[total]
        theory = theoretical[total]
        difference = abs(sim - theory)

        print(
            f"{total:<8}"
            f"{sim:<18.2f}"
            f"{theory:<18.2f}"
            f"{difference:.2f}"
        )

    visualize_results(simulated, theoretical)


if __name__ == "__main__":
    main()
