#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.length != 1
  puts "Usage: #{$0} <string>"
  exit 1
end

# Get the argument
input_string = ARGV[0]

# Define the regular expression
regex = /School/

# Check if the input string matches the regular expression
if input_string.match?(regex)
  puts "Match found!"
else
  puts "No match found."
end

