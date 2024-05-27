import itertools

def gen_secs():
    for sec in range(60):
        yield sec

def gen_mins():
    for min in range(60):
        yield min

def gen_hours():
    for hour in range(24):
        yield hour

def gen_time():
    for hour in gen_hours():
        for min in gen_mins():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, min, sec)

def gen_years(start=2024):
    for year in range(start, start+100):
        yield year

def gen_months():
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year=True):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        for day in range(1, 32):
            yield day
    elif month in [4, 6, 9, 11]:
        for day in range(1, 31):
            yield day
    elif month == 2:
        if leap_year:
            for day in range(1, 30):
                yield day
        else:
            for day in range(1, 29):
                yield day

def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, year%4==0):
                for gt in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, gt)

def main():
    date = gen_date()
    for gd in itertools.islice(date, 1000000, None, 1000000):
            print(gd)

if __name__ == "__main__":
    main()
