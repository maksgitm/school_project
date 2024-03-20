import os

from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_puper_secret_key_you_will_not_get_it'


# def main():
#     db_session.global_init("db/blogs.db")
#     app.register_blueprint(jobs_api.blueprint)
#     app.run()


@app.route('/')
@app.route('/index')
def start():
    return render_template("сайт.html", title='Школа 1357')


@app.route('/кружки')
def show_1():
    return render_template('кружки.html', title='Школа 1357')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # main()
