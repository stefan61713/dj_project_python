# imports go here
import time
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))  # it just works

from dj_project_python import parser


def main():
    """Main entry"""
    pass


if __name__ == '__main__':
    main()

timer_start = time.time()
file = open("example.txt", "r")
text = file.read()
result = parser.split(text)
print(f"Found a total of {result[1]} sentence(s).")
print(f"With a total of {result[2]} character(s) in the file.\n")
print("Found the following sentences:\n")
for i in range(len(result[0])):
    print(f"{i + 1}. {result[0][i]}")
timer_end = time.time()
print(f"\nThis program took {timer_end - timer_start} seconds to finish.")
