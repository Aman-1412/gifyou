import requests
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

API_KEY = "XXXXXXXXXXXXX"
ENDPOINT = "http://api.giphy.com"

@app.route("/",methods = ["GET","POST"])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'Trending':
            return trending()
        elif request.form['submit'] == 'Search':
            searchstring = request.form['searchstring']
            if searchstring:
                return search(searchstring)
            return search()
        elif request.form['submit'] == 'Translate':
            phrase = request.form['phrase']
            if phrase:
                return translate(phrase)
            return translate()
        elif request.form['submit'] == 'Random':
            tag = request.form['rantag']
            return random(tag)
    elif request.method == 'GET':
        return render_template("indexthree.html")



@app.route("/search/<searchstring>")
def search(searchstring="A man",limit = 5):
    URL = ENDPOINT + "/v1/gifs/search"
    searchstring = searchstring.replace(" ","-")
    payload = {"q" : searchstring, "api_key" : API_KEY, "limit" : str(limit), "fmt" : "html"}
    r = requests.get(URL,params = payload)
    # with open("test2search.html","w") as f:
    #     f.write(r.text)
    return r.text

@app.route("/birthday")
def birthday(searchstring="happy birthday",limit=3):
    URL = ENDPOINT + "/v1/gifs/search"
    searchstring = searchstring.replace(" ","+")
    payload = {"q" : searchstring, "api_key" : API_KEY, "limit" : str(limit), "fmt" : "html"}
    r = requests.get(URL,params = payload)
    # with open("test2search.html","w") as f:
    #     f.write(r.text)
    return r.text


@app.route("/trending")
def trending(limit=5):
    URL = ENDPOINT + "/v1/gifs/trending"
    payload = {"api_key" : API_KEY, "limit" : str(limit), "fmt" : "html"}
    r = requests.get(URL,params = payload)
    # with open("test2trend.html","w") as f:
    #     f.write(r.text)
    return r.content

@app.route("/translate")
def translate(phrase="Aman",limit=5):
    URL = ENDPOINT + "/v1/gifs/translate"
    payload = {"s" : phrase,"api_key" : API_KEY, "limit" : str(limit), "fmt" : "html"}
    r = requests.get(URL,params = payload)
    return r.text

@app.route("/random")
def random(tag=""):
    URL = ENDPOINT + "/v1/gifs/random"
    if tag:
        payload = {"tag" : tag, "api_key" : API_KEY, "fmt" : "html"}
    else:
        payload = {"api_key" : API_KEY, "fmt" : "html"}
    r = requests.get(URL,params = payload)
    return r.text

@app.route("/gifbyid/<id>")
def gifbyid(id):
    URL = ENDPOINT + "/v1/gifs/" +str(id)

    payload = {"api_key" : API_KEY,"fmt" : "html"}
    r = requests.get(URL,params = payload)





if __name__=="__main__":
	app.run(debug=True)
