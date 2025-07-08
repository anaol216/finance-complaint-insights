#src/eda_preprocessing.py

import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

class ComplaintDataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        
    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        return self.df
    
    def filter_products(self, target_products):
        self.df['Product'] = self.df['Product'].str.strip()
        self.df = self.df[self.df['Product'].isin(target_products)]
        self.df = self.df.dropna(subset=['Consumer complaint narrative'])
        return self.df
    
    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        text = re.sub(r'\bi am writing.*?\.', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def clean_narratives(self):
        self.df['cleaned_narrative'] = self.df['Consumer complaint narrative'].apply(self.clean_text)
        return self.df
    
    def plot_product_distribution(self):
        sns.countplot(y=self.df['Product'], order=self.df['Product'].value_counts().index)
        plt.title("Complaint Count per Product")
        plt.show()
    
    def plot_narrative_lengths(self):
        self.df['narrative_length'] = self.df['Consumer complaint narrative'].astype(str).apply(lambda x: len(x.split()))
        sns.histplot(self.df['narrative_length'], bins=50, kde=True)
        plt.title("Narrative Word Count Distribution")
        plt.show()
    
    def save_filtered_data(self, out_path):
        self.df.to_csv(out_path, index=False)
        print(f"Filtered data saved to {out_path}")
