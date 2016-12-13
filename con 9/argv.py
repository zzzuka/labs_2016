import sys

s = 0
for arg in range(1, len(sys.argv)):
    try:
        s += int(sys.argv[arg])
    except ValueError:
        pass
sys.exit(s)