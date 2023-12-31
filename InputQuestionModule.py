from torch import nn


class InputQuestionModule(nn.Module):

    def __init__(self, vocab_size, embedding_dim=50, padding_idx=0, num_gru_layers=1):
        super().__init__()

        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.padding_idx = padding_idx
        self.num_gru_layers = num_gru_layers
        # self.story_rnn = nn.GRU(
        #     input_size=embedding_dim,
        #     hidden_size=embedding_dim,
        #     num_layers=num_gru_layers,
        #     batch_first=True
        # )
        # self.question_rnn = nn.GRU(
        #     input_size=embedding_dim,
        #     hidden_size=embedding_dim,
        #     num_layers=num_gru_layers,
        #     batch_first=True
        # )

        self.mha = nn.MultiheadAttention(
            embed_dim=embedding_dim,
            batch_first=True,
            num_heads=5
        )

        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim, padding_idx=padding_idx)

    def forward(self, story, question):

        story = self.embedding(story)
        question = self.embedding(question)

        embedded_story = self.mha(story, story, story)[0]
        embedded_question = self.mha(question, question, question)[0]
        # inped_story = self.story_rnn(self.embedding(story))[0]
        # inped_question = self.question_rnn(self.embedding(question))[0]

        return embedded_story, embedded_question