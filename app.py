from flask import Flask, render_template, request
from database import init_db, save_note, get_notes, delete_all_notes

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        if request.form["action"] == "save":
            save_note(request.form["note"])
        elif request.form["action"] == 'delete':
            delete_all_notes()
    notes = get_notes()
    return render_template("index.html", notes=notes)
    
    
app.run(debug=True)
