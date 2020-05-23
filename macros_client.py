from common_macros import *

HOST = 'localhost'

START = 'start the game by infecting the country'
GET_INFO = 'get information about status country / all countries'
GET_LINKS = 'showcase the links between countries'
GO_DAY = 'rewind for a few days while the virus is spreading'
HELP = 'get information about possible commands'
EXIT = 'quit game'

EXIT_MSG = 'Are you sure you want to exit? (Y/N)\n----------> '
ERROR_MSG = 'Incorrect input. Let\'s try again!\n'
ASK_COUNTRY_MSG = 'Please, write country name here:\n----------> '
PARTICULAR_MSG = 'Do you want to get info about particular country? (Y/N)\n----------> '
ASK_DAYS_MSG = 'Please, write number of days here:\n----------> '
ASK_ACTION_MSG = 'Enter action:\n----------> '

COMMAND_DESCRIPTIONS = {'start': START, 'get info': GET_INFO, 'get links': GET_LINKS, 'go day': GO_DAY,
                        'help': HELP, 'exit': EXIT}

POSSIBLE_COUNTRIES_MSG = 'Possible countries : '
UNKNOWN_COUNTRY_MSG = 'Unknown command: '
DAYS_LATER_MSG = 'day(s) later ...\n'


def get_infected_msg(country, country_id):
    return f'{country} was infected (ID: {country_id})'


def get_request_str(main_args):
    return f'http://{main_args.host}:{main_args.port}'

