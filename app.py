from flask import Flask, render_template, request
from database import init_db, save_note, get_notes

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        save_note(request.form["note"])
    notes = get_notes()
    return render_template("index.html", notes=notes)
    
    
app.run(debug=True)
