import subprocess

def run_tests():
    # Run unittest and automatically discover all tests in the 'tests/' directory
    subprocess.run(["python", "-m", "unittest", "discover", "tests"])

if __name__ == "__main__":
    run_tests()
