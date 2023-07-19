from flask import Blueprint

site = Blueprint('site', __name__,url_prefix='/site')

@site.route('/')
def getdata():
    return "hello site"