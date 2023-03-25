import pandas as pd
import re
import string

# Read the CSV file into a pandas DataFrame
data = pd.read_csv("mncdata.csv")

# Define the clean_text function
def clean_text(text, tokenize=False):
    if not isinstance(text, str):
        return None if not tokenize else []

    # Remove special characters
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Tokenize the text (if needed)
    if tokenize:
        words = text.split()
        return words
    else:
        return text

# Apply the clean_text function to the 'Review' column
data['Cleaned_Review'] = data['Review'].apply(clean_text)

# Apply the clean_text function with tokenize=True to the 'Review' column
data['Tokenized_Review'] = data['Review'].apply(lambda x: clean_text(x, tokenize=True))

# Display the DataFrame
print(data)

reviewers = data['Name'].unique()

for reviewer in reviewers:
    reviewer_data = data[data['Name'] == reviewer]
    reviewer_reviews = "\n".join([review for review in reviewer_data['Cleaned_Review'].tolist() if review is not None])
    
    with open(f"{reviewer}_reviews.txt", "w") as f:
        f.write(reviewer_reviews)
