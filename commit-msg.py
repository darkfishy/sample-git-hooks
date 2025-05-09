#!/usr/bin/env python
# coding: utf-8

import platform
import sys


if len(sys.argv) < 2:
    print(f"Error: No commit message file provided.\nArgs({len(sys.argv)}): {sys.argv}")
    exit(1)


SUBJECT_MAX_LENGTH = 50
BODY_MAX_LENGTH = 72
ERRORS  = []


def clean_line(line):
    line = line.strip()
    if len(line):
        if line[0] == "#":
            return None
        if line[-1] == "\n":
            return line[:-1]
    return line


def in_venv():
    return sys.prefix != sys.base_prefix


def read_commit_msg():
    with open(sys.argv[1]) as f:
        return [clean_line(l) for l in f.readlines()]


def validate_line_length(line, length=0):
    return len(line) <= length


def validate_commit_message(message):
    try:
        if not message[0]:
            ERRORS.append("Commit message is missing a Subject line")
        elif not message[0].lower().startswith('merge') and not validate_line_length(message[0], SUBJECT_MAX_LENGTH):
            ERRORS.append(f"Subject must be less than {SUBJECT_MAX_LENGTH} characters")

        if message[1]:
            ERRORS.append("There should be a blank line after Subject")

        if message[2]:
            valid_body = all([validate_line_length(item, BODY_MAX_LENGTH) for item in message[2:] if item not in (None, '')])
            ERRORS.append(f"Some lines in the body of your message exceed the limit of {BODY_MAX_LENGTH} characters") if not valid_body else None

    except (IndexError, TypeError):
        pass

# Commit message verification
print(f"Your python version is {platform.python_version()} ({ '' if in_venv() else 'not ' }running in virtualenv).")

validate_commit_message(read_commit_msg())

if len(ERRORS):
    print('There are errors in your commit message:')
    print('\n'.join(ERRORS))
    exit(1)
