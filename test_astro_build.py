from astro_build import calculate_day

def test_calculate_day():
    assert calculate_day(2015, 3, 18, 0) == 5556.0

