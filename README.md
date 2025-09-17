# Σημειωματάριο με Flask

Μια εφαρμογή τύπου "to-do list" που επιτρέπει στο χρήστη να δημιουργεί, τροποποιεί και διαγράφει σημειώσεις. Υποστηρίζει προτεραιότητες (importance) και αποθηκεύει τα δεδομένα σε SQLite χρησιμοποιώντας Flask και SQLAlchemy.

---

## Προαπαιτούμενα

- Python 3.10+
Αν δεν έχετε την python κατεβασμένη στο σύστημά σας,
επισκεφτείτε τον σύνδεσμο https://www.python.org/
και κατεβάστε την νεότερη έκδοση, επιλέγοντας "Add Python to PATH" για ευκολία.

---

## Οδηγίες Εκτέλεσης

1. **Αρχή**  
κάνετε shift + right click μέσα σε αυτό το folder και ανοίγετε το PowerShell μέσα σε αυτόν τον φάκελο

2. **Δημιουργία και ενεργοποίηση virtualenv**
python -m venv env

**powershell:**(αν υπάρξει πρόβλημα)
Set-ExecutionPolicy RemoteSigned
και απάντησε: Y.

# Windows PowerShell
.\env\Scripts\Activate.ps1
# macOS/Linux
source env/bin/activate

3. **Εγκατάσταση απαιτούμενων βιβλιοθηκών**
pip install -r requirements.txt
Εκτέλεση της εφαρμογής

4. **Εκτέλεση του προγράμματος**
python app.py

Η εφαρμογή θα τρέχει τοπικά στη διεύθυνση: http://127.0.0.1:5000/






## Περιγραφή εφαρμογής
Flask: Back-end, διαχείριση routes και templates.

SQLAlchemy: Διαχείριση SQLite βάσης δεδομένων.

Jinja2: Σύνδεση HTML templates με Python δεδομένα.

Virtualenv: Απομονωμένο περιβάλλον για όλες τις εξαρτήσεις.

Υποστηρίζει:
Προσθήκη νέας σημείωσης.

Τροποποίηση υπάρχουσας σημείωσης.

Διαγραφή σημείωσης.

Κατηγοριοποίηση σημειώσεων με βάση την προτεραιότητα (importance).

## Δομή φακέλων
project-folder/
│
├── app.py                  
├── requirements.txt        
├── /templates              
├── /static                 
├── /env                    
└── notes.db                 

## Προβλήματα και λύσεις
Virtualenv δεν εκκινεί στα Windows: χρήση Set-ExecutionPolicy RemoteSigned.

Προσθήκη νέου πεδίου στη βάση δεδομένων: διαγραφή ή migration της SQLite βάσης.

Favicon δεν εμφανίζεται: χρήση favicon.io.
## Πηγές
- https://www.tutorialspoint.com/flask/index.htm
- https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=LL&index=37&t=268s
- https://www.youtube.com/watch?v=yKHJsLUENl0&list=LL&index=16
- https://realpython.com/primer-on-jinja-templating
- https://www.tutorialspoint.com/sqlalchemy/index.htm
- https://virtualenv.pypa.io/en/latest



Μέρος της Ατομική εργασία για το μάθημα Εισαγωγή στην Επιστήμη του Ηλεκτρολόγου Μηχανικού 2024-2025 του Σαλιάρη Νικόλαου
## github : https://github.com/MagicNikos/To_do_list

