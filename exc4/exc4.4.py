import itertools

def gen_secs():
    """Generates the seconds of the minute"""
    for sec in range(60):
        yield sec

def gen_mins():
    """Generates the minutes of the hour"""
    for min in range(60):
        yield min

def gen_hours():
    """Generates the hours of the day"""
    for hour in range(24):
        yield hour

def gen_time():
    """Generates the time in the format hh:mm:ss
    :return: a generator of the time in the format hh:mm:ss"""
    # iterate through hours
    for hour in gen_hours():
        # iterate through minutes
        for min in gen_mins():
            # iterate through seconds
            for sec in gen_secs():
                # yield the time
                yield "%02d:%02d:%02d" % (hour, min, sec)

def gen_years(start=2024):
    """Generates the years from a given start year
    :param start: the year to start from
    :return: a generator of the years from the start year
    for 100 years"""
    for year in range(start, start+100):
        yield year

def gen_months():
    """Generates the months of the year"""
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    """Generates the days of the month for a given month
    :param month: the month to generate days for
    :param leap_year: whether the year is a leap year
    :return: a generator of the days of the month"""
    # If the month is in the list of months with 31 days
    if month in [1, 3, 5, 7, 8, 10, 12]:
        for day in range(1, 32):
            yield day
    # If the month is in the list of months with 30 days
    elif month in [4, 6, 9, 11]:
        for day in range(1, 31):
            yield day
    # If the month is February
    elif month == 2:
        # If it is a leap year
        if leap_year:
            for day in range(1, 30):
                yield day
        # If it is not a leap year
        else:
            for day in range(1, 29):
                yield day

def gen_date():
    """Generates a date in the format dd/mm/yyyy hh:mm:ss
    of every second for 100 years starting from 2024
    :return: a generator of the date and time"""
    # iterate through years
    for year in gen_years():
        # iterate through months
        for month in gen_months():
            # iterate through days
            for day in gen_days(month, year%4==0):
                # iterate through time
                for gt in gen_time():
                    # yield the date
                    yield "%02d/%02d/%04d %s" % (day, month, year, gt)

def main():
    # Test gen_secs
    date = gen_date()
    # Print the date every 1,000,000th seconds
    for gd in itertools.islice(date, 1000000, None, 1000000):
            print(gd)

if __name__ == "__main__":
    main()
