import sys

s = 0
for arg in range(1, len(sys.argv)):
    if sys.argv[arg].is_integer():
        s += sys.argv[arg]
sys.exit(s)