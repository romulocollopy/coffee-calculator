import flask
import calculator

app = flask.Flask(__name__)


@app.route('/')
def home():
    response = flask.jsonify({'status_code': '418',
                              'reason': "I'm a teapot"})
    response.status_code = 418
    return response


@app.route('/cups/')
def calc_view():
    number = flask.request.args.get('number', None)
    number = float(number) if number else None

    spoons = calculator.get_amount_of_coffee_spoons(number) \
        if number is not None else None

    return flask.render_template('index.html', spoons=spoons)


@app.route('/cups/12/')
def redirect_to_new():
    return flask.redirect('/cups/')


if __name__ == "__main__":
    app.run()
