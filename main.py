import random
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv


def simulate_monty_hall(num_simulations: int) -> pd.DataFrame:
    results: dict[str, list[bool]] = {'Change': [], 'Keep': []}

    for _ in range(num_simulations):

        prize_door: int = random.randint(0, 2)
        contestant_choice: int = random.randint(0, 2)

        # Monty Hall opens a door with a goat that has not been selected
        monty_opens: int = next(
            door for door in range(3)
            if door != prize_door
            and door != contestant_choice
        )

        # The contestant changes their first election
        remaining_doors: list[int] = [
            door for door in range(3)
            if door != contestant_choice
            and door != monty_opens
        ]
        final_choice: int = remaining_doors[0]

        # End game results
        win_change: bool = final_choice == prize_door
        win_keep: bool = contestant_choice == prize_door

        results['Change'].append(win_change)
        results['Keep'].append(win_keep)

    df: pd.DataFrame = pd.DataFrame(results)
    return df.cumsum()


def plot_results(df: pd.DataFrame, save_dir: str) -> None:

    plt.figure(figsize=(10, 6))

    plt.plot(df.index, df['Change'], label='Change', color='blue')
    plt.plot(df.index, df['Keep'], label='Keep', color='red')

    plt.text(
        df.index[-1] - 2000,
        df["Change"].iloc[-1] + 1000,
        f'{df["Change"].iloc[-1]}',
        fontsize=10, color='blue'
    )
    plt.text(
        df.index[-1] - 2000,
        df["Keep"].iloc[-1] + 1000,
        f'{df["Keep"].iloc[-1]}',
        fontsize=10, color='red'
    )

    plt.title('Monty Hall Simulation Results')
    plt.xlabel('Number of Simulations')
    plt.ylabel('Cumulative Wins')
    plt.legend()
    plt.grid(True)

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_path: str = os.path.join(save_dir, 'monty_hall_results.png')
    plt.savefig(save_path)


def main():
    load_dotenv()
    num_simulations: int = int(os.getenv("NUM_SIMULATIONS"))
    save_dir: str = os.getenv("SAVE_DIR")
    df: pd.DataFrame = simulate_monty_hall(num_simulations)
    plot_results(df, save_dir)


if __name__ == "__main__":
    main()
