#!/usr/bin/env python3
"""
Database seeding script for DrugLens Flask Application
Creates and populates the SQLite database with sample medicine data.
"""

import sqlite3
import os

def create_tables():
    """Create database tables if they don't exist."""
    conn = sqlite3.connect("medicines.db")
    c = conn.cursor()
    
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    
    # Create medicines table
    c.execute('''CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        barcode TEXT,
        description TEXT,
        dosage TEXT,
        side_effects TEXT,
        interactions TEXT
    )''')
    
    # Create history table
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
    print("✓ Database tables created successfully")

def seed_medicines():
    """Add sample medicine data to the database."""
    conn = sqlite3.connect("medicines.db")
    c = conn.cursor()
    
    # Sample medicines data
    medicines = [
        ('Paracetamol', '123456789', 
         'Pain reliever and fever reducer. Commonly used for headaches, muscle aches, and reducing fever.',
         '500mg every 6 hours, maximum 4 doses per day',
         'Nausea, dizziness, skin rash (rare)',
         'May interact with warfarin, alcohol. Avoid overdose as it can cause liver damage.'),
        
        ('Ibuprofen', '987654321',
         'Anti-inflammatory pain reliever. Effective for pain, inflammation, and fever reduction.',
         '400mg every 8 hours with food, maximum 1200mg per day',
         'Stomach upset, heartburn, dizziness, headache',
         'May interact with blood thinners, ACE inhibitors. Not recommended with kidney disease.'),
        
        ('Aspirin', '555666777',
         'Pain reliever, anti-inflammatory, and blood thinner. Used for pain relief and heart attack prevention.',
         '325mg every 4-6 hours for pain, 81mg daily for heart protection',
         'Stomach irritation, increased bleeding risk, ringing in ears',
         'Avoid with other blood thinners, not for children under 16 due to Reye syndrome risk.'),
        
        ('Amoxicillin', '111222333',
         'Antibiotic used to treat bacterial infections including respiratory, ear, and urinary tract infections.',
         '500mg every 8 hours for 7-10 days',
         'Nausea, diarrhea, skin rash, allergic reactions',
         'May interact with birth control pills, blood thinners. Complete full course even if feeling better.'),
        
        ('Omeprazole', '444555666',
         'Proton pump inhibitor that reduces stomach acid production. Used for heartburn and ulcers.',
         '20mg once daily before breakfast',
         'Headache, nausea, diarrhea, stomach pain',
         'May interact with clopidogrel, digoxin. Long-term use may affect vitamin B12 absorption.')
    ]
    
    # Insert medicines if they don't already exist
    for medicine in medicines:
        c.execute("SELECT COUNT(*) FROM medicines WHERE name = ?", (medicine[0],))
        if c.fetchone()[0] == 0:
            c.execute("INSERT INTO medicines (name, barcode, description, dosage, side_effects, interactions) VALUES (?, ?, ?, ?, ?, ?)", 
                     medicine)
            print(f"✓ Added medicine: {medicine[0]}")
        else:
            print(f"- Medicine already exists: {medicine[0]}")
    
    conn.commit()
    conn.close()
    print("✓ Medicine database seeded successfully")

def main():
    """Main function to run the database seeding process."""
    print("🏥 DrugLens Database Seeding")
    print("=" * 40)
    
    # Check if database exists
    db_exists = os.path.exists("medicines.db")
    if db_exists:
        print("ℹ️  Database file already exists")
    else:
        print("📝 Creating new database file")
    
    # Create tables
    create_tables()
    
    # Seed with sample data
    seed_medicines()
    
    print("\n✅ Database setup complete!")
    print("🔍 The DrugLens application now has sample medicine data for testing.")
    print("\nSample medicines available:")
    print("- Paracetamol (Barcode: 123456789)")
    print("- Ibuprofen (Barcode: 987654321)")
    print("- Aspirin (Barcode: 555666777)")
    print("- Amoxicillin (Barcode: 111222333)")
    print("- Omeprazole (Barcode: 444555666)")

if __name__ == "__main__":
    main()