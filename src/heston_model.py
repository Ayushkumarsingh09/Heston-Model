import numpy as np
from scipy.integrate import quad

def heston_integrand(phi, S, K, T, r, kappa, theta, sigma, rho, v0, option_type):
    """Computes the integrand for the Heston model."""
    i = 1j
    x = np.log(S)
    if option_type == "call":
        u = 0.5
        b = kappa - rho * sigma
    elif option_type == "put":
        u = -0.5
        b = kappa
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    d = np.sqrt((rho * sigma * i * phi - b)**2 - sigma**2 * (2 * u * i * phi - phi**2))
    g = (b - rho * sigma * i * phi + d) / (b - rho * sigma * i * phi - d)

    C = r * i * phi * T + kappa * theta / sigma**2 * ((b - rho * sigma * i * phi + d) * T - 2 * np.log((1 - g * np.exp(d * T)) / (1 - g)))
    D = (b - rho * sigma * i * phi + d) / sigma**2 * ((1 - np.exp(d * T)) / (1 - g * np.exp(d * T)))

    return np.real(np.exp(C + D * v0 + i * phi * x) / (i * phi))

def heston_price(S, K, T, r, kappa, theta, sigma, rho, v0, option_type="call"):
    """Calculates the option price using the Heston model."""
    integral_1 = quad(lambda phi: heston_integrand(phi, S, K, T, r, kappa, theta, sigma, rho, v0, option_type), 0, np.inf)[0]
    price = 0.5 * (S - K * np.exp(-r * T)) + 1 / np.pi * integral_1
    return price

if __name__ == "__main__":
    # Example parameters
    S = 100      # Stock price
    K = 100      # Strike price
    T = 1        # Time to maturity
    r = 0.05     # Risk-free rate
    kappa = 2.0  # Speed of mean reversion
    theta = 0.04 # Long-term variance
    sigma = 0.3  # Volatility of variance
    rho = -0.7   # Correlation
    v0 = 0.04    # Initial variance

    price = heston_price(S, K, T, r, kappa, theta, sigma, rho, v0, "call")
    print(f"Heston Call Option Price: {price:.4f}")
