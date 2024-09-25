# Directory Synchronization Script

## Overview

This Python script synchronizes two directories (source and destination) in one-way mode, ensuring that the destination folder mirrors the content of the source folder. The synchronization process copies new or updated files from the source to the destination and deletes files from the destination if they no longer exist in the source.

## The script

•	Synchronizes directories periodically according to a user-specified interval.

•	Logs all operations (file creation, deletion, copying) to a specified log file and the console. 

•	Takes input via command-line arguments for source directory, destination directory, synchronization interval, and log file path.

## Features

•	One-way synchronization (source → destination).

•	Automatically detects new, modified, or deleted files and applies the necessary changes to the destination.

•	Periodic synchronization based on user-defined intervals.

•	Logs detailed information about file operations to a log file and the console.

•	Handles errors such as file copy or delete failures.

•	Uses Python's built-in libraries (no third-party folder sync libraries).

## Requirements

•	Python 3.x

This script uses standard Python libraries like argparse, filecmp, shutil, os, time, and logging, so no external dependencies are required.

## Installation
1.	Ensure you have Python 3.x installed. You can download it from python.org.

2.	Clone this repository:

    git clone https://github.com/goncmeix/DirectorySynchronizationScript

3.	Navigate to the directory where the script is located

## Usage

## Command-line Arguments

This script accepts four command-line arguments:
1.	source: The path to the source directory.
2.	destination: The path to the destination directory.
3.	interval: The synchronization interval in minutes.
4.	log_file: The path to the log file.

## Example

Run the script using the following command:

    python sync_script.py /path/to/source /path/to/destination 10 /path/to/logfile.log
•	/path/to/source – Directory that contains the files to be synced.

•	/path/to/destination – Directory that will be synced to match the source.

•	10 – The script will check for updates and sync every 10 minutes.

•	/path/to/logfile.log – The path where the log file will be saved.

## Stopping the Script

To stop the script, you can press Ctrl+C. The script will log that the synchronization was interrupted and exit cleanly.

## Logging

All file operations (copying and deleting) will be logged in the specified log file. The log entries will include:

•	Timestamps

•	Operation type (copying, deleting)

•	Name of the affected files or directories

•	Any errors encountered

### Example log output:

    2024-09-25 13:00:00 - INFO - Starting directory synchronization
    2024-09-25 13:00:05 - INFO - file.txt was missing from destination directory or had different information, file was copied
    2024-09-25 13:01:00 - INFO - Directory synchronization ended

## Error Handling

•	The script handles potential errors during the file operations using try-except blocks. 

•	If a file copy or delete operation fails, an error message will be logged and printed to the console, allowing you to investigate the problem without halting the script.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contribution

Feel free to submit issues or pull requests if you have suggestions or improvements. All contributions are welcome!

