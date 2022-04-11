import os
import json
from typing import List

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name : str, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    # file_path = os.path.join(cwd_path, file_name)
    ### using relative paths, prior row not necessary

    with open(f"{file_name}","r") as json_file:
        sequence = json.load(json_file)

    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None
    else:
        return sequence[field]


def linear_search(sequention : List[int], number : int):
    search_results_dict = {"positions":[], "count":0}
    for index,item in enumerate(sequention):
        if item == number:
            search_results_dict["positions"].append(index)
            search_results_dict["count"] += 1
    return search_results_dict


def pattern_search(sequence : str, pattern : str):
    # print(sequence)
    pattern_indices = set()
    for index in range(len(sequence)-(len(pattern)-1)):
        string = sequence[index:index+len(pattern)]
        # print(index)
        
        # print(string)
        if string == pattern:
            pattern_indices.add(index)
    return pattern_indices





def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    # print(sequential_data)
    # print(linear_search(sequential_data, 0))
    DNA_data = read_data("sequential.json","dna_sequence")
    print(pattern_search(DNA_data,"ATA"))


if __name__ == '__main__':
    main()