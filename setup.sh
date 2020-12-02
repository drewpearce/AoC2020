#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ -z "$1" ]
then
  echo "Day is required"
  exit 1
else
  day="$1"
fi

echo "Setting up Day $day"

txt="$DIR/src/inputs/$day.txt"
txt_test="$DIR/src/inputs/$day""_test.txt"
py="$DIR/src/$day.py"

if [ -f "$txt" ]
then
  echo "$txt" already exists
  exit 1
fi

if [ -f "$txt_test" ]
then
  echo "$txt_test" already exists
  exit 1
fi

if [ -f "$py" ]
then
  echo "$py" already exists
  exit 1
fi

echo "Touching text files."
touch "$txt"
touch "$txt_test"

echo "Creating python file from template."
cp "$DIR/template.txt" "$py"
sed -i "" 's/${day}/'$day'/' $py

echo "Done."
