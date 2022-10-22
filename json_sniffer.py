# import necessary modules
import os
import glob
import json
import re


def parser_func(data_folder_path):
    """
    get all files matching extension from directory

    Parameters
    ----------
    data_folder_path : str
        the path to the json file to be read

    Returns
    -------
    all_files : list
         array of paths to all json file present
         in the specified folder path
    """
    all_files = []
    for root, dirs, files in os.walk(data_folder_path):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
    
    return all_files


def sniff_schema(filepath):
    """
    reads and process file name

    Parameters
    ----------
    filepath : str
        the file name/path to be processed

    Returns
    -------
    output_dict : dict
         key:value pair containing the expected output from sniffing
         - key : attributes  within the "message" key
    file_number : str
        the number ending the file name
    """
    # get file number
    try:
        file_number = re.findall(r'_\d+', filepath)[-1]
    except IndexError:
        file_number = ""

    output_dict = {}

    # open file
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    try:
        for key, value in data["message"].items():
            if type(value) == str:
                output_dict[key] = {"type": "string",
                                    "tag": "",
                                    "description": "",
                                    "required": False}
            elif type(value) == float:
                output_dict[key] = {"type": "number",
                                    "tag": "",
                                    "description": "",
                                    "required": False}
            elif type(value) == int:
                output_dict[key] = {"type": "integer",
                                    "tag": "",
                                    "description": "",
                                    "required": False}
            elif type(value) == list and len(value) > 0:
                if type(value[0]) == str:
                    output_dict[key] = {"type": "enum",
                                        "tag": "",
                                        "description": "",
                                        "required": False}
                elif type(value[0]) == dict:
                    output_dict[key] = {"type": "array",
                                        "tag": "",
                                        "description": "",
                                        "required": False}
                else:
                    output_dict[key] = {"type": "array",
                                        "tag": "",
                                        "description": "",
                                        "required": False}
            elif type(value) == list and len(value) == 0:
                output_dict[key] = {"type": "array",
                                    "tag": "",
                                    "description": "",
                                    "required": False}
            elif type(value) == bool:
                output_dict[key] = {"type": "boolean",
                                    "tag": "",
                                    "description": "",
                                    "required": False}
            else:
                output_dict[key] = {"type": "object",
                                    "tag": "",
                                    "description": "",
                                    "required": False}
    except KeyError:
        print(f"Cannot find the message attribute in file {filepath}")
        
    return output_dict, file_number


def load(sniff_result_dict=None, file_number=None, output_folder_path=None):
    """
    dumps the output

    Parameters
    ----------
    sniff_result_dict : dict
        key:value pair containing with the expected output from sniffing
    file_number : str
        the number ending the file name to be used to name the output
        file
    output_folder_path: str
        path to dump the output file
    """
    # serializing json
    json_object = json.dumps(sniff_result_dict, indent=4)
 
    # writing to schema.json
    if len(file_number) >= 1:
        with open(f"{output_folder_path}schema{str(file_number)}.json", "w") as outfile:
            outfile.write(json_object)
            
    else:
        with open(f"{output_folder_path}schema.json", "w") as outfile:
            outfile.write(json_object)
            
            
if __name__ == "__main__":
    all_files = parser_func(data_folder_path="./data/")
    if len(all_files) > 0:
        for file in all_files:
            sniff_result_dict, file_number = sniff_schema(file)
            load(sniff_result_dict=sniff_result_dict, file_number=file_number, output_folder_path="./schema/")
    else:
        print("No files found in the data folder!")
