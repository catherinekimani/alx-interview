#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """


import sys


def print_stats(stats, file_size):
    """ script that reads stdin line by line and computes metrics """
    print(f"File size: {file_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")


if __name__ == '__main__':
    file_size, count = 0, 0
    status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    stats = {k: 0 for k in status_codes}
    try:
        for line in sys.stdin:
            count += 1
            parts = line.split()
            try:
                status_code = parts[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass
            try:
                file_size += int(parts[-1])
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                print_stats(stats, file_size)

        print_stats(stats, file_size)

    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
