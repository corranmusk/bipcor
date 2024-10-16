from flask import render_template, flash, redirect, url_for
from app import db
from app.models import IPReport, AccessToken, LogEntry
from app.main import bp
from app.main.forms import AddIPAddr, GenerateToken, AddLogEntry
from datetime import datetime, timedelta
from sqlalchemy import desc, func
import secrets


@bp.route("/")
@bp.route("/summary")
def summary():
    toptenBadIPs = (
        db.session.query(IPReport.IPAddr, func.count(IPReport.IPAddr))
        .group_by(IPReport.IPAddr)
        .order_by(desc(func.count(IPReport.IPAddr)))
        .limit(10)
        .all()
    )
    return render_template(
        "main/summary.html", toptenBadIPs=toptenBadIPs, title="Summary"
    )


@bp.route("/banned")
def currentlyBanned():
    return render_template(
        "main/reports.html",
        title="Currently Banned",
        bannedIPs=IPReport.query.filter(IPReport.expires > datetime.utcnow()),
    )


@bp.route("/allreports")
def allReports():
    return render_template(
        "main/reports.html", title="All Reports", bannedIPs=IPReport.query.all()
    )


@bp.route("/report", methods=["GET", "POST"])
def reportIPAddr():
    form = AddIPAddr()
    if form.validate_on_submit():
        newreport = IPReport()
        newreport.IPAddr = form.IPAddr.data
        newreport.notes = form.notes.data
        newreport.source = form.source.data
        newreport.reported = datetime.utcnow()
        newreport.expires = datetime.utcnow() + timedelta(hours=6)
        db.session.add(newreport)
        db.session.commit()

        flash("Added IPAddr report for {}".format(form.IPAddr.data))
    return render_template("main/add.html", title="Report bad IP address", form=form)


@bp.route("/token/generate", methods=["GET", "POST"])
def generateToken():
    form = GenerateToken()
    if form.validate_on_submit():
        newtoken = AccessToken()
        newtoken.ipAddr = form.tokenIP.data
        newtoken.token = secrets.token_hex(20)
        newtoken.notes = form.notes.data
        # Add to database
        db.session.add(newtoken)
        db.session.commit()
        # Show token
        flash("Token generated for {}:{}".format(newtoken.ipAddr, newtoken.token))

    return render_template("main/generatetoken.html", title="Generate Token", form=form)


@bp.route("/token/list")
def listTokens():
    return render_template(
        "main/tokenlist.html", title="Tokens", tokens=AccessToken.query.all()
    )


@bp.route("/token/summary")
@bp.route("/token")
def tokenSummary():
    pass


@bp.route("/showlog")
def showLog():
    return render_template(
        "main/log.html",
        title="Event log",
        entries=LogEntry.query.order_by(desc(LogEntry.logtime)).all(),
    )


@bp.route("/addlog", methods=["GET", "POST"])
def addLogEntry():
    form = AddLogEntry()
    if form.validate_on_submit():
        newlogentry = LogEntry()
        newlogentry.loglevel = form.loglevel.data
        newlogentry.detail = form.detail.data
        db.session.add(newlogentry)
        db.session.commit()
        flash("Log entry {} added.".format(newlogentry.id))
        return redirect(url_for("main.showLog"))

    return render_template("main/qf.html", title="Add Log Entry", form=form)
