import torch
import torch.nn as nn


class RNN(nn.Module):
    # https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size

        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)
        self.learning_rate = 0.005
        criterion = nn.NLLLoss()

    def forward(self, input_, hidden):
        combined = torch.cat((input_, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def init_hidden(self):
        return torch.zeros(1, self.hidden_size)

    def train_network(self, category_tensor, line_tensor):
        hidden = self.initHidden()

        self.zero_grad()
        output = None
        for i in range(line_tensor.size()[0]):
            output, hidden = self.rnn(line_tensor[i], hidden)

        loss = self.criterion(output, category_tensor)
        loss.backward()

        # Add parameters' gradients to their values, multiplied by learning rate
        for p in self.rnn.parameters():
            p.data.add_(-self.learning_rate, p.grad.data)

        return output, loss.item()
