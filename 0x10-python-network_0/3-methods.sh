#!/bin/bash
#script to get allowed methods
curl -sIX OPTIONS "$1" | grep "Allow": | cut -d" " -f 2-
