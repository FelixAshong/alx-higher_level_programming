#!/bin/bash
# Displays all HTTP methods that a server will accept
curl -sI "$1" | grep "Allow" | cut -d" " -f 2-
