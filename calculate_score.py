import subprocess
import re

# Run the tests and get the results
result = subprocess.run(['pytest', '--maxfail=1', '--disable-warnings', '-q'], capture_output=True, text=True)

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
    if "collected" in line:
        match = re.search(r"collected (\d+) items", line)
        if match:
            total_tests = int(match.group(1))
    elif "FAILED" in line or "ERROR" in line:
        match = re.search(r"= (\d+) failed, (\d+) passed,", line)
        if match:
            failures = int(match.group(1))

# Calculate the score
passed_tests = total_tests - failures - errors
score = (passed_tests / total_tests) * 5 if total_tests > 0 else 0

print(f'Score: {score}/5')

