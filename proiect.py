import numpy as np
import matplotlib.pyplot as plt

def simulate_roulette(strategy, bet_amount, rounds, simulations):
    """
    Simulează un joc de ruletă pentru o strategie specifică.

    Args:
        strategy (str): Tipul pariului ('straight', 'color', 'even_odd').
        bet_amount (float): Suma pariată pe rundă.
        rounds (int): Numărul de runde per simulare.
        simulations (int): Numărul de simulări independente.

    Returns:
        dict: Rezultatele simulării cu profituri și pierderi medii.
    """
    outcomes = []

    for _ in range(simulations):
        total_profit = 0

        for _ in range(rounds):
            result = np.random.randint(0, 37)  # Ruleta europeană are 37 de numere

            if strategy == 'straight':
                # Pariu pe un număr specific (câștig 35:1)
                chosen_number = np.random.randint(0, 37)
                if result == chosen_number:
                    total_profit += bet_amount * 35
                else:
                    total_profit -= bet_amount

            elif strategy == 'color':
                # Pariu pe culoare (roșu/negru)
                red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
                chosen_color = 'red' if np.random.rand() < 0.5 else 'black'
                if (result in red_numbers and chosen_color == 'red') or (result not in red_numbers and result != 0):
                    total_profit += bet_amount
                else:
                    total_profit -= bet_amount

            elif strategy == 'even_odd':
                # Pariu pe par/impar (excludem 0)
                chosen_type = 'even' if np.random.rand() < 0.5 else 'odd'
                if (result % 2 == 0 and result != 0 and chosen_type == 'even') or (result % 2 == 1 and chosen_type == 'odd'):
                    total_profit += bet_amount
                else:
                    total_profit -= bet_amount

        outcomes.append(total_profit)

    return {
        'average_profit': np.mean(outcomes),
        'std_dev': np.std(outcomes),
        'outcomes': outcomes
    }

def plot_results(outcomes, strategy):
    """Afișează distribuția câștigurilor și convergența."""
    plt.figure(figsize=(12, 6))

    # Histogramă a câștigurilor
    plt.subplot(1, 2, 1)
    plt.hist(outcomes, bins=20, color='blue', alpha=0.7, edgecolor='black')
    plt.title(f'Distribuția câștigurilor pentru {strategy}')
    plt.xlabel('Profit total')
    plt.ylabel('Frecvența')

    # Convergența profitului mediu
    cumulative_avg = np.cumsum(outcomes) / np.arange(1, len(outcomes) + 1)
    plt.subplot(1, 2, 2)
    plt.plot(cumulative_avg, color='green')
    plt.title('Convergența profitului mediu')
    plt.xlabel('Numărul de simulări')
    plt.ylabel('Profit mediu')

    plt.tight_layout()
    plt.show()

# Parametrii simulării
strategy = 'color'  # 'straight', 'color', 'even_odd'
bet_amount = 10
rounds = 10000
simulations = 1000

# Rulare simulare
results = simulate_roulette(strategy, bet_amount, rounds, simulations)

# Afișare rezultate
print(f"Strategia: {strategy}")
print(f"Profit mediu: {results['average_profit']:.2f}")
print(f"Deviere standard: {results['std_dev']:.2f}")

# Grafic rezultate
plot_results(results['outcomes'], strategy)
