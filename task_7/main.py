import random
import matplotlib.pyplot as plt
import pandas as pd


def roll_dies_monte_carlo(n):
    # Initialize a dictionary to count occurrences of each sum
    sum_counts = {i: 0 for i in range(2, 13)}

    # Simulate rolling two dice
    for _ in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sum_counts[dice_sum] += 1

    return sum_counts


def plot_results(sums, simulated_probs):
    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.bar(sums, simulated_probs, color="orange")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Simulated Probability")
    plt.title("Simulated Probabilities for Sums of Two Dice")
    plt.grid(True)
    plt.show()


def main():
    n = 100000
    sum_counts = roll_dies_monte_carlo(n)

    probabilities = {sum_value: count / n for sum_value, count in sum_counts.items()}

    # Convert results to lists for plotting
    sums = list(sum_counts.keys())
    simulated_probs = [probabilities[sum_value] for sum_value in sums]

    plot_results(sums, simulated_probs)

    # Output the simulated probabilities as a markdown table
    probability_df = pd.DataFrame(
        list(probabilities.items()), columns=["Сума", "Імовірність"]
    )
    print(probability_df.to_markdown(index=False))


if __name__ == "__main__":
    main()
