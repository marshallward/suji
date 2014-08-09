import yaml
import datetime

def minute_to_kana(minutes):

    # Check input
    if not type(minutes) is int or minutes < 0 or minutes >= 60:
        raise ValueError('Input must be an integer between 0 and 59'
                         ' (inclusive).')

    with open('time.yaml') as t_cnt_file:
        t_cnt = yaml.load(t_cnt_file)

    # "decaminute" and its remainder
    damin_q = minutes / 10
    damin_r = minutes % 10

    # Set the multiple of 10 (if present)
    m_kana = ''
    if minutes >= 20:
        m_kana = t_cnt['digits'][damin_q]

    if minutes >= 10 and damin_r > 0:
        m_kana += t_cnt['digits'][10]

    if minutes > 0:
        if damin_r == 0:
            m_kana += t_cnt['minutes'][10]
        else:
            m_kana += t_cnt['minutes'][damin_r]
    else:
        m_kana = t_cnt['minutes'][0]

    print(m_kana)
