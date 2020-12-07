import api
import webbrowser


def main():
    keyword = input('Enter a keyword for searching: ')
    result = api.search_podcast(keyword)

    for index, element in enumerate(result):
        print(f'{index+1}.{element.title}')

    index_of_episode = int(input('Do you want to see any of these episodes? Type a number: '))
    url_of_episode = result[index_of_episode-1].url

    webbrowser.open(f'https://talkpython.fm{url_of_episode}', new=2)


if __name__ == '__main__':
    main()
