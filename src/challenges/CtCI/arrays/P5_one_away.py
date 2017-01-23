
from collections import Counter


def is_one_letter_away(string1, string2):
    """
    returns True if there is zero or one character different between string1 and
    string2.
    We use the difference of counters, making sure there is at most one letter
    with a count > 0
    """
    c1, c2 = Counter(string1), Counter(string2)
    if len(c1) > len(c2):
        diff = Counter(string1) - Counter(string2)
    else:
        diff = Counter(string2) - Counter(string1)
    return len([_ for _ in diff.values() if _ > 0]) <= 1