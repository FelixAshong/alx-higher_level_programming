#!/bin/bash
# Sends a GET request to a given URL with a header and displays the response
curl -sL -H 'X-HolbertonSchool-User-Id: 98' "$1"
