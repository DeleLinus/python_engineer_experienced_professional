

# Author: Gideon Ayanwoye
# Date: 22-10-2022
# Python version: 3.8.8

## Table of Contents
1. [ Project Description. ](#desc)
2. [ Development Setup ](#setup)
3. [ Running the program ](#installation)
4. [ Running the test ](#installation2)
5. [ References ](#ref)

<a name="desc"></a>
# Data2Bots Python Backend development Assessment 

This is a program that:
1. Reads a JSON file similar to what's present in this location (./data/)
2. Sniffs the schema of the JSON file
3. Dumps the output in (./schema/)


<a name="setup"></a>

# Development Setup
To run this system, you must have python installed on your computer.
No third party library has been used for the main program except for the program testing that uses `jsonschema`. The libraries leveraged for the main program include:
* `os`
* `glob`
* `json`
* `re`

which are readily available with python.

> The program file initially included the `json_sniffer.py` module where the whole ETL implementation happened, 
> and the `main.py` file that helps with seamless execution of the program. Another module containing the 
> unit tests (`test.py`), the `README.md`, `requirements.txt` files and the given data folders.

<a name="installation"></a>
# Running the program
Ensure the following before running the program:
* The input json files should be in the `data` folder.
* Open terminal and ensure the working directory is set to the folder containing the `main.py` program file

Then run the program "main.py" to enjoy this program. output data will be in the `schema` folder named with the number corresponding to the input data file name. 

```bash
$/> python main.py
```

<a name="installation2"></a>
# Running the test
Ensure the required dependency (jsonschema==4.3.2) is installed by running the followiing command in terminal:
NB: Ensure the working directory is set to the folder containing the `requirements.txt` file
```bash
$/> pip install -r requirements.txt
```
Then run the program "test.py":

```bash
$/> python test.py
```


<a name="ref"></a>
## References

- [Python Technical Issues (Stackoverflow)](https://stackoverflow.com/)
