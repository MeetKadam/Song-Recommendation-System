import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Load the dataset
data = pd.read_csv('data.csv')

# Filter for songs released after 2000
data = data[data['year'] > 2000]

# Select the features you want to use for similarity
features = data[['valence', 'acousticness', 'danceability', 'duration_ms', 
                 'energy', 'instrumentalness', 'liveness', 
                 'loudness', 'speechiness', 'tempo']]

# Normalize the features
features = (features - features.mean()) / features.std()

# Function to compute similarity only for a given song, without computing the full matrix
def get_similar_songs(song_name, num_songs=5):
    try:
        # Get the index of the song
        song_idx = data[data['name'] == song_name].index[0]

        # Compute cosine similarity between the selected song and all other songs
        song_features = features.iloc[song_idx].values.reshape(1, -1)
        similarities = cosine_similarity(song_features, features).flatten()

        # Get indices of the most similar songs, excluding the first one (itself)
        similar_indices = similarities.argsort()[-(num_songs+1):-1][::-1]
        
        # Retrieve the song names and artists, resetting the index
        similar_songs = data.iloc[similar_indices][['name', 'artists']].reset_index(drop=True)
        
        # Add a column for numbering starting from 1
        similar_songs.index += 1  # Start index from 1
        
        # Check if there are similar songs found
        if similar_songs.empty:
            return f"No similar songs found for '{song_name}'."
        
        # Formatting the output
        formatted_output = "Top recommended songs related to: '{}'\n".format(song_name)
        formatted_output += "{:<5} {:<50} {}\n".format("No.", "Song Name", "Artists")
        formatted_output += "-" * 70 + "\n"
        for i in range(len(similar_songs)):
            formatted_output += "{:<5} {:<50} {}\n".format(i + 1, similar_songs['name'].iloc[i], similar_songs['artists'].iloc[i])
        
        return formatted_output

    except IndexError:
        return f"Song '{song_name}' not found in the dataset."

# Example usage
print(get_similar_songs('Sweater Weather'))  # Replace with an actual song title from your dataset
