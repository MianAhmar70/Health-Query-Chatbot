from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch

class HealthChatbotModel:
    def __init__(self):
        
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.questions = []
        self.answers = []
        self.question_embeddings = None

    def load_data(self, filepath):
        
        data = pd.read_csv(filepath)
        self.questions = data['short_question'].fillna("").tolist()
        self.answers = data['short_answer'].fillna("").tolist()

       
        self.question_embeddings = self.model.encode(self.questions, convert_to_tensor=True)

    def get_answer(self, query):
        
        query_embedding = self.model.encode(query, convert_to_tensor=True)

       
        similarities = util.cos_sim(query_embedding, self.question_embeddings)

        
        best_match_index = torch.argmax(similarities).item()

        return self.answers[best_match_index]

