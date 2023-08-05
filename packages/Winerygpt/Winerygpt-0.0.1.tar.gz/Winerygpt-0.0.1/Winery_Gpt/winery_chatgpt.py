# import libraries
import logging
import os
import warnings
from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma

# Suppress warnings
warnings.filterwarnings('ignore')


class AskGPT:
    def __init__(self,key,txtfile):

        self.model = None

        # Set OpenAI API key
        api_key = key
        os.environ['OPENAI_API_KEY'] = key

        loader = TextLoader(txtfile, encoding='utf8')

        docs = loader.load()

        # Split documents into chunks for efficient processing
        char_text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        doc_texts = char_text_splitter.split_documents(docs)

        # Embed text chunks using OpenAI embeddings
        openAI_embeddings = OpenAIEmbeddings(openai_api_key=api_key)
        vStore = Chroma.from_documents(doc_texts, openAI_embeddings)

        # Create a RetrievalQA model for question-answering
        self.model = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff",
                                                 retriever=vStore.as_retriever(search_kwargs={"k": 1}))

    def generate_response(self, question):
        try:
            ans = self.model.run(question)
            return ans
        except Exception as e:
            # print(f"Error: {e}")
            return "I'm sorry, I don't know the answer to that."
