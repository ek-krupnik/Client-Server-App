PORT = 8000

APP_NAME = 'Plague_Inc_Europe'

LIST_COUNTRIES = ['Germany', 'France', 'Italy', 'Spain', 'Poland', 'GreatBritain', 'Portugal', 'Austria']
COUNTRIES_NUMBER = len(LIST_COUNTRIES)
LINKS_NUMBER = 15

INDEX_ERROR_MSG = 'Wrong country name'
TYPE_ERROR_MSG = {'id': 'Id should be int',
                  'name': 'Name should be str',
                  'is_infected': 'is_infected should be bool',
                  'get_info': 'Get_info only for Country type elements',
                  'spread': 'spread only for Country type elements',
                  'time': 'time should be int',
                  }
VALUE_ERROR_MSG = 'time should be above zero'

INFECTED_MSG = 'infected'
NOT_INFECTED_MSG = 'absolutely healthy'

HANDLE_INFECT = '/infect'
HANDLE_INFO = '/get_info'
HANDLE_ALL_INFO = '/get_all_info'
HANDLE_GO_DAYS = '/go_days'
HANDLE_MAKE_MAP = '/make_map'
HANDLE_GET_LINKS = '/get_links'
