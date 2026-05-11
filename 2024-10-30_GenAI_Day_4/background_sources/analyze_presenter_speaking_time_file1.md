
# Analyze Presenter Speaking Time

## Goal
The objective was to analyze the transcript from the file **GMT20241030-154841_Recording.transcript.vtt.txt** and generate a detailed table summarizing each speech segment. The table includes:

- **Start Time**: The timestamp of when each segment begins.
- **Duration**: The length of the speech segment in seconds.
- **Speaker**: The individual speaking.
- **Character Count**: The number of characters in the text spoken.
- **Word Count**: The number of words in the text spoken.

## Steps Taken
1. **Input File**: I used the transcript file **GMT20241030-154841_Recording.transcript.vtt.txt** as the source data.
   
2. **Parsing the File**: 
   - Identified each speech segment by matching the pattern for timestamps and speaker text.
   - Extracted the start and end times, speaker names, and corresponding speech text for each segment.

3. **Duration Calculation**:
   - Implemented a function to calculate the duration of each segment by converting the start and end timestamps into seconds and computing their difference.

4. **Character and Word Count**:
   - Calculated the number of characters and words in the text for each segment using string length and word-splitting functions, respectively.

5. **Data Compilation**:
   - Compiled the extracted data into a structured format (a table) with the following columns:
     - Start Time
     - Duration
     - Speaker
     - Character Count
     - Word Count

6. **Displaying the Table**:
   - Presented the resulting table to the user with the correct file name in the title to ensure clarity and traceability.
