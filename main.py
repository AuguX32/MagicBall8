from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)

liste_phrases = [
"Peut être...",
"La boule est trop occupée, essaye plus tard ",
"Essaye plus tard",
"Essaye encore",
" Pas d'avis",
" C'est ton destin",
" Le sort en est jeté",
" Une chance sur deux",
" Repose ta question",
"Seul le destin te l'apprendra",

" D'après moi oui",
" C'est certain",
" Oui absolument",
" Tu peux compter dessus",
" Sans aucun doute",
" Très probable",
" Oui",
" C'est bien parti",
" C'est bien parti pour",
" La chance est de ton coté",

" C'est non",
" Peu probable",
" Faut pas rêver",
" N'y compte pas",
" Impossible",
]

@app.route('/', methods = ["GET", "POST"])
def index () :
    reponse = None
    if request.method == "POST" :
        reponse = choice(liste_phrases)
    return render_template("index.html", prediction = reponse)











app.run(host='0.0.0.0', port=81)