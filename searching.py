import os
import json
from turtle import position

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


def linear_search(sequention : str, number : int):
    search_results_dict = {"positions":[], "count":0}
    for index,item in enumerate(sequention):
        if item == number:
            search_results_dict["positions"].append(index)
            search_results_dict["count"] += 1
    return search_results_dict



def main():
    sequential_data = read_data("sequential.json","unordered_numbers")
    # print(sequential_data)
    print(linear_search(sequential_data, 0))

if __name__ == '__main__':
    main()