
# Song Recommendation System

This project is a **content-based song recommendation system** that uses machine learning techniques to suggest songs based on the attributes of previously liked tracks. By analyzing song features such as acousticness, danceability, energy, and more, the system generates personalized recommendations.

## Features

- **Content-Based Filtering**: Recommends songs based on the similarity of song attributes to the user's previously liked songs.
- **Machine Learning Model**: Utilizes cosine similarity or other distance measures to compute similarity between songs.
- **Feature Extraction**: Considers features like danceability, energy, loudness, tempo, and more to understand the song's characteristics.
- **Dataset**: Includes song metadata with features like track name, artist, album, duration, and numerical features like valence, energy, etc.

## Tech Stack

- **Python**: For building the recommendation system.
- **Pandas & NumPy**: For data processing and manipulation.
- **Scikit-Learn**: For implementing machine learning algorithms.
- **Jupyter Notebook/Google Colab**: For running and testing the code.
  
## Dataset

The dataset used for this system contains various features of songs, including:

- `track_name`
- `artists`
- `album_name`
- `duration_ms`
- `danceability`
- `energy`
- `valence`
- `tempo`
- `loudness`
- `acousticness`
- `speechiness`
- `popularity`
  
### Example of dataset columns:
```
track_name, artists, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, popularity
```

## How it Works

1. **Data Preprocessing**: The system loads and cleans the dataset, normalizing the features to ensure consistent values.
2. **Feature Selection**: The relevant features such as `danceability`, `energy`, `tempo`, etc., are selected for similarity analysis.
3. **Cosine Similarity Calculation**: The system calculates the cosine similarity between songs to recommend tracks that are most similar to the user's preferred songs.
4. **Recommendation Generation**: Based on the similarity scores, the top N songs are recommended to the user.


## Usage

1. **Input Song**: Provide a song or a list of songs you like, and the system will recommend similar tracks based on their features.
2. **Recommendation Output**: The system outputs a list of top recommended songs ranked by similarity.

## Example

```bash
Input Song: "Blinding Lights" by The Weeknd
Recommended Songs:
1. "Don't Start Now" by Dua Lipa
2. "Levitating" by Dua Lipa
3. "Say So" by Doja Cat
```

