import sys
from .asytest import run_tests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: This script requires one command line argument for tests location.")
        sys.exit(1)

    tests_path = sys.argv[1]
    run_tests(tests_path)