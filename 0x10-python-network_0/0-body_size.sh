#!/bin/bash
# script that retrieves the content-length value
curl -sI "$1" | grep "Content-Length" | cut -d" " -f2
