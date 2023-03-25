import os
import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

# Read the restructured_movie_reviews.csv file
data = pd.read_csv("mncdata.csv")

# Extract the unique reviewer names
reviewers = data['Name'].unique()

# Function to create a dataset for training
def create_dataset(file_path, tokenizer):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=128
    )
    return dataset

# Function to fine-tune the GPT-2 model for a specific reviewer
def fine_tune_gpt2(reviewer, file_path, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the tokenizer, model, and configuration
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    config = GPT2Config.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2", config=config)

    # Create the dataset
    dataset = create_dataset(file_path, tokenizer)

    # Define the data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=2,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        prediction_loss_only=True,
        logging_steps=100,
        logging_dir=f"{output_dir}/logs",
    )

    # Initialize the Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )

    # Train the model
    trainer.train()
    
    # Save the model
    trainer.save_model(output_dir)

    # Save the configuration file
    config.save_pretrained(output_dir)

# Fine-tune GPT-2 for each reviewer
for reviewer in reviewers:
    print(f"Fine-tuning GPT-2 for {reviewer}...")
    reviews_file = f"{reviewer}_reviews.txt"
    output_dir = f"models/{reviewer}_gpt2"
    fine_tune_gpt2(reviewer, reviews_file, output_dir)
    print(f"Finished fine-tuning GPT-2 for {reviewer}")
