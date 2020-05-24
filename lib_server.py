from macros_server import *
import random


class Country(object):

    def __init__(self, id, name, is_infected):

        if not isinstance(id, int):
            raise TypeError(TYPE_ERROR_MSG['id'])
        if not isinstance(name, str):
            raise TypeError(TYPE_ERROR_MSG['name'])
        if not isinstance(is_infected, bool):
            raise TypeError(TYPE_ERROR_MSG['is_infected'])
        if LIST_COUNTRIES.count(name) == 0:
            raise IndexError(INDEX_ERROR_MSG)

        self.id = id
        self.name = name
        self.infected = is_infected

    def __str__(self):
        return f'{str(self.name)} (ID: {str(self.id)} + ) is infected: {str(self.infected)}'


class EuropeVirus(object):

    def __init__(self):
        self.countries = [Country(id, country, False) for id, country in enumerate(LIST_COUNTRIES)]
        self.infected_countries = set()
        self.map = {i: set() for i in LIST_COUNTRIES}

    @staticmethod
    def get_id(country_name):
        if LIST_COUNTRIES.count(country_name) == 0:
            raise IndexError(INDEX_ERROR_MSG)
        return LIST_COUNTRIES.index(country_name)

    def infect_country(self, country_name):
        country_id = self.get_id(country_name)
        self.countries[country_id].infected = True
        self.infected_countries.add(self.countries[country_id])
        return country_id

    def get_all_info(self):
        return [str(country) for country in self.countries]

    def get_info(self, country):
        if not isinstance(country, str):
            raise TypeError(TYPE_ERROR_MSG['get_info'])

        id = self.get_id(country)
        if self.countries[id].infected:
            return INFECTED_MSG
        else:
            return NOT_INFECTED_MSG

    def spread(self, country_from):
        if not isinstance(country_from, Country):
            raise TypeError(TYPE_ERROR_MSG['spread'])

        for country_to in self.map[country_from.name]:
            self.countries[country_to.id].infected = True
            self.infected_countries.add(country_to)

    def go_days(self, time):
        if not isinstance(time, int):
            raise TypeError(TYPE_ERROR_MSG['time'])
        if time < 0:
            raise ValueError(VALUE_ERROR_MSG)

        while time > 0:
            started = [country for country in self.infected_countries]
            for country in started:
                self.spread(country)
            time -= 1

    def get_random_country(self):
        return random.choice(self.countries)

    def make_map(self):
        for i in range(LINKS_NUMBER):
            country_from = self.get_random_country()
            country_to = self.get_random_country()
            if country_to != country_from:
                self.map[country_from.name].add(country_to)

    def get_links(self, country_name):
        if LIST_COUNTRIES.count(country_name) == 0:
            raise IndexError(INDEX_ERROR_MSG)
        return str(list(country.name for country in self.map[country_name]))
