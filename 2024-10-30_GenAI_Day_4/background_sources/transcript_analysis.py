
import re
import pandas as pd

# Function to calculate duration
def calculate_duration_fixed(start, end):
    start = start.split(".")[0]
    end = end.split(".")[0]
    start_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start.split(":"))))
    end_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end.split(":"))))
    return end_seconds - start_seconds

# Function to analyze transcript file
def analyze_transcript(file_path, output_path):
    # Load the transcript file
    with open(file_path, 'r') as file:
        transcript = file.readlines()

    # Parse the transcript for analysis
    data = []
    for i in range(len(transcript)):
        if re.match(r"\d+\n", transcript[i]):  # Line number
            start_end = transcript[i + 1].strip().split(" --> ")
            start_time = start_end[0]
            end_time = start_end[1]
            speaker_text = transcript[i + 2].strip().split(": ", 1)
            if len(speaker_text) == 2:
                speaker, text = speaker_text
                duration = calculate_duration_fixed(start_time, end_time)
                data.append({
                    "Start Time": start_time,
                    "Duration": f"{duration}s",
                    "Speaker": speaker,
                    "Character Count": len(text),
                    "Word Count": len(text.split())
                })

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save the results to a CSV file
    df.to_csv(output_path, index=False)
    return output_path

# Example usage
# file_path = "/path/to/input/transcript.vtt"
# output_path = "/path/to/output/results.csv"
# analyze_transcript(file_path, output_path)
