import unittest
import subprocess

# Run the tests and get the results
result = subprocess.run(['python', '-m', 'unittest', 'discover', '-s', 'tests'], capture_output=True, text=True)

# Parse the result to calculate the score
output = result.stdout.splitlines()
total_tests = 0
failures = 0
errors = 0
for line in output:
    if "Ran" in line and "tests" in line:
        total_tests = int(line.split()[1])
    if "FAILED" in line:
        parts = line.split(',')
        for part in parts:
            if "failures" in part:
                failures = int(part.split()[0])
            if "errors" in part:
                errors = int(part.split()[0])

passed_tests = total_tests - failures - errors
score = (passed_tests / total_tests) * 5 if total_tests > 0 else 0

print(f'Score: {score}/5')

