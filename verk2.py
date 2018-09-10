#from sys import argv

from bottle import *

@route("/")
def index():
    return """
    <h2>Verkefni 2</h2>
    <a href="/a">detta er Lidur A</a>
    <a href="/b">detta er Lidur B</a>
    """

@route("/a")
def a():
    return """ 
        <h2>Verkefni 2 - Lidur A</h2>
        <a href = "/sida/1">Sida 1.</a> 
        <a href = "/sida/2">Sida 2.</a>  
        <a href = "/sida/3">Sida 3.</a>  
    """

@route("/sida/<id>")
def page(id):
    if id == '1':
        return "detta er sida 1<br><a href = '/a'><Til baka</a>"
    if id == '2':
        return "detta er sida 2<br><a href = '/a'><Til baka</a>"
    if id == '3':
        return "detta er sida 3<br><a href = '/a'><Til baka</a>"
    else:
        abort(404,"<h2 style = 'color red'>dessi Sida finnst ekki")


@route("/b")
def b():
    return """ 
        <h2>Verkefni 2 Lidur B</h2>
        <h4>Veldu uppahalds bokstafinn dinn</h4>
        <a href ="/sida2?bokstafur=a<img src = 'img/A'.jpg></a>
        <a href ="/sida2?bokstafur=b<img src = 'img/B'.jpg></a>
        <a href ="/sida2?bokstafur=c<img src = 'img/C'.jpg></a>
        <a href ="/sida2?bokstafur=d<img src = 'img/D'.jpg></a>
        """


@route("/sida2")
def page():
    l = request.query.bokstafur
    if l == 'a':
        return"<h3>Minn uppahalds bokstafur er:</h3><img src = 'img/A'.jpg>"
    if l == 'b':
        return"<h3>Minn uppahalds bokstafur er:</h3><img src = 'img/B'.jpg>"
    if l == 'c':
        return"<h3>Minn uppahalds bokstafur er:</h3><img src = 'img/C'.png>"
    if l == 'd':
        return"<h3>Minn uppahalds bokstafur er:</h3><img src = 'img/D'.png>"




@route('/img/<skra>')
def static_skrar(skra):
    return static_file(skra, root='img')







@error(404)
def villa(error):
    return "<h2 style = color:red>dessi sida finnst ekki</h2>"



run(host = 'localhost',port= 8080, reloader=True, debug=True)
