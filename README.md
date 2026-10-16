# CSV Cleaner



A lightweight Python command-line tool that cleans whitespace from CSV headers and values and removes completely blank rows.



## Features



- Removes leading and trailing whitespace from column names and values.

- Skips completely blank rows.

- Accepts custom input and output file paths.

- Reports missing input files and invalid CSV structures with readable errors.

- Uses Python's built-in libraries; no third-party packages required.



## Requirements



- Python 3.11 or compatible Python 3 version.



## Usage



Run the following command from the project directory:



```powershell

python cleaner.py sample.csv cleaned.csv

```



Replace `sample.csv` with your input file and `cleaned.csv` with the desired output filename.



## Example



\*\*Input:\*\*



```csv

Name,Email,City

&#x20; Rahul Sharma  , rahul@example.com , Delhi

Priya Verma,priya@example.com, Mumbai



&#x20; Amit Kumar, amit@example.com , Jaipur

```



\*\*Output:\*\*



```csv

Name,Email,City

Rahul Sharma,rahul@example.com,Delhi

Priya Verma,priya@example.com,Mumbai

Amit Kumar,amit@example.com,Jaipur

```



## Testing



- Python syntax compilation: passed.

- Sample CSV cleaning: passed with 3 records.

- Custom output filename: passed.

- Missing input file: readable error displayed; unwanted output file was not created.



## Current Limitations



- Designed for simple CSV-cleaning tasks, not every possible CSV format.

- Does not validate email addresses or correct invalid data.

- Does not currently provide a graphical interface.



## Project Status



Beginner portfolio prototype. Further edge-case testing and code review are needed before production use.




