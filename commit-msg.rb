#!/usr/bin/env ruby
# frozen_string_literal: true

# Main execution
if ARGV.empty?
  puts "Error: No commit message file provided."
  exit(1)
end

SUBJECT_MAX_LENGTH = 50
BODY_MAX_LENGTH = 72
ERRORS  = []

def clean_line(line)
  line.start_with?("#") ? nil : line
end

def read_commit_message(file_path)
  File.readlines(file_path, chomp: true).map { |line| clean_line(line.strip) } .compact
end

def validate_line_length(line, length = 0)
  !line.nil? && line.length <= length
end

def validate_commit_message(message)

  if message[0].nil? || message[0].empty?
    ERRORS << "Commit message is missing a Subject line"
  end

  if !message[0].downcase.start_with?('merge') && !validate_line_length(message[0], SUBJECT_MAX_LENGTH)
    ERRORS << "Subject must be less than #{SUBJECT_MAX_LENGTH} characters"
  end

  if !message[1].nil? && !message[1].empty?
    ERRORS << "There should be a blank line after Subject"
  end

  unless message[2].nil?
    valid_body = message[2..].reject(&:empty?).map { |l| validate_line_length l, BODY_MAX_LENGTH }.all?
    ERRORS << "Some lines in the body of your message exceed the limit of #{BODY_MAX_LENGTH} characters" unless valid_body
  end
end

# Commit message verification
commit_message = read_commit_message(ARGV[0])
validate_commit_message commit_message

if commit_message.reject(&:empty?).empty?
  puts "Commit message cannot be left blank."
  exit(1)
end

unless ERRORS.empty?
  puts 'There are errors in your commit message:'
  puts ERRORS.join("\n")
  exit(1)
end
