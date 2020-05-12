import re
import requests
import argparse
import networkx as nx
from matplotlib import pyplot as plt
from macros import *


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8000, type=int)

    return parser


def correct_exit():
    answer = input(EXIT_MSG)
    if answer == 'N':
        pass
    else:
        exit()


def input_error():
    print(ERROR_MSG)


def throw_and_repeat(func, is_necessary=False):
    input_error()
    func(is_necessary)


def is_correct_name(name):
    return name.isalpha()


def is_correct_time(time):
    return time.isdigit()


def get_name():
    print('Possible countries : ', end='')
    print(*LIST_COUNTRIES)
    return input(ASK_COUNTRY_MSG)


def ask_for_country(is_necessary=False):
    user_input = ''
    if is_necessary:
        user_input = get_name()
    else:
        answer = input(PARTICULAR_MSG)
        if answer == 'Y':
            user_input = get_name()
        elif answer == 'N':
            return ''
        else:
            throw_and_repeat(ask_for_country, is_necessary)

    if user_input and is_correct_name(user_input):
        return user_input
    else:
        throw_and_repeat(ask_for_country, is_necessary)


def ask_for_days(is_necessary=True):
    user_input = input(ASK_DAYS_MSG)
    if user_input and is_correct_time(user_input):
        return int(user_input)
    else:
        throw_and_repeat(ask_for_days, is_necessary)


def infect_country(main_args):
    country = ask_for_country(True)
    country_id = requests.post(f'http://{main_args.host}:{main_args.port}/infect', params={'name': country}).text
    print(f'{country} was infected (ID: {country_id})')


def get_info(main_args):
    country = ask_for_country(False)
    if len(country):
        req_function = 'get_info'
    else:
        req_function = 'get_all_info'

    status = requests.get(f'http://{main_args.host}:{main_args.port}/{req_function}', params={'name': country}).text
    print(status)


def go_day(main_args):
    time = ask_for_days()
    num_days = requests.post(f'http://{main_args.host}:{main_args.port}/go_days', params={'time': time}).text
    print(f'{num_days} day(s) later ...\n')


def make_new_map(main_args):
    requests.post(f'http://{main_args.host}:{main_args.port}/make_map')


def draw(maps):
    graph = nx.Graph()
    graph.add_nodes_from(LIST_COUNTRIES)
    for country_from in LIST_COUNTRIES:
        for country_to in maps[country_from]:
            graph.add_edge(country_from, country_to)

    nx.draw(graph, pos=nx.spring_layout(graph), with_labels=True, font_weight='bold', arrows=True)
    plt.show()


def get_links(main_args):
    lst_countries = []
    for country in LIST_COUNTRIES:
        arg_str = requests.get(f'http://{main_args.host}:{main_args.port}/get_links', params={'name': country}).text
        lst_countries.append(list(filter(None, re.split(r'\W|\d', arg_str))))
        maps = {country: lst for country, lst in zip(LIST_COUNTRIES, lst_countries)}
    draw(maps)


def print_possible_commands():
    for i, cmd in enumerate(COMMAND_DESCRIPTIONS):
        print(f'{i}) {cmd}\n')


def main():
    main_parser = create_parser()
    main_args = main_parser.parse_args()
    while True:
        try:
            cmd = input(ASK_ACTION_MSG)
            if cmd == 'start':
                make_new_map(main_args)
                infect_country(main_args)
            elif cmd == 'get info':
                get_info(main_args)
            elif cmd == 'get links':
                get_links(main_args)
            elif cmd == 'go day':
                go_day(main_args)
            elif cmd == 'help':
                print_possible_commands()
            elif cmd == 'exit':
                correct_exit()
            else:
                print(f'Unknown command: {cmd}\n')
        except KeyboardInterrupt:
            correct_exit()


if __name__ == '__main__':
    main()
