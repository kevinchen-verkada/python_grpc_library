#!/usr/bin/env bash

set -e

BINARY_FULL_PATH=$(realpath "$BINARY")
# Move to the workspace root since the coverage_report.dat file has relative paths in it.
cd "$BUILD_WORKSPACE_DIRECTORY"

# --ignore-errors unmapped seems to be necessary for empty files
$BINARY_FULL_PATH --ignore-errors unmapped "$@"
