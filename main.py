import json_sniffer as js


if __name__ == "__main__":
    all_files = js.parser_func(data_folder_path="./data/")
    if len(all_files) == 0:
        print("No files found in the data folder!")

    else:
        for file in all_files:
            sniff_result_dict, file_number = js.sniff_schema(file)
            js.load(sniff_result_dict=sniff_result_dict, file_number=file_number, output_folder_path="./schema/")
        print("All files processed and dumped!")
