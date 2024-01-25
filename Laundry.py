# filename: Laundry.py


def minutesNeeded(m):
    """
    Return integer number of minutes to launder m (integer) loads
    """
    return (m-1) * 25 + 60


if __name__ == "__main__":
    print(minutesNeeded(2))

# EOF
