# DrugLens - Medicine Information System 🏥

A comprehensive Flask-based medicine information system with QR/barcode scanning, multi-language translation, and user management.

## Features ✨

- **User Authentication** - Secure signup/login system with session management
- **Medicine Search** - Search medicines by name with detailed information
- **QR/Barcode Scanning** - Upload images to scan medicine barcodes for instant lookup
- **Multi-Language Translation** - Automatic translation to Hindi using Google Translate
- **Search History** - Track and view all medicine search history
- **Admin Panel** - Add new medicines to the database
- **Responsive Design** - Mobile-friendly interface with Bootstrap styling

## Quick Start 🚀

### Prerequisites

- Python 3.11 or higher
- pip or uv package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rakshitha-k2626/DrugLensFlask.git
   cd DrugLensFlask
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install flask pillow pyzbar googletrans==4.0.0-rc1
   ```

3. **Set up the database**
   ```bash
   python seed_database.py
   ```

4. **Set environment variable (recommended)**
   ```bash
   export SESSION_SECRET="your-secret-key-here"
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## System Dependencies 🔧

For QR/barcode scanning functionality, you may need to install system dependencies:

**Ubuntu/Debian:**
```bash
sudo apt-get install libzbar0
```

**macOS:**
```bash
brew install zbar
```

**Note:** The application gracefully handles missing QR scanning dependencies with appropriate fallback messages.

## Usage Guide 📖

### Getting Started
1. **Sign Up** - Create a new account or log in with existing credentials
2. **Search Medicines** - Use the search function to find medicine information by name
3. **Scan Barcodes** - Upload images containing barcodes/QR codes for instant medicine lookup
4. **View History** - Check your search history anytime
5. **Admin Functions** - Add new medicines to the database (admin panel)

### Sample Data
The application comes with sample medicine data:
- **Paracetamol** (Barcode: 123456789)
- **Ibuprofen** (Barcode: 987654321)
- **Aspirin** (Barcode: 555666777)
- **Amoxicillin** (Barcode: 111222333)
- **Omeprazole** (Barcode: 444555666)

## Configuration ⚙️

### Environment Variables
- `SESSION_SECRET` - Secret key for Flask sessions (required for production)
- `PORT` - Port number for the application (default: 5000)

### Database
- Uses SQLite database (`medicines.db`)
- Automatically creates tables on first run
- Run `python seed_database.py` to populate with sample data

## Architecture 🏗️

### Backend
- **Flask** - Web framework
- **SQLite** - Database for users, medicines, and search history
- **PIL (Pillow)** - Image processing for barcode scanning
- **pyzbar** - QR/barcode decoding library
- **googletrans** - Google Translate API for multi-language support

### Frontend
- **Jinja2** - Template engine
- **Bootstrap 5** - CSS framework for responsive design
- **Custom CSS** - Enhanced styling and user experience

### Security
- Session-based authentication
- SQL injection protection with parameterized queries
- CSRF protection recommended for production

## Development 👩‍💻

### Project Structure
```
DrugLensFlask/
├── app.py                 # Main Flask application
├── seed_database.py       # Database seeding script
├── templates/             # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── medicine.html
│   ├── history.html
│   ├── admin.html
│   └── scan.html
├── static/
│   └── css/
│       └── style.css      # Custom styling
├── pyproject.toml         # Python dependencies
├── uv.lock               # Dependency lock file
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

### Database Schema
- **users** - User accounts (id, email, password)
- **medicines** - Medicine data (id, name, barcode, description, dosage, side_effects, interactions)
- **history** - Search history (id, user_id, medicine_id, search_date)

## Deployment 🌐

For production deployment:

1. Set secure `SESSION_SECRET` environment variable
2. Use a production WSGI server (e.g., Gunicorn)
3. Configure proper database backup strategy
4. Enable HTTPS for secure communication
5. Consider implementing password hashing for enhanced security

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License 📄

This project is open source and available under the MIT License.

## Support 💬

For issues and questions, please create an issue on the GitHub repository.