from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_review(model_path, prompt, max_length=500):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained(model_path)

    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, do_sample=True, top_p=0.95, top_k=60)

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Replace with the name of the reviewer whose model you want to use
reviewer_name = "Sam"
model_path = f"models/{reviewer_name}_gpt2"

# Replace with the movie prompt you want to generate a review for
movie_prompt = "Please write a detailed review of the movie 'The Lion King'"

# Generate a review
generated_review = generate_review(model_path, movie_prompt)
print(f"{reviewer_name}'s generated review: {generated_review}")
