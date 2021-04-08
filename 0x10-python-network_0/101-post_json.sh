#!/bin/bash
# JSON POST request to a URL passed as the first argument
curl -s --header "Content-Type: application/json" --request POST --data @$2 $1
