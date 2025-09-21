from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime
from PIL import Image
from googletrans import Translator
import os

# ---------------- SAFE PYZXING LOADING ----------------
PYZXING_AVAILABLE = False
try:
    from pyzxing import BarCodeReader
    reader = BarCodeReader()
    PYZXING_AVAILABLE = True
except Exception as e:
    print(f"Warning: pyzxing not available. QR/Barcode scanning disabled. Reason: {e}")
    PYZXING_AVAILABLE = False

    # fallback decode function
    def decode(img):
        return []


app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'fallback-secret-key')
translator = Translator()

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect("medicines.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        barcode TEXT,
        description TEXT,
        dosage TEXT,
        side_effects TEXT,
        interactions TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        medicine_id INTEGER,
        search_date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(medicine_id) REFERENCES medicines(id)
    )''')
    conn.commit()
    conn.close()

init_db()

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return render_template("home.html")

# Signup
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect("medicines.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (email,password) VALUES (?,?)",(email,password))
            conn.commit()
            conn.close()
            return redirect("/login")
        except:
            conn.close()
            return "Email already exists!"
    return render_template("signup.html")

# Login
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect("medicines.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email=? AND password=?",(email,password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user_id']=user[0]
            return redirect("/")
        else:
            return "Invalid credentials!"
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.pop('user_id',None)
    return redirect("/")

# Search Medicine
@app.route("/medicine", methods=["GET","POST"])
def medicine():
    if 'user_id' not in session:
        return redirect("/login")
    result=None
    if request.method=="POST":
        query = request.form['query']
        conn = sqlite3.connect("medicines.db")
        c = conn.cursor()
        c.execute("SELECT * FROM medicines WHERE name LIKE ?",('%'+query+'%',))
        result = c.fetchone()
        if result:
            c.execute("INSERT INTO history (user_id, medicine_id, search_date) VALUES (?,?,?)",
                      (session['user_id'], result[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
        conn.close()
    return render_template("medicine.html", result=result)

# Scan QR/Barcode
@app.route("/scan", methods=["GET","POST"])
def scan():
    if 'user_id' not in session:
        return redirect("/login")
    result = None
    translated = None
    error_message = None
    scanned_code = None

    if request.method == "POST":
        if not PYZXING_AVAILABLE:
            error_message = "QR/Barcode scanning functionality is currently unavailable. System dependencies are being configured."
        else:
            file = request.files['barcode_image']
            temp_path = os.path.join("static", "temp_barcode.png")
            file.save(temp_path)
            abs_temp_path = os.path.abspath(temp_path)
            abs_temp_path_fwd = abs_temp_path.replace('\\', '/')
            print(f"[DEBUG] Path sent to pyzxing: {abs_temp_path_fwd}")
            decoded = reader.decode(abs_temp_path_fwd)
            if decoded and decoded[0]['parsed']:
                scanned_code = decoded[0]['parsed']
                # Convert bytes to string if needed
                if isinstance(scanned_code, bytes):
                    scanned_code = scanned_code.decode('utf-8')
                conn = sqlite3.connect("medicines.db")
                c = conn.cursor()
                c.execute("SELECT * FROM medicines WHERE barcode=?", (scanned_code,))
                result = c.fetchone()
                if result:
                    c.execute("INSERT INTO history (user_id, medicine_id, search_date) VALUES (?,?,?)",
                              (session['user_id'], result[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    conn.commit()
                    translated = {
                        "description": translator.translate(result[3], dest='hi').text,
                        "dosage": translator.translate(result[4], dest='hi').text,
                        "side_effects": translator.translate(result[5], dest='hi').text,
                        "interactions": translator.translate(result[6], dest='hi').text
                    }
                conn.close()
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)

    return render_template("scan.html", result=result, translated=translated, error_message=error_message, scanned_code=scanned_code)

# History
@app.route("/history")
def history():
    if 'user_id' not in session:
        return redirect("/login")
    conn=sqlite3.connect("medicines.db")
    c=conn.cursor()
    c.execute("""SELECT m.name,m.description,h.search_date 
                 FROM history h 
                 JOIN medicines m ON h.medicine_id=m.id 
                 WHERE h.user_id=?""",(session['user_id'],))
    records=c.fetchall()
    conn.close()
    return render_template("history.html",records=records)

# Admin Panel
@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        name=request.form['name']
        barcode=request.form['barcode']
        description=request.form['description']
        dosage=request.form['dosage']
        side_effects=request.form['side_effects']
        interactions=request.form['interactions']
        conn=sqlite3.connect("medicines.db")
        c=conn.cursor()
        c.execute("INSERT INTO medicines (name,barcode,description,dosage,side_effects,interactions) VALUES (?,?,?,?,?,?)",
                  (name,barcode,description,dosage,side_effects,interactions))
        conn.commit()
        conn.close()
        return "Medicine added successfully!"
    return render_template("admin.html")

# Run on Replit
if __name__=="__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port, debug=True)