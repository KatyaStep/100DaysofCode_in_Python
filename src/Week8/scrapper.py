import requests
import bs4
import pprint

url = "https://pybit.es/pages/projects.html"


def pull_site():
    site_page = requests.get(url)
    site_page.raise_for_status()
    return site_page


def scrape(site):
    header_list = []
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.projectHeader')

    for header in html_header_list:
        header_list.append(header.text)

    for headers in header_list:
        print(headers)


if __name__ == '__main__':
    site = pull_site()
    scrape(site)
