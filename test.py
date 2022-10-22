import unittest
import json
from jsonschema import validate
import json_sniffer as js

# initialize global variables
global test_schema
global test_json
with open("./schema/schema_1.json") as schema_file:
    test_schema = json.load(schema_file)

with open("./data/data_1.json") as json_file:
    test_json = json.load(json_file)




class TestFunctions(unittest.TestCase):
    """
    Using data_1 and schema_1 output
    test the following cases
    - Padding: All attributes in the JSON schema should be padded with "tag" and "description" keys
    - The JSON schema properties "required" is false
    - For data types of the JSON schema:
        - STRING: program should identify what is a string and map accordingly in JSON schema output
        - INTEGER: program should identify what is an integer and map accordingly in JSON schema output
        - ENUM: When the value in an array is a string, the program should map the data type as an ENUM
        - ARRAY: When the value in an array is another JSON object, the program should map the data type as an ARRAY
    """

    def test_output_json_object(self):
        """
        # Test the whole JSON is valid against the Schema
        """

        validate(instance=test_json, schema=test_schema)


if __name__ == '__main__':
    unittest.main()
