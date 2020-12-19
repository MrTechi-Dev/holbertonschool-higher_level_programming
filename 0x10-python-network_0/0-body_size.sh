#!/bin/bash
#Curl scrip that extarcts the content  length of a header response
curl -sI  "$1" | grep Content-Length | cut -d' ' -f2
