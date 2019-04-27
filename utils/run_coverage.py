#!/usr/bin/env python3

import sys
import os

import unittest
import coverage

sys.path.append(os.path.join("..", os.getcwd()))

THRESHOLD = 90

cov = coverage.Coverage()
cov.start()

loader = unittest.TestLoader()
tests = loader.discover("tests")
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)

cov.stop()
cov.save()

rcoverage = cov.html_report(omit="*lib*")

print("Required coverage: {}%".format(THRESHOLD))
print("Code coverage: {}%".format(rcoverage))

if rcoverage < THRESHOLD:
    print("Error: coverage is too low")

    sys.exit(1)
