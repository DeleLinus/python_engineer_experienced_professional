

# Author: Gideon Ayanwoye
# Date: 22-10-2022
# Python version: 3.8.8

## Table of Contents
1. [ Project Description. ](#desc)
2. [ Development Setup ](#setup)
3. [ Installation Setup ](#installation)
4. [ Details of Project ](#dcue)
5. [ References ](#ref)

<a name="desc"></a>
# ETL PIPELINE USING SCHIPOL API

This is a program that:
1. Reads a JSON file similar to what's present in this location (./data/)
2. Sniffs the schema of the JSON file
3. Dumps the output in (./schema/)


<a name="setup"></a>

# Development Setup
To run this system, you must have python installed on your computer.
No third party library has been used for this program. The libraries leveraged include:
* `os`
* `glob`
* `json`
* `re`

which are readily available with python.

> The program file initially included the `json_sniffer.py` module where the whole ETL implementation happened, 
> and the `main.py` file that helps with seamless execution of the program. Another module containing the 
> unit tests (`test_functions.py`), the README.md file, the given data folders.

<a name="installation"></a>
# Running the program
Ensure the following before running the program:
* The input json files should be in the `data` folder.
* Open terminal and ensure the working directory is set to the folder containing the `main.py` program file

Then run the program "main.py" to enjoy this program. output data will be in the `schema` folder named with the number corresponding to the input data file name. 

```bash
$/> python main.py
```

<a name="ref"></a>
## References

- [Python Technical Issues (Stackoverflow)](https://stackoverflow.com/)
