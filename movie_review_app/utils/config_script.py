from transformers import GPT2Config

reviewer_name = "Sam"  # Replace with the name of the reviewer whose model you want to save the configuration for
model_path = f"models/{reviewer_name}_gpt2"

config = GPT2Config.from_pretrained("gpt2")
config.save_pretrained(model_path)
