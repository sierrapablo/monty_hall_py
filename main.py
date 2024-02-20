import random
import pandas as pd
import matplotlib.pyplot as plt
import os


def simulate_monty_hall(num_simulations):
    results = {'Change': [], 'Keep': []}

    for _ in range(num_simulations):

        prize_door = random.randint(0, 2)
        contestant_choice = random.randint(0, 2)

        # Monty Hall opens a door with a goat that has not been selected
        monty_opens = next(door for door in range(
            3) if door != prize_door and door != contestant_choice)

        # The contestant changes their first election
        remaining_doors = [door for door in range(
            3) if door != contestant_choice and door != monty_opens]
        final_choice = remaining_doors[0]

        # End game results
        win_change = final_choice == prize_door
        win_keep = contestant_choice == prize_door

        results['Change'].append(win_change)
        results['Keep'].append(win_keep)

    df = pd.DataFrame(results)
    return df.cumsum()


def plot_results(df, save_dir):

    plt.figure(figsize=(10, 6))

    plt.plot(df.index, df['Change'], label='Change', color='blue')
    plt.plot(df.index, df['Keep'], label='Keep', color='red')

    plt.text(df.index[-1] - 2000, df["Change"].iloc[-1] + 1000,
             f'{df["Change"].iloc[-1]}',
             fontsize=10, color='blue')
    plt.text(df.index[-1] - 2000, df["Keep"].iloc[-1] + 1000,
             f'{df["Keep"].iloc[-1]}',
             fontsize=10, color='red')

    plt.title('Monty Hall Simulation Results')
    plt.xlabel('Number of Simulations')
    plt.ylabel('Cumulative Wins')
    plt.legend()
    plt.grid(True)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_path = os.path.join(save_dir, 'monty_hall_results.png')
    plt.savefig(save_path)


def main():
    num_simulations = 100000
    save_dir = 'results'
    df = simulate_monty_hall(num_simulations)
    plot_results(df, save_dir)


if __name__ == "__main__":
    main()
