import yaml

def counter_kana(num, counter_reading):

    yomi = decakana(num)

    if num > 0 and num % 10 == 0:
        yomi += counter_reading[10]
    else:
        yomi += counter_reading[num % 10]

    return yomi


def minutes_to_kana(minutes):

    with open('time.yaml') as time_file:
        min_reading = yaml.load(time_file)['minutes']

    return counter_kana(minutes, min_reading)


def hours_to_kana(hours):

    with open('time.yaml') as time_file:
        hr_reading = yaml.load(time_file)['hours']

    return counter_kana(hours, hr_reading)


def decakana(num, kanji=False):
    """Return the reading for the portion of ``num`` greater than 10."""

    # TODO: Kanji readings
    # TODO: num >= 100
    assert num < 100

    with open('digits.yaml') as digits_file:
        digits = yaml.load(digits_file)

    danum_q = num // 10
    danum_r = num % 10

    danum_kana = ''
    if num >= 20:
        danum_kana += digits[danum_q]

    if num >= 10 and danum_r > 0:
        danum_kana += digits[10]

    return danum_kana
