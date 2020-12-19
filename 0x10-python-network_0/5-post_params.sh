#!/bin/bash
# sends a POST request to the passed URL, and displays the body
curl -s -X POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
