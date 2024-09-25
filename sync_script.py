import argparse
import filecmp
import os
import shutil
import time
from datetime import datetime
import logging


# Function to handle directory synchronization
def sync_directories(dirA, dirB):
    try:
        # Compare the two directories
        comparison = filecmp.dircmp(dirA, dirB)

        # Files only in A or different between A and B (to be copied from A to B)
        for file_name in comparison.left_only + comparison.diff_files:
            src_path = os.path.join(dirA, file_name)
            dest_path = os.path.join(dirB, file_name)

            if os.path.isdir(src_path):
                try:
                    shutil.copytree(src_path, dest_path, dirs_exist_ok=True)  # Copy directories
                    log_message = f"{file_name} was missing from destination directory, directory was copied"
                    logging.info(log_message)
                    print(datetime.now(), log_message)
                except Exception as e:
                    logging.error(f"Failed to copy directory {file_name}: {str(e)}")
                    print(datetime.now(), f"Failed to copy directory {file_name}: {str(e)}")
            else:
                try:
                    shutil.copy2(src_path, dest_path)  # Copy files
                    log_message = f"{file_name} was missing from destination directory or had different information, file was copied"
                    logging.info(log_message)
                    print(datetime.now(), log_message)
                except Exception as e:
                    logging.error(f"Failed to copy file {file_name}: {str(e)}")
                    print(datetime.now(), f"Failed to copy file {file_name}: {str(e)}")

        # Files only in B (to be deleted from B)
        for file_name in comparison.right_only:
            dest_path = os.path.join(dirB, file_name)

            if os.path.isdir(dest_path):
                try:
                    shutil.rmtree(dest_path)  # Remove directories
                    log_message = f"{file_name} does not exist in source directory, directory deleted"
                    logging.info(log_message)
                    print(datetime.now(), log_message)
                except Exception as e:
                    logging.error(f"Failed to delete directory {file_name}: {str(e)}")
                    print(datetime.now(), f"Failed to delete directory {file_name}: {str(e)}")
            else:
                try:
                    os.remove(dest_path)  # Remove files
                    log_message = f"{file_name} does not exist in source directory, file deleted"
                    logging.info(log_message)
                    print(datetime.now(), log_message)
                except Exception as e:
                    logging.error(f"Failed to delete file {file_name}: {str(e)}")
                    print(datetime.now(), f"Failed to delete file {file_name}: {str(e)}")

        # Recursively compare subdirectories
        for sub_dir in comparison.common_dirs:
            sync_directories(os.path.join(dirA, sub_dir), os.path.join(dirB, sub_dir))

    except Exception as e:
        logging.error(f"Error during synchronization: {str(e)}")
        print(datetime.now(), f"Error during synchronization: {str(e)}")


# Main execution
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Directory Synchronization Script")
    parser.add_argument('source', help="Source directory path")
    parser.add_argument('destination', help="Destination directory path")
    parser.add_argument('interval', type=float, help="Synchronization interval in minutes")
    parser.add_argument('log_file', help="Log file path")

    args = parser.parse_args()

    dirA = args.source
    dirB = args.destination
    schedule = args.interval * 60  # Convert to seconds
    log_file = args.log_file

    # Setup logging
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Synchronize directories periodically
    while True:
        try:
            logging.info("Starting directory synchronization")
            print(datetime.now(), "Starting directory synchronization")

            sync_directories(dirA, dirB)

            logging.info("Directory synchronization ended")
            print(datetime.now(), "Directory synchronization ended")

            time.sleep(schedule)
        except KeyboardInterrupt:
            logging.info("Synchronization interrupted by user.")
            print(datetime.now(), "Synchronization interrupted by user.")
            break
