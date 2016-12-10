#!/bin/bash

set -e

if [ "$TEST_SUITE" = "all-the-rest" ]; then
    py.test $(grep TEST_SUITE= .travis.yml | grep -v all-the-rest | sed 's/^.*=/--ignore /' | paste -d' ' -s)
else
    py.test $TEST_SUITE
fi
