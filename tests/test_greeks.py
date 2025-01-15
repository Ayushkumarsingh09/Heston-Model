import pytest
from src.greeks import delta, gamma, vega

def test_delta():
    """Tests Delta calculation for the Heston Model."""
    S = 100
    K = 100
    T = 1
    r = 0.05
    kappa = 2.0
    theta = 0.04
    sigma = 0.3
    rho = -0.7
    v0 = 0.04

    result = delta(S, K, T, r, kappa, theta, sigma, rho, v0, "call")
    assert isinstance(result, float), "Delta should return a float value"

def test_gamma():
    """Tests Gamma calculation for the Heston Model."""
    S = 100
    K = 100
    T = 1
    r = 0.05
    kappa = 2.0
    theta = 0.04
    sigma = 0.3
    rho = -0.7
    v0 = 0.04

    result = gamma(S, K, T, r, kappa, theta, sigma, rho, v0, "call")
    assert isinstance(result, float), "Gamma should return a float value"

def test_vega():
    """Tests Vega calculation for the Heston Model."""
    S = 100
    K = 100
    T = 1
    r = 0.05
    kappa = 2.0
    theta = 0.04
    sigma = 0.3
    rho = -0.7
    v0 = 0.04

    result = vega(S, K, T, r, kappa, theta, sigma, rho, v0, "call")
    assert isinstance(result, float), "Vega should return a float value"
