# Σημειωματάριο με Flask

Μια εφαρμογή τύπου "to-do list" που επιτρέπει στο χρήστη να δημιουργεί, τροποποιεί και διαγράφει σημειώσεις. Υποστηρίζει προτεραιότητες (importance) και αποθηκεύει τα δεδομένα σε SQLite χρησιμοποιώντας Flask και SQLAlchemy.

---

## Προαπαιτούμενα

- Python 3.10+
- Flask
- Flask-SQLAlchemy

---

## Οδηγίες Εκτέλεσης

1. **Κλωνοποίηση του αποθετηρίου**  
   ```bash
   git clone https://github.com/username/repo.git
   cd repo
   Σημαντικό για Windows: Αν παρουσιαστεί σφάλμα κατά την ενεργοποίηση του virtualenv, τρέξε στο PowerShell με δικαιώματα διαχειριστή:

Set-ExecutionPolicy RemoteSigned


και απάντησε Y.

2. Εγκατάσταση απαιτούμενων βιβλιοθηκών
pip install -r requirements.txt

3. Εκτέλεση της εφαρμογής
python app.py


Η εφαρμογή θα τρέχει τοπικά στη διεύθυνση: http://127.0.0.1:5000/

Περιγραφή εφαρμογής

Flask: Back-end, διαχείριση routes και templates.

SQLAlchemy: Διαχείριση SQLite βάσης δεδομένων.

Jinja2: Σύνδεση HTML templates με Python δεδομένα.

Virtualenv: Απομονωμένο περιβάλλον για όλες τις εξαρτήσεις.

Υποστηρίζει:

Προσθήκη νέας σημείωσης.

Τροποποίηση υπάρχουσας σημείωσης.

Διαγραφή σημείωσης.

Κατηγοριοποίηση σημειώσεων με βάση την προτεραιότητα (importance).

Δομή φακέλων
project-folder/
│
├── app.py                  
├── requirements.txt        
├── /templates              
├── /static                 
├── /env                    
└── notes.db                

Προβλήματα και λύσεις

Virtualenv δεν εκκινεί στα Windows: χρήση Set-ExecutionPolicy RemoteSigned.

Προσθήκη νέου πεδίου στη βάση δεδομένων: διαγραφή ή migration της SQLite βάσης.

.

- [Flask Tutorial - Tutorialspoint](https://www.tutorialspoint.com/flask/index.htm)
- [Flask για αρχάριους - YouTube](https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=LL&index=37&t=268s)
- [Flask SQLAlchemy - YouTube](https://www.youtube.com/watch?v=yKHJsLUENl0&list=LL&index=16)
- [Jinja2 Templating - RealPython](https://realpython.com/primer-on-jinja-templating)
- [SQLAlchemy Tutorial - Tutorialspoint](https://www.tutorialspoint.com/sqlalchemy/index.htm)
- [Virtualenv Documentation](https://virtualenv.pypa.io/en/latest)
- [Favicon Generator](https://favicon.io/)


