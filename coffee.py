import flask
import calculator

app = flask.Flask(__name__)


@app.route('/')
def home():
    return '418'


@app.route('/cups/<int:number_of_cups>/')
def calc_view(number_of_cups):
    spoons = calculator.get_amount_of_coffee_spoons(number_of_cups)
    return flask.render_template('index.html', spoons=spoons)


if __name__ == "__main__":
    app.run()
