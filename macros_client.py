PORT = 8000
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

LIST_COUNTRIES = ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'GreatBritain', 'Portugal', 'Austria']
COMMAND_DESCRIPTIONS = {'start': START, 'get info': GET_INFO, 'get links': GET_LINKS, 'go day': GO_DAY,
                        'help': HELP, 'exit': EXIT}

POSSIBLE_COUNTRIES_MSG = 'Possible countries : '
UNKNOWN_COUNTRY_MSG = 'Unknown command: '
DAYS_LATER_MSG =  'day(s) later ...\n'

HANDLE_INFECT = '/infect'
HANDLE_INFO = '/get_info'
HANDLE_ALL_INFO = '/get_all_info'
HANDLE_GO_DAYS = '/go_days'
HANDLE_MAKE_MAP = '/make_map'
HANDLE_GET_LINKS = '/get_links'
