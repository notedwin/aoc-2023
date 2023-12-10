#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <day_number>"
    exit 1
fi

name="day$1"

mkdir $name 

cp init.py "$name/$name.py"
touch "$name/${name}_test.txt"
touch "$name/$name.txt"

echo "'$name' setup successfully."
