# Python File Management System

## Description

This project implements a file management system using a client-server architecture. The server allows clients to perform various file operations remotely.

## Features

- File listing (`ls`)
- Changing directories (`cd`)
- Creating directories (`mkdir`)
- Deleting files (`del`)
- Removing directories (`rmdir`)
- Creating files (`touch`)
- Displaying directory structure (`tree`)
- Uploading files to the server (`upload <filename>`)

## Installation

1. **Prerequisites**: Python 3.x
2. Clone the repository: `git clone <repository-url>`
3. Navigate to the project directory: `cd <project-directory>`
4. **Running the Server**: `python server.py`
5. **Running the Client**: `python client.py`

## Usage

- Enter commands as prompted by the client interface to perform file operations.

## Example Commands

- `ls`: Lists files and directories.
- `cd <directory>`: Changes the current directory.
- `mkdir <folderName>`: Creates a new directory.
- `del <filename>`: Deletes a file.
- `rmdir <folderName>`: Removes a directory.
- `touch <filename>`: Creates a new file.
- `tree`: Displays the directory structure.
- `upload <filename>`: Uploads a file to the server.

### Example Inputs

#### Valid Input

1. **Listing Files**:
   - **Input**: `ls`
   - **Expected Output**: Lists files and directories in the current directory.

2. **Creating a Directory**:
   - **Input**: `mkdir newFolder`
   - **Expected Output**: Confirmation message that `newFolder` has been created.

#### Invalid Input

1. **Unknown Command**:
   - **Input**: `move file.txt`
   - **Expected Output**: Error message "Unknown command".

2. **Deleting Non-existent File**:
   - **Input**: `del nonExistentFile.txt`
   - **Expected Output**: Error message or notification that the file does not exist.

## Troubleshooting

- Ensure proper network connectivity and server availability.

