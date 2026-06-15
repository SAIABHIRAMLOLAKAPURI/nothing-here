import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import joblib
import os

class IntentTrainer:
    def __init__(self, data_path="jarvis/data/intents.csv", model_path="jarvis/data/intent_model.pkl"):
        self.data_path = data_path
        self.model_path = model_path

    def train(self):
        if not os.path.exists(self.data_path):
            print(f"Error: {self.data_path} not found.")
            return

        df = pd.read_csv(self.data_path)

        # Simple but effective pipeline for text classification
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
            ('clf', LinearSVC(C=1.0, random_state=42))
        ])

        pipeline.fit(df['text'], df['intent'])

        # Save the model
        joblib.dump(pipeline, self.model_path)
        print(f"Model trained and saved to {self.model_path}")

        accuracy = pipeline.score(df['text'], df['intent'])
        print(f"Training Accuracy: {accuracy * 100:.2f}%")
        return accuracy

if __name__ == "__main__":
    trainer = IntentTrainer()
    trainer.train()
