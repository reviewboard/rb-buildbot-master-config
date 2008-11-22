#!/usr/bin/env python

from glob import glob
import os
import sys


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s path file_pattern[,file_pattern] "
                         "[max_files]\n" % sys.argv[0])
        sys.exit(1)

    path = sys.argv[1]
    file_patterns = sys.argv[2].split(",")

    if len(sys.argv) > 3:
        max_files = int(sys.argv[3])
    else:
        max_files = 5

    for file_pattern in file_patterns:
        files = [
            (os.path.getmtime(f), f)
            for f in glob(os.path.join(path, file_pattern))
        ]
        files.sort()
        files.reverse()

        files = files[max_files:]

        for (t, f) in files:
            os.unlink(f)


if __name__ == "__main__":
    main()
