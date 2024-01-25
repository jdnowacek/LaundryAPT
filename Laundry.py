# filename: Laundry.py


def minutes_needed(m):
    """
    Return integer number of minutes to launder m (integer) loads
    """
    return (m-1) * 25 + 60


if __name__ == '__main__':
    print(minutes_needed(2))

# EOF
