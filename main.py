import flask
import lib


app = flask.Flask('Plague_Inc_Europe')
virus = lib.EuropeVirus()


def make_output(country):
    return str(country.name) + ' (ID: ' + str(country.id) + ') is infected: ' + str(country.infected)


@app.route('/infect', methods=['POST'])
def infect_country():
    country_name = flask.request.args['name']
    id = virus.infect_country(country_name)
    return str(id)


@app.route('/get_all_info', methods=['GET'])
def get_all_info():
    res = ''
    for country in virus.get_all_info():
        res += make_output(country) + '\n'
    return res


@app.route('/get_info', methods=['GET'])
def get_info():
    country = flask.request.args['name']
    return str(virus.get_info(country))


@app.route('/make_map', methods=['POST'])
def make_map():
    virus.make_map()


@app.route('/go_days', methods=['POST'])
def go_days():
    time = int(flask.request.args['time'])
    virus.go_days(time)
    return str(time)


@app.route('/get_links', methods=['GET'])
def get_links():
    country_name = flask.request.args['name']
    return str(virus.get_links(country_name))


def main():
    app.run('::', port=8000, debug=True)


if __name__ == '__main__':
    main()