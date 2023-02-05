import spacy

nlp = spacy.load("en_core_web_sm")

word1 = nlp("dog")
word2 = nlp("bone")
word3 = nlp("bear")

print(f"Similarity between {word1} and {word2} = {word1.similarity(word2)}")
print(f"Similarity between {word3} and {word2} = {word3.similarity(word2)}")
print(f"Similarity between {word3} and {word1} = {word3.similarity(word1)}")

print("======================||=================================")

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text,token2.text,token1.similarity(token2)}")

print("======================||=================================")

sentence_to_compare = "Why is my cat on the car"
print(f"We are comparing \"{sentence_to_compare}\" to other sentences in the list")

sentences = ["Where did my dog go",
             "Hello there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

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

# Similarity between dog and bone = 0.25421421644290154
# Similarity between bear and bone = 0.12584526101060983
# Similarity between bear and dog = 0.2940996130324144
# ======================||=================================
# ('cat', 'cat', 1.0)
# ('cat', 'apple', 0.20368057489395142)
# ('cat', 'monkey', 0.5929930210113525)
# ('cat', 'banana', 0.2235882729291916)
# ('apple', 'cat', 0.20368057489395142)
# ('apple', 'apple', 1.0)
# ('apple', 'monkey', 0.2342509925365448)
# ('apple', 'banana', 0.6646700501441956)
# ('monkey', 'cat', 0.5929930210113525)
# ('monkey', 'apple', 0.2342509925365448)
# ('monkey', 'monkey', 1.0)
# ('monkey', 'banana', 0.4041501581668854)
# ('banana', 'cat', 0.2235882729291916)
# ('banana', 'apple', 0.6646700501441956)
# ('banana', 'monkey', 0.4041501581668854)
# ('banana', 'banana', 1.0)
# ======================||=================================
# We are comparing "Why is my cat on the car" to other sentences in the list
# Where did my dog go -  0.6085941922436378
# Hello there is my car -  0.8259162920501877
# I've lost my car in my car -  0.6787540461994952
# I'd like my boat back -  0.562494104588661
# I will name my dog Diana -  0.6491444739190607