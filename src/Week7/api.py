from typing import List, Type

import requests
import collections

Podcast = collections.namedtuple('Podcast', 'category, id, url, title, description')


def search_podcast(keyword: str) -> List[Podcast]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'
    resp = requests.get(url)
    resp.raise_for_status()

    result = resp.json()
    episodes = []

    for record in result.get('results'):
        if record['category'] == 'Episode':
            episodes.append(Podcast(**record))
        else:
            continue

        # episodes.append(Podcast(**record)) if record['category'] == 'Episode' else 0
    return episodes
