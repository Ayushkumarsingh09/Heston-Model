import numpy as np
import matplotlib.pyplot as plt
from src.heston_model import heston_price

def plot_option_prices(S, K, T, r, kappa, theta, sigma, rho, v0, option_type="call"):
    """Plots option prices for different strike prices under the Heston Model."""
    strikes = np.linspace(50, 150, 100)
    prices = [heston_price(S, K, T, r, kappa, theta, sigma, rho, v0, option_type) for K in strikes]

    plt.figure(figsize=(10, 6))
    plt.plot(strikes, prices, label=f"Heston {option_type.capitalize()} Prices")
    plt.xlabel("Strike Price")
    plt.ylabel("Option Price")
    plt.title("Heston Model Option Prices")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example parameters
    S = 100
    T = 1
    r = 0.05
    kappa = 2.0
    theta = 0.04
    sigma = 0.3
    rho = -0.7
    v0 = 0.04

    plot_option_prices(S, K=100, T=T, r=r, kappa=kappa, theta=theta, sigma=sigma, rho=rho, v0=v0, option_type="call")
