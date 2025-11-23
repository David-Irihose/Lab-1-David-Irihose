#!/bin/bash

# -------------------------------------------
# Organizer Script - Archives CSV files
# -------------------------------------------

# 1. Check/Create archive directory
if [ ! -d "archive" ]; then
    mkdir archive
fi

# 2. Find all .csv files in current directory
for file in *.csv; do
    
    # If no CSV files exist, skip
    [ -e "$file" ] || continue

    # 3a. Generate timestamp (YYYYMMDD-HHMMSS)
    timestamp=$(date +"%Y%m%d-%H%M%S")

    # 3b. Create new filename
    base="${file%.csv}"
    newname="${base}-${timestamp}.csv"

    # 3c. Log the action + file contents
    echo "----------------------------------------" >> organizer.log
    echo "Archived: $file  --> archive/$newname" >> organizer.log
    echo "Timestamp: $timestamp" >> organizer.log
    echo "File contents:" >> organizer.log
    cat "$file" >> organizer.log
    echo "" >> organizer.log

    # 3d. Move & rename the CSV
    mv "$file" "archive/$newname"

done

echo "Archiving complete."
