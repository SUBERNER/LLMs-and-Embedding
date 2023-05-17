#embeddingConversion.py
#used for moduals and function for embedding text
#for multiple LLMs


#imports
from transformers import GPT2Model, GPT2Tokenizer, BertModel, BertTokenizer

#LMM model variables


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
    embeddedText = output.last_hidden_state.mean(dim = 1).squeeze(0)
    return embeddedText
    #"dim" specifies the deminsions along which a specific operation should be applied to
    #"squeeze" removes demensions/removes number of dimesnions from tensor