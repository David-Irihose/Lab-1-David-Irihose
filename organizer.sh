#!/bin/bash

# -------------------------------------------
# Organizer Script and Archives CSV files
# -------------------------------------------

# Check/Create archive directory
if [ ! -d "archive" ]; then
    mkdir archive
fi

# csv files in current directory
for file in *.csv; do
    
    # If no CSV files exist, skip
    [ -e "$file" ] || continue

    #Generate timestamp (YYYYMMDD-HHMMSS)
    timestamp=$(date +"%Y%m%d-%H%M%S")

    #Create new filename
    base="${file%.csv}"
    newname="${base}-${timestamp}.csv"

    # Log the action + file contents
    echo "----------------------------------------" >> organizer.log
    echo "Archived: $file  --> archive/$newname" >> organizer.log
    echo "Timestamp: $timestamp" >> organizer.log
    echo "File contents:" >> organizer.log
    cat "$file" >> organizer.log
    echo "" >> organizer.log

    #Move & rename the CSV
    mv "$file" "archive/$newname"

done

echo "Archiving complete."
