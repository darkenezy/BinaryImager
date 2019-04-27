#!/usr/bin/env python3

import sys
from pylint import lint

THRESHOLD = 10

run = lint.Run(['binaryimager.py'], do_exit=False)
score = run.linter.stats['global_note'] # Yes this is a terrible name for the score

print("Required score: {}".format(THRESHOLD))
print("Code score: {}".format(score))

if score < THRESHOLD:
    print("Error: score is too low")

    sys.exit(1)
