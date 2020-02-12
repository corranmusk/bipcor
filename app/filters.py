from app import app


@app.template_filter("formatdatetime")
def format_datetime(value, format="%d %b %Y %H:%M"):
    """Format a date time to (Default): d Mon YYYY HH:MM"""
    if value is None:
        return None
    return value.strftime(format)
