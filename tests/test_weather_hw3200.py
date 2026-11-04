"""
Test file for the weather station functions - Template

Copy this file to `test_weather.py` and replace every TODO with your own tests.
Keep `weather.py` in the same folder so the import below works.
"""

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from weather_hw3200 import (
    celsius_to_fahrenheit,
    clean_readings,
    summarize_temperatures,
)

# =============================================================================
# PART 1: UNIT TESTS
# =============================================================================

@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
        (-273.15, -459.67),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    """Test Celsius to Fahrenheit conversion."""
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected)
    
    """Check that invalid inputs raise the correct errors."""

@pytest.mark.parametrize(
    "bad_input, expected_error",
    [
        ("hello", TypeError),
        (None, TypeError),
        (True, TypeError),
        (-273.16, ValueError),
    ],
)
def test_celsius_to_fahrenheit_invalid(bad_input, expected_error):
    with pytest.raises(expected_error):
        celsius_to_fahrenheit(bad_input)


    """Test temperature summary with one missing value."""

def test_summarize_temperatures():
    temps = [10.0, float("nan"), 20.0]

    result = summarize_temperatures(temps)

    assert result["mean"] == pytest.approx(15.0)
    assert result["min"] == 10.0
    assert result["max"] == 20.0
    assert result["n_missing"] == 1


# =============================================================================
# PART 2: FIXTURES
# =============================================================================

@pytest.fixture
def raw_readings():
    return pd.DataFrame({
        "station": ["JFK", "CPK", "JFK", "CPK", "LGA"],
        "date": ["2026-07-02", "2026-07-01", "2026-07-01",
                 "2026-07-02", "2026-07-01"],
        "temp_c": [30.0, 25.0, float("nan"), 999.0, 28.0],
    })

"""Check the columns, rows, and missing values."""

def test_raw_readings_fixture(raw_readings):
    assert list(raw_readings.columns) == ["station", "date", "temp_c"]
    assert len(raw_readings) == 5
    assert raw_readings["temp_c"].isna().sum() == 1


# =============================================================================
# PART 3: TESTING DATAFRAMES
# =============================================================================
"""Check that readings are cleaned and sorted correctly."""

def test_clean_readings(raw_readings):
    expected = pd.DataFrame({
        "station": ["CPK", "JFK", "LGA"],
        "date": ["2026-07-01", "2026-07-02", "2026-07-01"],
        "temp_c": [25.0, 30.0, 28.0],
        "temp_f": [77.0, 86.0, 82.4],
    })

    actual = clean_readings(raw_readings)

    assert_frame_equal(actual, expected)


# =============================================================================
