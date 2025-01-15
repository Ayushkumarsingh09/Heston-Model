import pytest
from src.heston_model import heston_price

def test_heston_price():
    """Tests the Heston pricing function."""
    S = 100
    K = 100
    T = 1
    r = 0.05
    kappa = 2.0
    theta = 0.04
    sigma = 0.3
    rho = -0.7
    v0 = 0.04

    price = heston_price(S, K, T, r, kappa, theta, sigma, rho, v0, "call")
    assert price > 0, "Price should be positive"
