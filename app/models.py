from app import db
from datetime import datetime
from sqlalchemy import desc

# class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(64), index=True, unique=True)
#    email = db.Column(db.String(120), index=True, unique=True)
#    password_hash = db.Column(db.String(128))
#
#    def __repr__(self):
#        return '<User {}>'.format(self.username)


class IPReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), index=True)
    IPAddr = db.Column(db.String(20), index=True)
    notes = db.Column(db.String(180))
    reported = db.Column(db.DateTime, default=datetime.utcnow())
    expires = db.Column(db.DateTime)

    def __repr__(self):
        return "<IPReport {}>".format(self.id)


class AccessToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ipAddr = db.Column(db.String(20))
    validFrom = db.Column(db.DateTime, default=datetime.utcnow())
    validTo = db.Column(db.DateTime)
    token = db.Column(db.String(32), index=True)
    lastUsed = db.Column(db.DateTime)
    notes = db.Column(db.Text)

    def __repr__(self):
        return "<AccessToken {}>".format(self.id)

    def updatelastused(token, ipAddr):
        pass

    def check_token(token, ipAddr):
        accesstoken = (
            AccessToken.query.order_by(desc(AccessToken.validFrom))
            .filter_by(token=token, ipAddr=ipAddr)
            .first()
        )
        if accesstoken is not None:
            # We have a result
            if accesstoken.validTo:
                # Check that date is valid
                if accesstoken.validTo < datetime.utcnow():
                    return True
            else:
                # No end date set so okay
                return True
        return False


class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logtime = db.Column(db.DateTime, default=datetime.utcnow())
    loglevel = db.Column(db.String(8))
    detail = db.Column(db.Text)

    def __repr__(self):
        return "<LogEntry {}>".format(self.id)
