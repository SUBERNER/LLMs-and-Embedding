#embeddingConversion.py
#used for moduals and function for embedding text
#for multiple LLMs


#imports
try:
    from transformers import GPT2Model, GPT2Tokenizer, BertModel, BertTokenizer
    from sklearn.metrics.pairwise import cosine_similarity
except ImportError as e:
    print(e)
   
    
#varibles
model = None
tokenizer = None


#Embedds the text given by the user
def EmbeddingText(modelUsage: str, word):
    #"modelUsage" should be anything that can go into "from_pretrained"
    #"word" holds what is being embedded
    
    #LMM model variables
    if (modelUsage == "bert-base-uncased"):
        model = BertModel.from_pretrained(modelUsage)
        tokenizer = BertTokenizer.from_pretrained(modelUsage)
    elif (modelUsage == "gpt2"):
        model = GPT2Model.from_pretrained(modelUsage)
        tokenizer = GPT2Tokenizer.from_pretrained(modelUsage)
    
    encodedText = tokenizer.encode(word, add_special_tokens = False, return_tensors = "pt")
        #converts user input to embedded format and stores in temporary list
        #'pt' is being used, DUE NOT CHANGE unless you change the tensors being used with this program
    
    output = model(encodedText)
    embeddedText = output.last_hidden_state.mean(dim = 1).squeeze(0).detach().numpy()
    
    return embeddedText
    #"dim" specifies the deminsions along which a specific operation should be applied to
    #"squeeze" removes demensions/removes number of dimesnions from tensor
    
    
#compares the embeddings
#the result is the cosine similarity between each embedding
def CompareEmbeddings(embeddingGPT, embeddingBert):
    similarity = cosine_similarity(embeddingGPT.reshape(1, -1), embeddingBert.reshape(1, -1)) #compares both embeddings and finds what is similar
    return similarity