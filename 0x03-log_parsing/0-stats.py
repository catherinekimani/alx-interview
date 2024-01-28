#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys
if __name__ == '__main__':
    filesize, line_count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """ script that reads stdin line by line and computes metrics """
        print("File Size: {:d}".format(filesize))
        for code, count in sorted(stats.items()):
            if count:
                print("{}: {}".format(code, count))
    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                statusCode = data[-2]
                if statusCode in stats:
                    stats[statusCode] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
