import unittest
import coverage

def run_tests_with_coverage():
# Start coverage collection
cov = coverage.Coverage()
cov.start()
# Load all tests from the 'autogpt/tests' package
suite = unittest.defaultTestLoader.discover("./tests")

# Run the tests
runner = unittest.TextTestRunner()
runner.run(suite)

# Stop coverage collection
cov.stop()
cov.save()

# Report the coverage
cov.report(show_missing=True)

if name == "main":
run_tests_with_coverage()
