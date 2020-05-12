import random


LIST_COUNTRIES = ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'GreatBritain', 'Portugal', 'Austria']
COUNTRIES_NUMBER = len(LIST_COUNTRIES)
LINKS_NUMBER = 15


class Country(object):

    def __init__(self, id, name, is_infected):

        if not isinstance(id, int):
            raise TypeError('id should be int')
        if not isinstance(name, str):
            raise TypeError('name should be str')
        if not isinstance(is_infected, bool):
            raise TypeError('is_infected should be bool')
        if LIST_COUNTRIES.count(name) == 0:
            raise IndexError('wrong county name')

        self.id = id
        self.name = name
        self.infected = is_infected


class EuropeVirus(object):

    def __init__(self):
        self.countries = [Country(id, country, False) for id, country in enumerate(LIST_COUNTRIES)]
        self.infected_countries = set()
        self.map = {i: set() for i in LIST_COUNTRIES}

    @staticmethod
    def get_id(country_name):
        if LIST_COUNTRIES.count(country_name) == 0:
            raise IndexError('this country is not available')
        return LIST_COUNTRIES.index(country_name)

    def infect_country(self, country_name):
        country_id = self.get_id(country_name)
        self.countries[country_id].infected = True
        self.infected_countries.add(Country(country_id, country_name, True))
        return country_id

    def get_all_info(self):
        return self.countries

    def get_info(self, country):
        if not isinstance(country, Country):
            raise TypeError('get_info only for Country type elements')

        id = self.get_id(country)
        if self.countries[id].infected:
            return 'infected'
        else:
            return 'absolutely healthy'

    def spread(self, country_from):
        if not isinstance(country_from, Country):
            raise TypeError('spread only for Country type elements')

        for country_to in self.map[country_from.name]:
            self.countries[country_to.id].infected = True
            self.infected_countries.add(country_to)

    def go_days(self, time):
        if not isinstance(time, int):
            raise TypeError('time should be int')
        if time < 0:
            raise ValueError('time should be above zero')

        while time > 0:
            started = []
            for country in self.infected_countries:
                started.append(country)
            for country in started:
                self.spread(country)
            time -= 1

    def get_random_country(self):
        return random.choice(self.countries)

    def make_map(self):
        for i in range(LINKS_NUMBER):
            country_from = self.get_random_country()
            country_to = self.get_random_country()
            self.map[country_from.name].add(country_to)

    def get_links(self, country_name):
        if LIST_COUNTRIES.count(country_name) == 0:
            raise IndexError('wrong county name')
        return str(list(country.name for country in self.map[country_name]))
