import sqlite3
import qrcode
import os

# Sample medicines data (name, barcode, description, dosage, side_effects, interactions)
sample_medicines = [
    ("Paracetamol", "QR0001", "Pain reliever and fever reducer.", "500mg twice daily", "Nausea, rash", "Alcohol, warfarin"),
    ("Ibuprofen", "QR0002", "Nonsteroidal anti-inflammatory drug.", "400mg thrice daily", "Stomach pain, dizziness", "Aspirin, diuretics"),
    ("Amoxicillin", "QR0003", "Antibiotic for bacterial infections.", "250mg thrice daily", "Diarrhea, headache", "Methotrexate, allopurinol"),
    ("Cetirizine", "QR0004", "Antihistamine for allergies.", "10mg once daily", "Drowsiness, dry mouth", "Alcohol, sedatives"),
    ("Metformin", "QR0005", "Used for type 2 diabetes.", "500mg twice daily", "Nausea, diarrhea", "Alcohol, cimetidine"),
    ("Amlodipine", "QR0006", "Calcium channel blocker for hypertension.", "5mg once daily", "Swelling, fatigue", "Simvastatin, diltiazem"),
    ("Atorvastatin", "QR0007", "Lowers cholesterol.", "10mg once daily", "Muscle pain, nausea", "Grapefruit juice, antibiotics"),
    ("Omeprazole", "QR0008", "Reduces stomach acid.", "20mg once daily", "Headache, abdominal pain", "Clopidogrel, methotrexate"),
    ("Losartan", "QR0009", "Treats high blood pressure.", "50mg once daily", "Dizziness, back pain", "Potassium supplements, NSAIDs"),
    ("Azithromycin", "QR0010", "Antibiotic for infections.", "500mg once daily", "Diarrhea, nausea", "Antacids, warfarin"),
]

def seed_medicines_db():
    conn = sqlite3.connect("medicines.db")
    c = conn.cursor()
    for med in sample_medicines:
        c.execute("INSERT OR IGNORE INTO medicines (name, barcode, description, dosage, side_effects, interactions) VALUES (?, ?, ?, ?, ?, ?)", med)
    conn.commit()
    conn.close()

def generate_qr_codes():
    qr_dir = "static/sample_qr"
    os.makedirs(qr_dir, exist_ok=True)
    for med in sample_medicines:
        img = qrcode.make(med[1])
        img.save(os.path.join(qr_dir, f"{med[1]}.png"))

if __name__ == "__main__":
    seed_medicines_db()
    generate_qr_codes()
    print("Sample medicines added and QR codes generated in static/sample_qr/")
