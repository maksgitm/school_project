import flask
from data import db_session
from flask import jsonify, make_response, request, abort
from data.dops import Dops
from data.make_results import get_results
from sqlalchemy_serializer import SerializerMixin


blueprint = flask.Blueprint(
    'dops_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/dops', methods=['POST'])
def create_dop():
    db_sess = db_session.create_session()
    dop = Dops(
        speciality=request.json['team_leader'],
        name=request.json['job'],
        cost=request.json['work_size'],
    )
    db_sess.add(dop)
    db_sess.commit()
    return jsonify({'id': jobs.id})