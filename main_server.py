import flask
import lib_server
from macros_server import *


app = flask.Flask(APP_NAME)
virus = lib_server.EuropeVirus()


@app.route(HANDLE_INFECT, methods=['POST'])
def infect_country():
    country_name = flask.request.args['name']
    id = virus.infect_country(country_name)
    return str(id)


@app.route(HANDLE_ALL_INFO, methods=['GET'])
def get_all_info():
    return "\n".join(virus.get_all_info())


@app.route(HANDLE_INFO, methods=['GET'])
def get_info():
    country = flask.request.args['name']
    return str(virus.get_info(country))


@app.route(HANDLE_MAKE_MAP, methods=['POST'])
def make_map():
    virus.make_map()


@app.route(HANDLE_GO_DAYS, methods=['POST'])
def go_days():
    time = int(flask.request.args['time'])
    virus.go_days(time)
    return str(time)


@app.route(HANDLE_GO_DAYS, methods=['GET'])
def get_links():
    country_name = flask.request.args['name']
    return str(virus.get_links(country_name))


def main():
    app.run('::', port=PORT, debug=True)


if __name__ == '__main__':
    main()
