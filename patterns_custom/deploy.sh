#!/bin/bash
# Get the directory of the script file
SCRIPT_DIR="$(dirname "$0")"

# Print the script directory for debugging
echo "Script directory: $SCRIPT_DIR"

# Check if the directory exists
if [ ! -d "$SCRIPT_DIR" ]; then
  echo "Error: Directory $SCRIPT_DIR does not exist."
  exit 1
fi

# Copy the contents from the current path to ~/.config/fabric/patterns and overwrite existing files
cp -a "$SCRIPT_DIR"/* ~/.config/fabric/patterns/ | echo