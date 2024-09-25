# Python Utils

**Python Utils** is a collection of scripts and tools written in Python to automate various tasks, simplify workflows, and handle common data processing tasks. This repository is designed to be modular and easily extensible, making it easy to add new scripts or modify existing ones.

## Table of Contents

- [Structure](#structure)
- [Scripts](#scripts)
- [Installation](#installation)

## Structure

- `scripts/`: Contains individual Python scripts organized by category.
- `utils/`: Shared utility functions used by multiple scripts.
- `tests/`: Unit tests for the scripts.
- `requirements.txt`: List of Python dependencies required by the scripts.

## Scripts

### Available Scripts

1. **clean_emails.py**
   - **Description**: Sorts an email list alphabetically and removes duplicates.
   - **Category**: Data Processing
   - **Usage**:

     ```bash
     python scripts/clean_emails.py <email_list.txt>
     ```

2. **csv_merger.py** (To be developed)
   - **Description**: Merges multiple CSV files into one based on common columns.
   - **Category**: Data Processing
   - **Planned Features**:
     - Merge based on column headers
     - Optional removal of duplicate rows
     - Output as a single CSV or Excel file

3. **file_organizer.py** (To be developed)
   - **Description**: Organizes files in a directory based on file type or date.
   - **Category**: File Management
   - **Planned Features**:
     - Move files into folders by file type (e.g., `.txt`, `.jpg`, `.pdf`)
     - Option to organize by creation or modification date

4. **common_functions.py**
   - **Description**: Contains common utility functions like file reading/writing, logging, and error handling.

### Planned Scripts

- **json_validator.py**
  - **Description**: Validates JSON files against a schema and reports errors.
  - **Category**: Data Validation

- **text_report_generator.py**
  - **Description**: Generates summary reports from text files by extracting key information.
  - **Category**: Reporting

- **image_resizer.py**
  - **Description**: Resizes images in bulk based on user-defined dimensions.
  - **Category**: Image Processing

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-utils.git
   cd python-utils
