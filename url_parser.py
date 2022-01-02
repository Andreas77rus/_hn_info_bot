from bs4 import BeautifulSoup
import requests


class HNParser:
	def __init__(self, url):
		self.url = url
		self.request = requests.get(url)
		self.themes = None
		self.soup = BeautifulSoup(self.request.text, 'html.parser')

	def get_titles(self):
		self.themes = self.soup.find_all('td', class_='title')
		list_of_titles = []

		for theme in self.themes:
			clear_themes = theme.find('a', {'class': 'titlelink'})

			if clear_themes is not None:
				list_of_titles.append(clear_themes.text)

		return list_of_titles

	def get_links(self):
		list_of_link = []

		links = self.soup.find_all('a', {'class': 'titlelink'})
		for link in links:
			if link is not None:
				list_of_link.append(link['href'])

		return list_of_link


