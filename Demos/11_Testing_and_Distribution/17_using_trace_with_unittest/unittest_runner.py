# run_tests.py
import unittest, trace, sys, os
# The command-line interface will only trace the test itself, showing how much of the test program is executed
# To trace the module under test, use the programmatic API:
# Create a trace object
# Run unittest.main with exit=False
# Create a CoverageResults object and write the results to files
# Each tested module will produce its own .cover file
def run_tests_with_trace():
    # Create tracer
    tracer = trace.Trace(count=True, trace=False,
        ignoredirs=[sys.prefix, sys.exec_prefix]
    )
    # Discover tests
    suite = unittest.defaultTestLoader.discover(
        ".", pattern="test_bank_utils.py"
    )
    # Run tests inside the tracer
    runner = unittest.TextTestRunner(verbosity=2)

    def run():
        return runner.run(suite)

    result = tracer.runfunc(run)

    # Write coverage results
    results = tracer.results()
    results.write_results(
        show_missing=True, summary=True, coverdir=".")

    return result

if __name__ == "__main__":
    run_tests_with_trace()
