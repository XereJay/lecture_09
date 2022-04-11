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


def binary_search(array : List[int], number):
    # print(array)
    left_index = 0
    right_index = len(array) - 1
    middle_index = len(array)//2 - 1 +len(array)%2

    nr_of_iter = 0
    while nr_of_iter <len(array):
        if array[middle_index] == number:
            return middle_index
        elif array[middle_index] > number:
            right_index = middle_index
            middle_index = right_index//2
        else:
            left_index = middle_index
            middle_index = middle_index + (right_index-left_index)//2
        
        nr_of_iter +=1
    else:
        return array[-1]





def main():
    # sequential_data = read_data("sequential.json","unordered_numbers")
    # print(sequential_data)
    # print(linear_search(sequential_data, 0))
    # DNA_data = read_data("sequential.json","dna_sequence")
    # print(pattern_search(DNA_data,"ATA"))
    sorted_list = read_data("sequential.json", "ordered_numbers")
    print(binary_search(sorted_list,120))

if __name__ == '__main__':
    main()