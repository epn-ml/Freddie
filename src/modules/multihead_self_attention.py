import torch.nn as nn


class MultiheadSelfAttention(nn.Module):

    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim, num_heads)

    def forward(self, x):
        return self.attn.forward(x, x, x)

