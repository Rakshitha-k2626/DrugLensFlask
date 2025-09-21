# Overview

DrugLens is a comprehensive medicine information system built with Flask that enables users to search for medicine details, scan QR/barcodes for instant information retrieval, and access multi-language translations. The application features user authentication, search history tracking, and an admin panel for medicine database management. The system is designed to provide healthcare professionals and patients with quick access to critical medicine information including dosages, side effects, and drug interactions.

**Status: Fully implemented and operational** - The Flask application is running successfully on port 5000 with all core features functioning. The database is initialized with sample medicine data for testing.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Jinja2 templates with Bootstrap 5 for responsive UI design
- **Static Assets**: CSS styling with custom gradients and hover effects for enhanced user experience
- **Navigation**: Session-based conditional navigation showing different menu items for authenticated vs. non-authenticated users
- **Forms**: HTML forms for user registration, login, medicine search, barcode scanning, and admin medicine entry

## Backend Architecture
- **Web Framework**: Flask with session-based authentication using server-side sessions
- **Route Structure**: RESTful routes for authentication (`/login`, `/signup`, `/logout`), core functionality (`/medicine`, `/scan`, `/history`), and administration (`/admin`)
- **Authentication**: Simple email/password authentication with session management
- **File Upload Handling**: Image upload processing for barcode/QR code scanning functionality
- **Error Handling**: Graceful fallback mechanisms for optional dependencies

## Data Storage
- **Database**: SQLite with three main tables:
  - `users`: User authentication data (id, email, password)
  - `medicines`: Medicine information (id, name, barcode, description, dosage, side_effects, interactions)
  - `history`: User search history with foreign key relationships
- **Database Initialization**: Automatic table creation on application startup
- **Data Relationships**: Foreign key constraints between users, medicines, and search history

## Image Processing & Scanning
- **QR/Barcode Scanning**: pyzbar library for decoding barcodes and QR codes from uploaded images
- **Image Processing**: PIL (Pillow) for image manipulation and processing
- **Fallback Strategy**: Graceful degradation when pyzbar is unavailable, returning empty results instead of crashing

## Translation Services
- **Multi-language Support**: Google Translate API integration via googletrans library
- **Translation Features**: Real-time translation of medicine information to different languages
- **Language Detection**: Automatic language detection and translation capabilities

## Security & Configuration
- **Session Management**: Flask sessions with configurable secret key from environment variables
- **Environment Configuration**: Support for environment-based configuration with fallback defaults
- **Password Storage**: Plain text password storage (note: production systems should implement proper password hashing)

# External Dependencies

## Core Framework Dependencies
- **Flask**: Web application framework for routing, templating, and request handling
- **sqlite3**: Built-in Python database interface for local data storage

## Image Processing Dependencies
- **PIL (Pillow)**: Image processing library for handling uploaded barcode/QR code images
- **pyzbar**: Barcode and QR code decoding library with optional import handling

## Translation Services
- **googletrans**: Google Translate API client for multi-language medicine information translation

## Frontend Dependencies
- **Bootstrap 5**: CDN-hosted CSS framework for responsive design and UI components
- **Custom CSS**: Local stylesheet for application-specific styling and theming

## Optional Dependencies
The application implements graceful fallback mechanisms for optional dependencies, ensuring core functionality remains available even when certain features (like barcode scanning) are unavailable due to missing libraries.