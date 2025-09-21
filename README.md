
# DrugLens Flask Application

DrugLens is a Flask-based web application for scanning medicine QR/barcodes, searching medicines, and managing a medicine database. It supports user authentication, history tracking, and provides medicine information in both English and Hindi (via Google Translate API).


## Features

- **User Signup/Login/Logout**: Secure user authentication and session management.
- **Medicine Search**: Search for medicines by name and view detailed information.
- **QR/Barcode Scan**: Upload a QR/barcode image to instantly retrieve medicine details.
- **History**: View your search and scan history.
- **Admin Panel**: Add new medicines to the database.
- **Sample Data & QR Codes**: Comes with 10 sample medicines and QR codes for testing.
- **Multilingual Support**: Medicine details are auto-translated to Hindi.


## Setup Instructions

### 1. Clone the Repository

```
git clone <repo-url>
cd DrugLensFlask
```

### 2. Install Dependencies

Make sure you have Python 3.8+ installed. Install required packages:

```
pip install flask pillow googletrans==4.0.0-rc1 qrcode
```

### 3. Seed the Database and Generate Sample QR Codes

Run the following script to populate the database and generate QR codes:

```
python seed_sample_meds_and_qr.py
```

This will:
- Add 10 sample medicines to `medicines.db`
- Generate 10 QR code images in `static/sample_qr/`

### 4. Run the Application

```
python app.py
```

The app will be available at `http://localhost:5000/` by default.

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


## Usage

- **Signup/Login**: Create a user account or log in.
- **Search Medicine**: Use the search page to find medicines by name.
- **Scan QR/Barcode**: Go to the scan page, upload a QR code image (e.g., from `static/sample_qr/QR0001.png`), and view the medicine details.
- **History**: View your search and scan history.
- **Admin Panel**: Add new medicines (requires manual navigation).

### Sample Data & QR Codes

The app comes with 10 sample medicines and QR codes. Example:

- **Paracetamol** (Barcode: QR0001, QR image: `static/sample_qr/QR0001.png`)
- **Ibuprofen** (Barcode: QR0002, QR image: `static/sample_qr/QR0002.png`)
- ...

Upload any of these QR images on the scan page to test the workflow.

## Configuration ⚙️

### Environment Variables
- `SESSION_SECRET` - Secret key for Flask sessions (required for production)
- `PORT` - Port number for the application (default: 5000)


### Database
- Uses SQLite database (`medicines.db`)
- Automatically creates tables on first run
- Run `python seed_sample_meds_and_qr.py` to populate with sample data and QR codes

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


### Folder Structure
```
DrugLensFlask/
├── app.py                  # Main Flask application
├── generate_san_qr.py      # (Optional) QR code generation script
├── seed_database.py        # (Optional) Database seeding script
├── seed_sample_meds_and_qr.py # Script to seed sample medicines and QR codes
├── medicines.db            # SQLite database
├── static/
│   ├── css/
│   │   └── style.css       # Custom styles
│   └── sample_qr/          # Generated sample QR codes
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── medicine.html
│   ├── scan.html
│   ├── history.html
│   └── admin.html
├── README.md               # Project documentation
└── ...
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


## License

This project is for educational/demo purposes.

---

For questions or contributions, please open an issue or pull request.