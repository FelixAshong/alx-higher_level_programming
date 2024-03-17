#!/bin/bash
# Sends a JSON POST request to a URL passed and displays the body of the response.
curl -sH "Content-Type: application/json" -d @"$2" "$1"
