# semantic_similarity
using spacy library for NLP

# Similarities between cat,monkey and banana:

# -- First -- Cat and monkey have quite significant similarity as they are both animals and model recognises that
# --Second -- Banana and monkey have high correlation as monkeys eat bananas and model is recognising that
# --Third -- Cat and banana unlike monkey and banana don't have much similarities,so it is interesting that model has been trined to recognise that

# In my example I run the program to confirm similarity between dog,bone and bear;

# -- First-- Dog and bone have low correlation even though in reality dogs like to eat bones:
# --Second -- Bear and bone have very low similarity that is quite expected
# --Third-- Bear and dog don't have high similarity even though they are both aniimals which suggests that the model is not showing consistent results when we change input words, hence needs to be trained
    # Similarity between dog and bone = 0.25421421644290154
    # Similarity between bear and bone = 0.12584526101060983
    # Similarity between bear and dog = 0.2940996130324144


# difference between "en_core_web_sm" and en_core_web_md:
    # When you calculate the similarity between two pieces of text, 
    # the similarity method uses the word vectors to compare the meaning and context of each word in the texts. 
    # However, if the model you're using doesn't have word vectors, it will instead use the tagger, parser, and NER to judge similarity. 
    # These features capture some aspects of meaning and context, but they're less sophisticated than word vectors, so the similarity score may not be as accurate.
# I ve noticed in case of my words dog, bone and bear corellation was better: 
    # Similarity between dog and bone = 0.7336330071317306
    # Similarity between bear and bone = 0.4585049476135905
    # Similarity between bear and dog = 0.5030567204041406
# In case with comparing sentences the result are following.The results are not consistent this model was not supposed to be used to compare similarity between bigger data sets.
    # Where did my dog go -  0.4313613354785292
    # Hello there is my car -  0.5985130180792348
    # I've lost my car in my car -  0.5480285305981948
    # I'd like my boat back -  0.3007498749175949
    # I will name my dog Diana -  0.3904074922670841   
