from flask import render_template
from app.api import bp
from app.models import BadIPReport
from app import db
from datetime import datetime

@bp.route('/banned')
def currentlyBanned():
    return render_template(
        'api/banned.html',
        bannedIPs=BadIPReport.query.filter(BadIPReport.expires>datetime.utcnow())
    )
@bp.route('/report')
def reportBadIP():
    pass

@bp.route('/gettoken')
def getToken():
    pass
