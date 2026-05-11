#! /usr/bin/env uv run
"""Join multi-line chat messages into single"""

import sys
import re


def does_start_with_timestamp(line):
    """
    Check if the line starts with a timestamp.

    Parameters:
        line (str): The line to check.

    Returns:
        bool: True if the line starts with a timestamp, False otherwise.

    """
    # Extract the sequence of non-space characters at the beginning of the line
    match = re.match(r"^\S+", line)
    if match:
        timestamp_candidate = match.group(0)
        # Check if the candidate matches the HH:MM:SS format
        if re.match(r"^\d{2}:\d{2}:\d{2}$", timestamp_candidate):
            return True
    return False


def process_chat_messages(input_stream, output_stream):
    """
    Processmulti-line chat messages to join them into single-line entries.

    Parameters:
        input_stream: The input stream to read the chat messages from.
        output_stream: The output stream to write the processed messages to.
    """
    current_message = ""

    for line in input_stream:
        stripped_line = line.strip()

        # Detect a new message by timestamp at the start
        if does_start_with_timestamp(stripped_line):
            # If there's a current message, write it out
            if current_message:
                output_stream.write(current_message + "\n")
                current_message = ""

            # Start a new message
            current_message = stripped_line
        else:
            # If it's part of the current message, append to it
            if current_message:
                current_message += " " + stripped_line

    # Write the last message if there's one
    if current_message:
        output_stream.write(current_message + "\n")


if __name__ == "__main__":
    process_chat_messages(sys.stdin, sys.stdout)
