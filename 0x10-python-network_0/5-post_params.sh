#!/bin/bash
# Sends a POST request to a given URL, and displays the body of the response
curl -sL -X POST -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
