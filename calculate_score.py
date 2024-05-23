import unittest
import subprocess
import re

# Run the tests and get the results
result = subprocess.run(['python', '-m', 'unittest', 'discover', '-s', 'tests'], capture_output=True, text=True)

# Print the output for debugging
print("Test output:")
print(result.stdout)

# Initialize counters
total_tests = 0
failures = 0
errors = 0

# Parse the result to calculate the score
for line in result.stdout.splitlines():
    print(f"Processing line: {line}")  # Debug print
    if "Ran" in line and "tests" in line:
        match = re.search(r"Ran (\d+) tests in", line)
        if match:
            total_tests = int(match.group(1))
    elif "FAILED" in line:
        match = re.search(r"FAILED \((failures=(\d+))?(, )?(errors=(\d+))?\)", line)
        if match:
            if match.group(2):
                failures = int(match.group(2))
            if match.group(5):
                errors = int(match.group(5))

# If "FAILED" line not found, check if any tests were run
if total_tests > 0 and (failures == 0 and errors == 0):
    print("All tests passed")
else:
    print(f"Total tests: {total_tests}, Failures: {failures}, Errors: {errors}")

# Calculate the score
passed_tests = total_tests - failures - errors
score = (passed_tests / total_tests) * 5 if total_tests > 0 else 0

print(f'Score: {score}/5')

