from flask import render_template
from app.main import bp

@bp.route('/')
@bp.route('/banned')
def currentlyBanned():
    pass

@bp.route('/report')
def reportBadIP():
    pass
