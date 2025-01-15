import pytest
from src.calibration import calibrate_heston_parameters

def test_calibration():
    """Tests the Heston Model calibration function."""
    market_prices = [10, 12, 8, 15]
    strikes = [95, 100, 105, 110]
    maturities = [0.5, 1, 1.5, 2]
    S = 100
    r = 0.05

    calibrated_params = calibrate_heston_parameters(market_prices, strikes, maturities, S, r)
    assert isinstance(calibrated_params, dict), "Calibration should return a dictionary of parameters"
    assert len(calibrated_params) == 5, "Calibration should return 5 parameters"
