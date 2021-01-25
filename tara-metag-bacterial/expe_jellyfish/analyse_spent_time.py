from datetime import datetime

prev = None
month = 1
with open("times.txt") as mfile:
    for line in mfile:
        # Sun Jan 24 05:29:24 CET 2021
        line = line.strip().split()
        day = int(line[2])
        clock = line[3].split(':')
        hh = int(clock[0])
        mm = int(clock[1])
        ss = int(clock[2])

        curtime = datetime(2021, month, day, hh, mm, ss)
        if prev:
            diff = curtime-prev
            print(diff.total_seconds())
        prev = curtime
