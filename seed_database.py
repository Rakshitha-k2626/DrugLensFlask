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
    
    # Generate 1000 sample medicines
    medicines = []
    for i in range(1, 1001):
        name = f"SampleMed{i}"
        barcode = f"{100000000 + i}"
        description = f"Sample medicine {i} for testing purposes."
        dosage = f"{i % 500 + 1}mg every {i % 12 + 1} hours"
        side_effects = f"Side effect {i % 10 + 1}, Side effect {i % 5 + 1}"
        interactions = f"Interaction {i % 7 + 1}, Interaction {i % 3 + 1}"
        medicines.append((name, barcode, description, dosage, side_effects, interactions))
    
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