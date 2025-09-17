# virtualenv env 
# .\env\Scripts\Activate.ps1 
# python app.py 

from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta  


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


def greek_time(): #Για να είναι σωστή η ώρα στην Ελλάδα
    return datetime.utcnow() + timedelta(hours=3)

class Note(db.Model): #Οι σημειώσεις έχουν 4 στοιχεία 
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=greek_time)
    is_priority = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Note {self.id}>"



with app.app_context():
    db.create_all()


#Εδώ έχουμε τα routes μας για να μπορούμε να προσθέσουμε, να αφαιρέσουμε, να τροποποιήσουμε και να κατατάξουμε τις σημειώσεις μας
@app.route("/", methods=["GET", "POST"]) # POST αφού θα προσθέσουμε και αλλή σημείωση
def home():
    if request.method == "POST": 
        note_text = request.form.get("text").strip()  #Καθαρίζει το string απο άχρηστα κενά 

        if not note_text:  #έλεγχος αν η σημείωση είναι άδεια 
            all_notes = Note.query.order_by(Note.is_priority.desc(), Note.created_at.asc()).all() #κατάταξη τους με πρώτες τις σημειώσεις με τα άστρα και μετά χρονολογικά (γινεται και κατω)
            return render_template("home.html", notes=all_notes, error="Οι σημειώσεις δεν μπορούν να είναι κενές")

        new_note = Note(text=note_text)
        try:

            db.session.add(new_note) 
            db.session.commit()
            return redirect(url_for("home")) 
        except:
            return "Υπήρξε πρόβλημα με την προσθήκη της σημείωσης"
    else:
        all_notes = Note.query.order_by(Note.is_priority.desc(), Note.created_at.asc()).all() 
        return render_template("home.html", notes=all_notes)


@app.route("/remove/<int:note_id>")
def remove(note_id):
    note = Note.query.get_or_404(note_id) #Βρες την σημείωση ή 404

    try:
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for("home"))
    except:
        return "Υπήρξε πρόβλημα με την διαγραφή της σημείωσης"


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit(note_id):
    note = Note.query.get_or_404(note_id) #Βρες την σημείωση ή 404

    if request.method == "POST":
        new_text = request.form.get("text").strip()  #Πάλι καθαρίζει το string απο άχρηστα κενά 

        if not new_text:  #έλεγχος αν η σημείωση είναι άδεια (γινεται μόνο 2 φορές αρα δεν το έκανα σύναρτηση)
            return render_template("edit.html", note=note, error="Οι σημειώσεις δεν μπορούν να είναι κενές")

        note.text = new_text

        try:
            db.session.commit()
            return redirect(url_for("home"))
        except:
            return "Υπήρξε πρόβλημα με την τροποποίηση της σημείωσης"
    else:
        return render_template("edit.html", note=note)

@app.route("/priority/<int:note_id>")
def toggle_priority(note_id):
    note = Note.query.get_or_404(note_id)
    note.is_priority = not note.is_priority

    try:
        db.session.commit()
        return redirect(url_for("home"))
    except:
        return "Υπήρξε πρόβλημα με την αλλαγή της προτεραιότητας της σημείωσης"


# Όταν τρέχει η εφαρμογή.. το debug για να βλεπουμε αν έχει errors
if __name__ == "__main__":
    app.run(debug=True)