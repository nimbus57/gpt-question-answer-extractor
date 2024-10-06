import json

# input_text = "The cat sat on the mat. It looked up at the sun. Birds chirped in the trees."
# input_text = "The cat sat on the mat. It looked up at the sun. Birds chirped in the trees. The cat looked at the birds."
# input_text = "The cat sat on the mat. It looked up at the sun. Birds chirped in the trees. The cat looked at the birds. The birds chirped at the cat."
# input_text = "The cat sat on the mat. It looked up at the sun. Birds chirped in the trees. The cat looked at the birds. The birds chirped at the cat. The cat sat in the trees."
# input_text = "The cat sat on the mat. It looked up at the sun. Birds chirped in the trees. The cat looked at the birds. The birds chirped at the cat. The cat sat in the trees. The sun looked down at the cat."


def get_data(input_text):
    input_text_lower_case = input_text.lower()
    input_text_split_on_space = input_text_lower_case.split(' ')
    pairwise_words = list(zip(input_text_split_on_space, input_text_split_on_space[1:]))
    scores = {}

    for (word1, word2) in pairwise_words:
    # check to see if word1 has been added
        if word1 in scores:
            if word2 in scores[word1]:
                print('increment', word1,word2)
                scores[word1][word2] += 1
            else:
                print('initialize 2', word1, word2)
                scores[word1][word2] = 1
        else:
            print('initialize 1', word1, word2)
            scores[word1] = {}
            scores[word1][word2] = 1
    return scores
