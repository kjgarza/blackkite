#!/bin/bash

# # Define the source and destination directories
# SOURCE_DIR="_user_guide"
# DESTINATION_DIR="_user_guide_markdown_files"

# # Check if the destination directory exists, if not create it
# if [ ! -d "$DESTINATION_DIR" ]; then
#     mkdir -p "$DESTINATION_DIR"
# fi

# # Find and copy all Markdown files from the source to the destination
# find "$SOURCE_DIR" -name '*.md' -exec cp {} "$DESTINATION_DIR" \;

# echo "All Markdown files have been copied to $DESTINATION_DIR"


# Define the source and destination directories
SOURCE_DIR="_developer_guide"
DESTINATION_DIR="_developer_guide_markdown_files"

# Check if the destination directory exists, if not create it
if [ ! -d "$DESTINATION_DIR" ]; then
    mkdir -p "$DESTINATION_DIR"
fi

# Find and copy all Markdown files from the source to the destination
# find "$SOURCE_DIR" -name '*.md' -exec bash -c 'for file; do cp "$file" "$DESTINATION_DIR/$(basename "$(dirname "$file")")_$file"; done' _ {} +


# Find and copy all Markdown files from the source to the destination
find "$SOURCE_DIR" -name '*.md' -exec bash -c '
for file; do
    folder_name=$(basename "$(dirname "$file")")

    prefix="${folder_name//\//_}"

    cp "$file" "$DESTINATION_DIR${prefix}_$(basename "$file")"
done' _ {} +

echo "All Markdown files have been copied to $DESTINATION_DIR"
