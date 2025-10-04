# Lost & Found Web Application

## Overview
A Django-based Lost & Found web application that helps users report lost and found items. The system automatically matches reports using fuzzy text matching to connect lost items with found items.

## Current State
- Fully functional Django application running on SQLite
- Automatic fuzzy matching system using difflib (threshold: 0.55)
- Admin panel for managing items and marking them as claimed
- Image upload support for item photos
- Search functionality for browsing reports
- Responsive UI using Water.css framework

## Recent Changes
- October 04, 2025: Initial project setup and implementation
  - Created Django project structure with core app
  - Implemented Item model with status tracking (lost/found)
  - Built fuzzy matching algorithm using SequenceMatcher
  - Created all views and templates
  - Configured for Replit environment (ALLOWED_HOSTS, port 5000)
  - Applied database migrations

## Project Architecture

### Models
- **Item**: Main model storing lost/found reports
  - Fields: title, description, status, date, location, contact, photo, claimed
  - Tracks creator and creation timestamp
  - Status choices: 'lost' or 'found'

### Views
- **index**: Homepage showing 8 most recent reports
- **report_item**: Form for submitting lost/found items with automatic matching
- **item_list**: Browse all reports with search functionality
- **item_detail**: Detailed view of individual items

### Matching Algorithm
- Uses difflib.SequenceMatcher for fuzzy text matching
- Weighted scoring: title (60%), description (30%), location (10%)
- Match threshold: 0.55 (55% similarity)
- Automatically runs when new items are reported
- Logs potential matches to console

### Admin Features
- Full CRUD operations for items
- Filter by status and claimed status
- Search across title, description, location, contact
- Mark items as claimed/returned

## Technology Stack
- Django 5.2.7
- Python 3.11
- SQLite database
- Pillow for image handling
- Water.css for styling

## Usage

### Admin Access
1. Create a superuser: `python manage.py createsuperuser`
2. Access admin panel at `/admin/`
3. Manage items and mark them as claimed

### For Users
- Visit homepage to see recent reports
- Click "Report" to submit lost or found items
- Click "Browse" to search all reports
- System automatically suggests matches based on similarity

## Future Enhancements
- User authentication and profiles
- Email notifications for matching items
- Cloud storage for images (Cloudinary/Firebase)
- REST API with React frontend
- Pagination for item lists
- Enhanced matching with NLP/embeddings
