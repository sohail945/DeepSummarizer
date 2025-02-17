from transformers import AutoModelForCausalLM, AutoTokenizer

# Define model name
model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

# Download model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("Download complete!")
