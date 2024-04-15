"""Identify the most popular movie ratings based on data in two CSV files."""
from argparse import ArgumentParser
import pandas as pd
import sys

def best_movies(movies_file, ratings_file):
    """This function reads each csv file into its own data frame. 

    Args:
        movies_file (str): The path to the CSV file containing the movie data. 
        ratings_file (str): The path to the CSV file containing the rating data. 

    Returns:
       panda.series : a sorted version of the series of average ratings by appending the sort values function to the variable 
    """
    movies_df = pd.read_csv(movies_file)
    ratings_df = pd.read_csv(ratings_file)
    
    merged_df = pd.merge(ratings_df, movies_df, left_on ='item id', right_on ='movie id', how ='inner')
    
    average_ratings = merged_df.groupby('movie title')['rating'].mean()
    average_ratings.dropna(inplace=True) 
    
    sorted_ratings = average_ratings.sort_values(ascending=False)

    return sorted_ratings 


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())
