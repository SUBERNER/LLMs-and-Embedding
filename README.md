# LLMs-and-Embedding
A program that evaluates how well a language model performs at generating useful embeddings. It will be provided with sample text data along with the pre-trained model used to generate the embeddings for this data.

# USING THE PROGRAM:
1. Select whether you want to give the text to program by typing it in directly or by typing the file location that stores the text.

2. Select a CSV file to store the embedded word data. Similar to part of the last step, type the file location of the CSV file.

3. Embedding the words and the words themselfs will then be generated and stored inside of the CVS file. The first column is the word in its normal form. The second column is the embedding data provided by GPT2. The second to last column is the embedding data provided by BERT. The last column is used to show the similarity between the embedding of each LLM.
