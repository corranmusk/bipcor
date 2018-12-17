from app import db

#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(64), index=True, unique=True)
#    email = db.Column(db.String(120), index=True, unique=True)
#    password_hash = db.Column(db.String(128))
#
#    def __repr__(self):
#        return '<User {}>'.format(self.username)

class BadIPReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), index=True)
    badIP = db.Column(db.String(20), index=True)
    notes = db.Column(db.String(180))
    reported = db.Column(db.DateTime)
    expires = db.Column(db.DateTime)

class AccessToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ipAddr= db.Column(db.String(20))
    validFrom = db.Column(db.DateTime)
    validTo = db.Column(db.DateTime)
    token = db.Column(db.String(32), index=True)
    lastUsed = db.Column(db.DateTime)

    def check_token(token,ipAddr):
        accesstoken = AccessToken.query.filter_by(token=token).first()
        if accesstoken is None or accesstoken.validTo < datetime.utcnow():
            return None
        return accesstoken
#class LogEntry(db.Model)
