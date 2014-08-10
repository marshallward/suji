import yaml

def minute_to_kana(minutes):

    # Check input
    if not type(minutes) is int or minutes < 0:
        raise ValueError('Input must be a non-negative integer.')

    with open('time.yaml') as time_file:
        time_file = yaml.load(time_file)

    m_kana = decakana(minutes)

    if minutes > 0 and minutes % 10 == 0:
        m_kana += t_cnt['minutes'][10]
    else:
        m_kana += t_cnt['minutes'][minutes % 10]

    return m_kana


def decakana(num, kanji=False):
    """Return the reading for the portion of ``num`` greater than 10."""

    # TODO: Kanji readings
    # TODO: num >= 100
    assert num < 100

    with open('digits.yaml') as digits_file:
        digits = yaml.load(digits_file)

    danum_q = num / 10
    danum_r = num % 10

    danum_kana = ''
    if num >= 20:
        danum_kana += digits[danum_q]

    if num >= 10 and danum_r > 0:
        danum_kana += digits[10]

    return danum_kana
