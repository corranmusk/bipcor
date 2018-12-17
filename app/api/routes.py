from app.api import bp

@bp.route('/banned/<format>')
def currentlyBanned():
    pass

@bp.route('/report')
def reportBadIP():
    pass

@bp.route('/gettoken')
def getToken():
    pass
