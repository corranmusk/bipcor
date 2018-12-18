from flask import render_template, flash
from app import db
from app.models import BadIPReport
from app.main import bp
from app.main.forms import AddBadIP
from datetime import datetime, timedelta

@bp.route('/')
@bp.route('/summary')
def summary():
    return render_template('main/summary.html',title="Summary")

@bp.route('/banned')
def currentlyBanned():
    return render_template(
        'main/currentlybanned.html',
        title="Currently Banned",
        bannedIPs=BadIPReport.query.filter(BadIPReport.expires>datetime.utcnow())
    )

@bp.route('/report',methods=['GET','POST'])
def reportBadIP():
    form=AddBadIP()
    if form.validate_on_submit():
        newreport=BadIPReport()
        newreport.badIP=form.badIP.data
        newreport.notes=form.notes.data
        newreport.source=form.source.data
        newreport.reported=datetime.utcnow()
        newreport.expires=datetime.utcnow() + timedelta(hours=6)
        db.session.add(newreport)
        db.session.commit()

        flash ('Added BadIP report for {}'.format(form.badIP.data))
    return render_template('main/add.html',title="Report bad IP address",form=form)
