import os

from api import dops_api
from data.dops import Dops
from flask import Flask, render_template, url_for
import qrcode

from data import db_session
from data.make_results import get_results

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_puper_secret_key_you_will_not_get_it'


def main():
    db_session.global_init("db/sch_db.sqlite")
    # app.register_blueprint(dops_api.blueprint)
    db_sess = db_session.create_session()
    db_sess.query(Dops).delete()
    data = get_results()
    for el in data:
        link = el['link']
        qr = qrcode.make(link)
        qr.save('static/images/test_img.jpg')
        f = open('static/images/test_img.jpg', 'rb')
        file = f.read()
        dop = Dops(
            speciality=el['topic'],
            name=el['name_'],
            cost=el['cost'],
            age=el['age'],
            qr_code=file
        )
        f.close()
        db_sess.add(dop)
        db_sess.commit()
    # app.run()


@app.route('/')
@app.route('/index')
def start():
    return render_template("сайт.html", title='Школа 1357')


@app.route('/кружки')
def show_1():
    return render_template('кружки.html', title='Школа 1357')


if __name__ == '__main__':
    main()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
