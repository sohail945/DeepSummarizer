import os
import pandas as pd
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define model path where you have saved your files
model_path = 'D:\\Opensource model\\530ca3e1ad39d440e182c2e4317aa40f012512fa'  # Adjust this path

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Initialize the Hugging Face pipeline
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)

# Path to CSV file
file_path = 'D:\\Opensource model\\Rating.csv'

# Load and preprocess data
df = pd.read_csv(file_path)
df['Mean'] = pd.to_numeric(df['Mean'], errors='coerce')
df['SD'] = pd.to_numeric(df['SD'], errors='coerce')

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Define the prompt with strict output formatting
prompt = f"""
Given the following engagement data:

{df.to_string(index=False)}

Provide ONLY:
1. A direct summary of key insights in one paragraph. Focus on the highest and lowest mean scores and their implications.
2. Clear, actionable recommendations for improving the dimensions with the lowest mean scores.

DO NOT include any headings, reasoning, intermediate thoughts, or any additional text. Only return the final summary and recommendations in a structured format.
"""

# Generate response
response = pipe(prompt, max_length=700, num_return_sequences=1)

# Extract model output and clean it
generated_text = response[0]['generated_text']

# Split the output at </think> to get the relevant portion after it
if '</think>' in generated_text:
    generated_text = generated_text.split('</think>', 1)[1].strip()

# Remove unwanted section labels and extra headings (e.g., "Summary of Key Insights", "Recommendations for Improvement")
clean_output = generated_text.replace("Summary of Key Insights", "").replace("Summary of the Table", "").strip()


# Ensure that only Summary and Recommendations are present by separating them properly
# If there are multiple sections, ensure it's correctly split
sections = clean_output.split('\n\n', 1)

# Extract clean summary and recommendations
summary = sections[0].strip() if len(sections) > 0 else "Summary not generated."
recommendations = sections[1].strip() if len(sections) > 1 else "No recommendations provided."

# Streamlit UI
st.title("Engagement Data Interpretation")

# Display only summary and recommendations, no additional headers or labels
st.subheader("Summary")
st.write(summary)  # Direct paragraph summary

st.subheader("Recommendations for Improvement")
st.write(recommendations)  # Clear, actionable recommendations