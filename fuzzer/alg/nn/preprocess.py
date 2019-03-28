import string
import torch


all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)


def letter_to_index(letter):
    return all_letters.find(letter)


def letter_to_tensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letter_to_index(letter)] = 1
    return tensor


def line_to_tensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letter_to_index(letter)] = 1
    return tensor
