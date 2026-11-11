import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status

def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10

def test_gold_dining():
    assert reward_points("gold", 500, "dining", False) == 20

def test_platinum_travel():
    assert reward_points("platinum", 500, "travel", False) == 40

def test_fuel_category():
    assert reward_points("gold", 500, "fuel", False) == 0

def test_weekend_bonus():
    assert reward_points("gold", 500, "grocery", True) == 60

def test_classic_weekend():
    assert reward_points("classic", 500, "grocery", True) == 5

def test_unknown_card_tier():
    with pytest.raises(ValueError):
        reward_points("silver", 500, "grocery", False)

def test_invalid_amount():
    with pytest.raises(ValueError):
        reward_points("gold", 0, "grocery", False)

def test_zero_late_fee():
    assert late_payment_fee(5000, 0) == 0

def test_small_outstanding_fee():
    assert late_payment_fee(500, 5) == 100

def test_medium_outstanding_fee():
    assert late_payment_fee(5000, 5) == 500

def test_large_outstanding_fee():
    assert late_payment_fee(15000, 5) == 1000

def test_late_payment_extra_fee():
    assert late_payment_fee(500, 35) == 850

def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"

def test_blocked_card():
    assert card_status(20, 3, False) == "blocked"

def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"

def test_watch_status():
    assert card_status(50, 0, False) == "watch"

def test_good_status():
    assert card_status(20, 0, False) == "good"

