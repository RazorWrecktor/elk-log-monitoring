#!/bin/bash

SOURCE_DIR="./Data_original"
ARCHIVE_DIR="./Archive/Data"

mkdir -p "$ARCHIVE_DIR"

for file in "$SOURCE_DIR"/*.json; do
  base=$(basename "$file" .json)
  gzip -c "$file" > "$ARCHIVE_DIR/${base}.json.gz"
#  rm "$file"
done
