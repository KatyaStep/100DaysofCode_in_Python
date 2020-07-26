"""
TODO1: Parse the movie_metadata.csv, using csv.DictReader - DONE
TODO2: Only consider directors with a minimum of 4 movies, otherwise you get misrepresentative data.
TODO3: Take movies of year >= 1960.
TODO4: Print the top 20 highest rated directors with their movies ordered desc on rating.
"""
import csv
from collections import defaultdict, namedtuple, Counter

movie_csv = 'movies.csv'
Min_movies = 4  # director with minimum of 4 movies
Min_year = 1960  # movies of year >= 1960
top_movies_number = 20  # top of 20 highest rated movies

Movie = namedtuple('Movie', 'title, year, score')


def get_movies_by_director(data=movie_csv):
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director = row['director_name']
                title = row['movie_title']
                year = int(row['title_year'])
                score = float(row['imdb_score'])

                m = Movie(title=title, year=year, score=score)

                directors[director].append(m)
            except ValueError:
                continue

    return directors


def get_average_score(directors):
    """Filter directors with < MIN_MOVIES and calculate average score"""
    filtered_director = defaultdict(list)

    for director, movies in directors.items():
        sum_score = 0
        # avg_score = 0
        if len(movies) >= Min_movies:
            for movie in movies:
                if movie[1] >= Min_year:
                    sum_score += movie[2]
            avg_score = round(sum_score / len(movies), 1)
            filtered_director[director].append(avg_score)
    return filtered_director


def print_movies(sorted_directors, all_movies):
    count = 1
    for sort_director, score in sorted_directors.items():
        if count <= top_movies_number:
            print(f"{count}: {sort_director}, {score}", end="\n")
            print("--------------------------")
            if sort_director in all_movies:
                for movie in all_movies[sort_director]:
                    print(f'Title: {movie[0]},year: {movie[1]}, imdb: {movie[2]}', end="\n")
            print()
        count += 1


def main():
    movies = get_movies_by_director()
    sorted_directors = get_average_score(movies)
    print_movies(sorted_directors, movies)


if __name__ == '__main__':
    main()
