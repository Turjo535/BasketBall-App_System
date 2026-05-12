# 🏀 Basketball Application System

A comprehensive Django REST Framework-based backend system for basketball player and coach management, featuring performance tracking, team scouting, and automated report generation.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Usage Examples](#usage-examples)
- [Database Schema](#database-schema)
- [File Management](#file-management)
- [Development](#development)
- [Contributing](#contributing)

---

## 🎯 Overview

The Basketball Application is a sophisticated backend system designed to:

- **Track Player Performance**: Record and analyze individual player statistics, game footage, and performance metrics
- **Generate Comprehensive Reports**: Automatically create detailed PDF reports with player strengths, weaknesses, and performance projections
- **Facilitate Coaching**: Enable coaches to manage teams, scout opponents, analyze team dynamics, and identify key players
- **Manage Authentication**: Implement secure JWT-based authentication with OTP-based email verification
- **Organize Team Data**: Maintain detailed records of team information, game results, and scouting analysis

This system serves as the backend for a complete basketball management ecosystem connecting players, coaches, and team management.

---

## ✨ Features

### Player Management
- ✅ Player profile creation with detailed information (jersey, height, position, class year)
- ✅ Game performance tracking with contextual data
- ✅ Video file uploads for game footage
- ✅ Automated performance report generation with statistics

### Coaching & Scouting
- ✅ Team information management for opponents
- ✅ Advanced scouting reports with JSON-based strengths/weaknesses
- ✅ Key player identification and analysis
- ✅ Team performance notes and video uploads
- ✅ YouTube link integration for game analysis

### Reporting & Analytics
- ✅ Automated PDF report generation with performance statistics
- ✅ Email delivery of generated reports
- ✅ Report listing with PDF access
- ✅ Performance statistics tracking:
  - Points per game (PPG)
  - Field goal percentage (FG%)
  - Rebounds
  - Assists
  - Steals and blocks

### Authentication & Security
- ✅ Custom user authentication system (Django AbstractBaseUser)
- ✅ Role-based access control (Player/Coach)
- ✅ JWT token-based authentication (5-minute access token, 1-day refresh token)
- ✅ OTP-based email verification
- ✅ Password reset functionality

### User Management
- ✅ User registration with role assignment
- ✅ Email validation with OTP verification
- ✅ Password management and reset
- ✅ User activation workflow

---

## 🛠️ Tech Stack

### Backend Framework
- **Django 5.2** - Web framework
- **Django REST Framework** - REST API development
- **Django Simple JWT** - Token-based authentication

### Database
- **SQLite3** - Development database (portable)
- *PostgreSQL-ready for production*

### Supporting Libraries
- **Pillow** - Image processing and PDF generation
- **PyOTP** - One-Time Password generation for email verification
- **Django Crontab** - Scheduled task execution
- **Django Filter** - API filtering capabilities
- **White Noise** - Static file serving in production
- **Python 3.9+** - Core language

### Authentication & Security
- **JWT (JSON Web Tokens)** - Stateless authentication
- **PyOTP** - TOTP-based OTP generation
- **Gmail SMTP** - Email delivery

---

## 📁 Project Structure

```
Basketball_Application/
├── manage.py                    # Django management script
├── db.sqlite3                   # SQLite database
├── requirements.txt             # Python dependencies
│
├── Basketball_Application/      # Main project settings
│   ├── __init__.py
│   ├── settings.py             # Project configuration
│   ├── urls.py                 # URL routing
│   ├── asgi.py                 # ASGI configuration
│   └── wsgi.py                 # WSGI configuration
│
├── UserAccount/                 # Authentication & user management
│   ├── models.py               # Custom User model
│   ├── views.py                # Auth endpoints
│   ├── serializers.py          # User serializers
│   ├── urls.py                 # Auth routes
│   ├── utils.py                # Email utility
│   ├── admin.py                # Admin interface
│   ├── tests.py                # Test cases
│   ├── migrations/             # Database migrations
│   └── templates/
│       └── login.html
│
├── Players/                     # Player management
│   ├── models.py               # Player, Report, Scouting models
│   ├── views.py                # Player endpoints
│   ├── serializers.py          # Player serializers
│   ├── urls.py                 # Player routes
│   ├── permission.py           # Custom permissions
│   ├── pdf.py                  # PDF generation
│   ├── admin.py                # Admin interface
│   ├── tests.py                # Test cases
│   ├── migrations/             # Database migrations
│   └── templates/
│       └── report.html
│
├── Coach/                       # Coaching & scouting
│   ├── models.py               # Team & scouting models
│   ├── views.py                # Coach endpoints
│   ├── serializers.py          # Coach serializers
│   ├── urls.py                 # Coach routes
│   ├── admin.py                # Admin interface
│   ├── tests.py                # Test cases
│   └── migrations/             # Database migrations
│
└── media/                       # Uploaded files
    ├── video/%y/               # Game videos organized by year
    └── reports/%Y/%m/%d/       # PDF reports organized by date
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Git
- Virtual environment (venv or virtualenv)
- Gmail account (for email functionality)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Turjo535/BasketBall-App_System.git
cd Basketball_Application
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv myproject
myproject\Scripts\activate

# macOS/Linux
python3 -m venv myproject
source myproject/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Step 5: Run Migrations
```bash
python manage.py migrate
```

### Step 6: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

The API will be available at: `http://localhost:8000/`

---

## ⚙️ Configuration

### Email Configuration (settings.py)
Configure your Gmail account for sending emails:

```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

**Gmail Setup Steps:**
1. Enable 2-factor authentication on your Gmail account
2. Generate an App Password: [Google Account Security](https://myaccount.google.com/apppasswords)
3. Use the generated password in `EMAIL_HOST_PASSWORD`

### JWT Configuration
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',
}
```

### Media Files Configuration
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Serve media files in development (add to main urls.py)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📡 API Documentation

### Base URL
```
http://localhost:8000/
```

### Postman Collection
Import the provided `Basketball_Application.postman_collection.json` for complete API testing.

---

### 🔐 Authentication Endpoints (`/user/`)

#### Register
```
POST /user/register/
Content-Type: application/json

{
    "name": "John Player",
    "email": "john@example.com",
    "phone": "1234567890",
    "password": "SecurePassword123!",
    "role": "player"
}

Response: 201 Created
{
    "message": "User created successfully",
    "user": { ... }
}
```

#### Validate Email & Get OTP
```
POST /user/validate-email/
Content-Type: application/json

{
    "email": "john@example.com"
}

Response: 200 OK
{
    "message": "OTP sent to email"
}
```

#### Verify OTP
```
POST /user/verify-otp/
Content-Type: application/json

{
    "email": "john@example.com",
    "otp": "123456"
}

Response: 200 OK
{
    "message": "Account activated successfully"
}
```

#### Login
```
POST /user/login/
Content-Type: application/json

{
    "email": "john@example.com",
    "password": "SecurePassword123!"
}

Response: 200 OK
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Refresh Token
```
POST /user/token-refresh/
Content-Type: application/json

{
    "refresh": "your-refresh-token"
}

Response: 200 OK
{
    "access": "new-access-token"
}
```

#### Logout
```
POST /user/logout/
Authorization: Bearer {access_token}

Response: 200 OK
{
    "message": "Logout successful"
}
```

#### Change Password
```
POST /user/change-password/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "old_password": "CurrentPassword123!",
    "new_password": "NewPassword123!"
}

Response: 200 OK
{
    "message": "Password changed successfully"
}
```

---

### 🎮 Player Endpoints (`/player/`)

#### Create Player Profile
```
POST /player/playerinfo/
Authorization: Bearer {access_token}
Content-Type: multipart/form-data

{
    "jersey": "23",
    "height": "6'2\"",
    "position": "Guard",
    "class_year": "Senior",
    "game_context": "Regular Season",
    "team": "Lakers",
    "opponent": "Celtics",
    "gender": "Male",
    "tournament": "NBA 2024",
    "performance_note": "Excellent defensive performance",
    "image": <image_file>
}

Response: 201 Created
{
    "id": 1,
    "user": { ... },
    "jersey": "23",
    ...
}
```

#### List All Players
```
GET /player/player-list/
Authorization: Bearer {access_token}

Response: 200 OK
[
    {
        "id": 1,
        "user": { ... },
        "jersey": "23",
        ...
    }
]
```

#### Create Performance Report
```
POST /player/report/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "title": "Game vs Celtics - Performance Analysis",
    "overview": "Strong overall performance with good ball control",
    "projection": "Expected to maintain current form in upcoming games",
    "strength": ["Fast breaks", "Defensive presence", "Three-point shooting"],
    "weaknesses": ["Turnovers", "Rebounding"],
    "points_per_game": 25.5,
    "field_goal_percentage": 45.2,
    "rebounds": 6.0,
    "assists": 8.0,
    "steals_and_blocks": 2.5
}

Response: 201 Created
{
    "id": 1,
    "user": { ... },
    "title": "Game vs Celtics - Performance Analysis",
    ...
    "pdf": null
}
```

#### Get Report Details
```
GET /player/report/{id}/
Authorization: Bearer {access_token}

Response: 200 OK
{
    "id": 1,
    "user": { ... },
    "title": "Game vs Celtics - Performance Analysis",
    ...
}
```

#### Generate PDF Report
```
GET /player/report/{id}/pdf/
Authorization: Bearer {access_token}

Response: 200 OK (File Download)
- PDF file automatically downloaded
```

#### Email PDF Report
```
GET /player/report/{id}/pdf/email/
Authorization: Bearer {access_token}

Response: 200 OK
{
    "message": "PDF report sent to your email"
}
```

#### List PDF Reports
```
GET /player/report/lists/pdf/
Authorization: Bearer {access_token}

Response: 200 OK
[
    {
        "id": 1,
        "title": "Game vs Celtics",
        "pdf": "/media/reports/2024/05/13/report_1.pdf"
    }
]
```

---

### 🎓 Coach Endpoints (`/coach/`)

#### Create Team Information
```
POST /coach/teaminfo/
Authorization: Bearer {access_token}
Content-Type: multipart/form-data

{
    "opponent_team_name": "Boston Celtics",
    "jersey_color": "Green",
    "gender": "Male",
    "circuit_or_level": "NBA",
    "game_date": "2024-05-15T19:00:00Z",
    "performance_note": "Strong defensive team with good 3-point shooters",
    "youtube_link": "https://youtube.com/watch?v=example",
    "uploaded_video": <video_file>
}

Response: 201 Created
{
    "id": 1,
    "opponent_team_name": "Boston Celtics",
    ...
}
```

#### List Team Information
```
GET /coach/teams-list/
Authorization: Bearer {access_token}

Response: 200 OK
[
    {
        "id": 1,
        "opponent_team_name": "Boston Celtics",
        ...
    }
]
```

#### Create Scouting Report
```
POST /coach/scouting/
Authorization: Bearer {access_token}
Content-Type: application/json

{
    "report_title": "Celtics Advanced Scouting Report",
    "overview": "Boston Celtics are a well-rounded team with strong defense",
    "strengths": ["Defense", "Rebounding", "Team Chemistry"],
    "weaknesses": ["Bench depth", "Three-point consistency"],
    "tendencies": "Prefer fast-paced basketball with strong ball movement",
    "key_players": [1, 2, 3]  // IDs of key players
}

Response: 201 Created
{
    "id": 1,
    "report_title": "Celtics Advanced Scouting Report",
    ...
}
```

#### List Scouting Reports
```
GET /coach/teams-scouting/
Authorization: Bearer {access_token}

Response: 200 OK
[
    {
        "id": 1,
        "report_title": "Celtics Advanced Scouting Report",
        ...
    }
]
```

---

## 🔑 Authentication

### JWT Token Flow

1. **Registration & OTP Verification**
   - User registers with name, email, phone, password, and role
   - System sends OTP to email
   - User verifies OTP to activate account

2. **Login**
   - User logs in with email and password
   - System returns `access` and `refresh` tokens

3. **API Requests**
   - Include `Authorization: Bearer {access_token}` header
   - Example: `curl -H "Authorization: Bearer eyJ0eXAi..." http://localhost:8000/player/player-list/`

4. **Token Refresh**
   - When access token expires (5 minutes), use refresh token
   - Send refresh token to `/user/token-refresh/` to get new access token
   - Refresh token valid for 1 day

### Permission System

- **Is_Player**: Restricts endpoints to users with `role='player'`
- **Is_Coach**: Restricts endpoints to users with `role='coach'`
- **IsOwner**: Ensures user owns the resource
- **IsAuthenticated**: Requires valid JWT token

---

## 💡 Usage Examples

### Example 1: Complete Player Workflow

```bash
# 1. Register as a player
curl -X POST http://localhost:8000/user/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Michael Jordan",
    "email": "michael@nba.com",
    "phone": "5551234567",
    "password": "SecurePass123!",
    "role": "player"
  }'

# 2. Validate email (triggers OTP)
curl -X POST http://localhost:8000/user/validate-email/ \
  -H "Content-Type: application/json" \
  -d '{"email": "michael@nba.com"}'
# Check email for OTP

# 3. Verify OTP
curl -X POST http://localhost:8000/user/verify-otp/ \
  -H "Content-Type: application/json" \
  -d '{"email": "michael@nba.com", "otp": "123456"}'

# 4. Login
TOKEN=$(curl -X POST http://localhost:8000/user/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "michael@nba.com", "password": "SecurePass123!"}' \
  | jq -r '.access')

# 5. Create player profile
curl -X POST http://localhost:8000/player/playerinfo/ \
  -H "Authorization: Bearer $TOKEN" \
  -F "jersey=23" \
  -F "height=6'9\"" \
  -F "position=Shooting Guard" \
  -F "class_year=Senior" \
  -F "game_context=Championship" \
  -F "team=Chicago Bulls" \
  -F "opponent=Los Angeles Lakers" \
  -F "gender=Male" \
  -F "tournament=Finals 2024"

# 6. Create performance report
curl -X POST http://localhost:8000/player/report/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Finals Game 1 Performance",
    "overview": "Outstanding performance with 35 points",
    "projection": "Expected MVP consideration",
    "strength": ["Scoring", "Defense", "Leadership"],
    "weaknesses": ["Fouls"],
    "points_per_game": 35.0,
    "field_goal_percentage": 52.0,
    "rebounds": 7.0,
    "assists": 4.0,
    "steals_and_blocks": 2.0
  }'

# 7. Generate PDF report
curl -X GET http://localhost:8000/player/report/1/pdf/ \
  -H "Authorization: Bearer $TOKEN" \
  -o report.pdf

# 8. Email PDF report
curl -X GET http://localhost:8000/player/report/1/pdf/email/ \
  -H "Authorization: Bearer $TOKEN"
```

### Example 2: Coach Scouting Workflow

```bash
# 1. Register as a coach
curl -X POST http://localhost:8000/user/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Phil Jackson",
    "email": "phil@nba.com",
    "phone": "5559876543",
    "password": "SecurePass123!",
    "role": "coach"
  }'

# 2-3. Verify email and OTP (same as player example)

# 4. Login
TOKEN=$(curl -X POST http://localhost:8000/user/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "phil@nba.com", "password": "SecurePass123!"}' \
  | jq -r '.access')

# 5. Create team information
curl -X POST http://localhost:8000/coach/teaminfo/ \
  -H "Authorization: Bearer $TOKEN" \
  -F "opponent_team_name=Los Angeles Lakers" \
  -F "jersey_color=Purple" \
  -F "gender=Male" \
  -F "circuit_or_level=NBA" \
  -F "game_date=2024-05-20T19:00:00Z" \
  -F "performance_note=Balanced team with strong roster" \
  -F "youtube_link=https://youtube.com/watch?v=lakers"

# 6. Create scouting report
curl -X POST http://localhost:8000/coach/scouting/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "report_title": "Lakers Scouting Report",
    "overview": "Strong offensive team with excellent ball movement",
    "strengths": ["Offense", "Three-point shooting", "Depth"],
    "weaknesses": ["Defensive consistency", "Bench stamina"],
    "tendencies": "High-tempo basketball with quick transitions",
    "key_players": [1, 2]
  }'

# 7. View scouting reports
curl -X GET http://localhost:8000/coach/teams-scouting/ \
  -H "Authorization: Bearer $TOKEN"
```

---

## 🗄️ Database Schema

### User Model (Custom)
```python
class User(AbstractBaseUser):
    name = CharField(max_length=100, unique=True)
    email = EmailField(unique=True)
    phone = CharField(max_length=20)
    role = CharField(choices=[('player', 'Player'), ('coach', 'Coach')])
    is_active = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    otp_secret = CharField(max_length=32)
    otp_send_time = DateTimeField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
```

### Player Model
```python
class Player(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    jersey = CharField(max_length=10)
    height = CharField(max_length=10)
    position = CharField(max_length=50)
    class_year = CharField(max_length=50)
    game_context = CharField(max_length=100)
    team = CharField(max_length=100)
    opponent = CharField(max_length=100)
    gender = CharField(max_length=10)
    tournament = CharField(max_length=100)
    performance_note = TextField()
    image = ImageField()
    game_video = FileField(upload_to='video/%y/')
```

### Report_Model
```python
class Report_Model(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    title = TextField(null=True, blank=True)
    overview = TextField()
    projection = TextField()
    strength = JSONField()
    weaknesses = JSONField()
    points_per_game = DecimalField()
    field_goal_percentage = DecimalField()
    rebounds = DecimalField()
    assists = DecimalField()
    steals_and_blocks = DecimalField()
    pdf = FileField(upload_to='reports/%Y/%m/%d/', null=True, blank=True)
```

### Team_Scouting_model
```python
class Team_Scouting_model(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    key_players = ManyToManyField(User, related_name='scouting_reports')
    report_title = CharField(max_length=200)
    overview = TextField()
    strengths = JSONField()
    weaknesses = JSONField()
    tendencies = TextField()
```

---

## 📂 File Management

### Video Storage
- **Location**: `media/video/%y/`
- **Used for**: Player game videos and coach team videos
- **Organization**: Organized by year

### PDF Reports
- **Location**: `media/reports/%Y/%m/%d/`
- **Used for**: Generated performance reports
- **Organization**: Organized by date (year/month/day)

### Profile Images
- **Location**: `media/` (root)
- **Used for**: Player profile pictures

---

## 🔧 Development

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test UserAccount
python manage.py test Players
python manage.py test Coach

# Run with verbose output
python manage.py test --verbosity=2
```

### Database Migrations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations
```

### Django Admin
Access at: `http://localhost:8000/admin`

### Creating Fixtures
```bash
# Export data
python manage.py dumpdata > fixture.json

# Load data
python manage.py loaddata fixture.json
```

### Code Style
- Follow PEP 8 standards
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and modular

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Install dev dependencies
pip install -r requirements.txt

# Run pre-commit hooks (if configured)
pre-commit install
```

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact the development team
- Check existing documentation

---

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Postman Documentation](https://learning.postman.com/)

---

## 📊 Project Statistics

- **Backend Framework**: Django 5.2
- **REST API**: Django REST Framework
- **Authentication**: JWT + OTP
- **Database**: SQLite3 (PostgreSQL-ready)
- **Main Apps**: 3 (UserAccount, Players, Coach)
- **API Endpoints**: 16+ endpoints
- **Supported File Types**: Video, Images, PDF

---

**Last Updated**: May 13, 2026  
**Version**: 1.0.0  
**Status**: Production Ready
