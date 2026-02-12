#!/bin/bash
# Monitor clipboard for changes and append new content to stickies.txt
# Usage: ./scrape_clipboard.sh
# Stop with Ctrl-C

OUTFILE="stickies.txt"
LAST=""

echo "Watching clipboard... Cmd-C each sticky. Ctrl-C to stop."
echo "Output: $OUTFILE"
echo ""

while true; do
    CURRENT=$(pbpaste)
    if [ "$CURRENT" != "$LAST" ] && [ -n "$CURRENT" ]; then
        echo "$CURRENT" >> "$OUTFILE"
        LAST="$CURRENT"
    fi
    sleep 0.3
done
