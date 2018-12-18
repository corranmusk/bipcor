from flask import render_template
from app.main import bp
from app.main.forms import AddBadIP

@bp.route('/')
@bp.route('/summary')
def summary():
    return render_template('main/summary.html',title="Summary")

@bp.route('/banned')
def currentlyBanned():
    return render_template('main/currentlybanned.html',title="Currently Banned")

@bp.route('/report')
def reportBadIP():
    form=AddBadIP()
    if form.validate_on_submit():
        flash ('Added BadIP report')
    return render_template('main/add.html',title="Report bad IP address",form=form)
