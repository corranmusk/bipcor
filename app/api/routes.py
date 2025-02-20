from flask import render_template
from flask import abort, jsonify, make_response, request
from app.api import bp
from app.models import IPReport, AccessToken
from app import db
from datetime import datetime, timedelta, timezone


@bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)


@bp.route("/banned")
def currentlyBanned():
    return render_template(
        "api/banned.html",
        bannedIPs=db.session.query(IPReport.IPAddr)
        .filter(IPReport.expires > datetime.now(timezone.utc))
        .distinct(),
    )


@bp.route("/report", methods=["POST"])
def reportIPAddr():
    token = request.json.get("token")
    reportingIP = request.remote_addr
    IPAddr = request.json.get("IPAddr")
    notes = request.json.get("notes")
    if AccessToken.check_token(token, reportingIP):
        newreport = IPReport()
        newreport.IPAddr = IPAddr
        newreport.notes = notes
        newreport.source = reportingIP
        newreport.reported = datetime.now(timezone.utc)
        newreport.expires = datetime.now(timezone.utc) + timedelta(hours=6)
        db.session.add(newreport)
        db.session.commit()
    else:
        abort(401)
    return jsonify({"IPAddr": IPAddr}), 200


@bp.route("/gettoken")
def getToken():
    pass


@bp.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({"ip": request.remote_addr}), 200
