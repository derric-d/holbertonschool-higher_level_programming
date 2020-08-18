#!/bin/bash
# script to send custom header with get
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
