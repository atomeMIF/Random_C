#!/bin/bash

# Generate a random number between 0 and 999
randomNumber=$(( RANDOM % 1000 ))

# Print the random number
echo "Generated Random Number: $randomNumber"
