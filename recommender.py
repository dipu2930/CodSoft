# TASK 3: RECOMMENDATION SYSTEM

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_recommendation_system():
    # --- 1. Create a Sample Dataset ---
    # In a real-world scenario, this data would come from a large database.
    data = {
        'title': [
            'The Dark Knight', 'Inception', 'Interstellar', 'The Prestige',
            'The Avengers', 'Iron Man', 'Guardians of the Galaxy',
            'The Godfather', 'Goodfellas', 'Pulp Fiction',
            'Forrest Gump', 'The Shawshank Redemption', 'The Green Mile'
        ],
        'genre': [
            'Action Sci-Fi Thriller', 'Action Sci-Fi Thriller', 'Sci-Fi Drama Adventure', 'Mystery Thriller Drama',
            'Action Sci-Fi Adventure', 'Action Sci-Fi Adventure', 'Action Sci-Fi Comedy',
            'Crime Drama', 'Crime Drama Biography', 'Crime Drama Thriller',
            'Drama Romance Comedy', 'Drama', 'Drama Fantasy Crime'
        ]
    }
    df = pd.DataFrame(data)

    # --- 2. Feature Extraction (Convert Genres to Numbers) ---
    # We use TF-IDF to vectorize the genre strings. This turns text into numerical data
    # that we can use for calculations.
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['genre'])

    # --- 3. Calculate Similarity ---
    # We use cosine similarity to find how similar each movie is to every other movie.
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # --- 4. The Recommendation Function ---
    def get_recommendations(title, cosine_sim=cosine_sim, df=df):
        # Get the index of the movie that matches the title
        try:
            idx = df[df['title'] == title].index[0]
        except IndexError:
            return "Movie not found in the database."

        # Get the similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 5 most similar movies
        sim_scores = sim_scores[1:6]  # Exclude the movie itself

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]

        # Return the top 5 most similar movies
        return df['title'].iloc[movie_indices]

    return get_recommendations

# --- Main execution block ---
if __name__ == "__main__":
    recommender = create_recommendation_system()
    
    # --- Pick a movie the "user" has watched ---
    movie_watched = 'The Green Mile'
    
    print(f"Because you watched '{movie_watched}', you might also like:")
    print("-" * 50)
    
    recommendations = recommender(movie_watched)
    
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        for i, movie in enumerate(recommendations):
            print(f"{i+1}. {movie}")