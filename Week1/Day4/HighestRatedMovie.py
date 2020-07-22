import csv
from collections import defaultdict, namedtuple

movie_csv = 'movies.csv'
Movie = namedtuple('Movie', 'title, year, score')


def get_movies_by_director(data):
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

    print(directors)

get_movies_by_director(movie_csv)