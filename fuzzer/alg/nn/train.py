import time
import math

import sys

sys.path.append('/home/ltbringer/anaconda3/envs/fastest/lib/python3.5/site-packages')
print(sys.path)

import torch
import random

from torch import nn
from fuzzer.alg.nn.rnn import rnn
from fuzzer.alg.nn.process import all_categories, line_to_tensor
from fuzzer.alg.nn.predict import category_from_output


learning_rate = 0.05
criterion = nn.NLLLoss()


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


def __train_network(category_tensor, line_tensor):
    hidden = rnn.init_hidden()

    rnn.zero_grad()
    output = None
    for i in range(line_tensor.size()[0]):
        output, hidden = rnn(line_tensor[i], hidden)

    loss = criterion(output, category_tensor)
    loss.backward()

    # Add parameters' gradients to their values, multiplied by learning rate
    for p in rnn.parameters():
        p.data.add_(-learning_rate, p.grad.data)

    return output, loss.item()


def random_choice(l):
    return l[random.randint(0, len(l) - 1)]


def random_training_example(input_value, output_value):
    category = random_choice(all_categories)
    category_tensor = torch.tensor([all_categories.index(output_value)], dtype=torch.long)
    line_tensor = line_to_tensor(input_value)
    return category, category_tensor, line_tensor


def train(epochs, i, input_value, output_value):
    print_every = 100
    start = time.time()
    category, category_tensor, line_tensor = random_training_example(input_value, output_value)
    output, loss = __train_network(category_tensor, line_tensor)

    # Print iter number, loss, name and guess
    if i % print_every == 0:
        guess, guess_i = category_from_output(output)
        correct = '✓' if guess == category else '✗ (%s)' % category
        print('%d %d%% (%s) loss=%.4f input=(%s) output=(%s) result=%s' %
              (i, i / epochs * 100, time_since(start), loss, input_value, guess, correct)
              )

    return loss
