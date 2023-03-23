import pandas as pd

file_path = "Resources/election_data.csv"

vote_df = pd.read_csv(file_path)

print(vote_df.head())
       