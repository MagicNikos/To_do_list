# Σημειωματάριο με Flask

Μια εφαρμογή τύπου "to-do list" που επιτρέπει στο χρήστη να δημιουργεί, τροποποιεί και διαγράφει σημειώσεις. Υποστηρίζει προτεραιότητες (importance) και αποθηκεύει τα δεδομένα σε SQLite χρησιμοποιώντας Flask και SQLAlchemy.

---

## Προαπαιτούμενα

- Python 3.10+
- Flask
- SQLAlchemy
- Jinja2

---

## Οδηγίες Εκτέλεσης

1. **Αρχή**  
Με την python εγκατεστημένη στο υπολογιστή σας, πηγαίνεται σε κάποιο terminal ή ανοίξτε το Powershell 
μέσα στο φάκελο με τα αρχεία του προγράμματος (όνομα φακέκου "Code") κάνοντας shift + right click ->
"open Powershell window here" Μετά κάνετε copy paste τις ακόλουθες εντολές στο powershell (ή στο άλλο σας 
terminal πχ στο vs code).


2. **Εγκατάσταση του virtualenv**  
"python -m venv env"

3. **Ενεργοποίηση του virtualenv**
#### Για Windows 
".\env\Scripts\Activate.ps1"
 
#### Για macOS/Linux
"source env/bin/activate"

---
###### αν υπάρξει πρόβλημα με την ενεργοποίηση του περιβάλλοντος ανοίψτε το powershell με "run as administrator" και γράψτε:
##### "Set-ExecutionPolicy RemoteSigned" και απάντησε "Y".
---


5. **Εγκατάσταση απαιτούμενων βιβλιοθηκών**
 
 "python -m pip install -r requirements.txt"


6. **Εκτέλεση του προγράμματος**

"python app.py"

Η εφαρμογή θα τρέχει τοπικά στη διεύθυνση: http://127.0.0.1:5000/

---

## Δομή φακέλων
Code/
│
├── app.py                  
├── requirements.txt        
├── /templates              
├── /static                 
├── /env                    
└── notes.db                 

## Πηγές
- https://www.tutorialspoint.com/flask/index.htm
- https://www.youtube.com/watch?v=Z1RJmh_OqeA&list=LL&index=37&t=268s
- https://www.youtube.com/watch?v=yKHJsLUENl0&list=LL&index=16
- https://realpython.com/primer-on-jinja-templating
- https://www.tutorialspoint.com/sqlalchemy/index.htm
- https://virtualenv.pypa.io/en/latest



### Μέρος της Ατομική εργασία για το μάθημα Εισαγωγή στην Επιστήμη του Ηλεκτρολόγου Μηχανικού 2024-2025 του Σαλιάρη Νικόλαου, Πανεπιστήμιο Πατρών
#### github : https://github.com/MagicNikos/To_do_list













