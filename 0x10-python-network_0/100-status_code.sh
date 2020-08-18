#!/bin/bash
# script to get status code
curl -sIw "%{http_code}" "$1" -o /dev/null
