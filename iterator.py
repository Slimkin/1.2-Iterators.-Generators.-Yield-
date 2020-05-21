import wikipedia
import json


class CountriesWikiLink:

    def __init__(self, datafile_path, result_path):
        with open(datafile_path, encoding='utf8') as df:
            file_data = json.load(df)
        self.result_path = result_path
        self.countries = [country["name"]["official"] for country in file_data]
        self.start = -1
        self.end = len(self.countries)    

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        
        country = self.countries[self.start]
        try:
            country_page = wikipedia.page(country)
        except wikipedia.WikipediaException:
            country_page = wikipedia.page(f'{country} country')

        with open(self.result_path, 'a', encoding='utf8') as r:
            r.write(f'{country} - {country_page.url}\n')

        return country, country_page.url


if __name__ == "__main__":
    for item in CountriesWikiLink('countries.json', 'result.txt'):
        print(item)