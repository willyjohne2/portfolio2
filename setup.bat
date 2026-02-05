@echo off
REM Portfolio Project Setup Script for Windows

echo.
echo 🚀 Portfolio Project Setup
echo ==========================
echo.

REM Check if in the correct directory
if not exist "manage.py" (
    echo ❌ Error: manage.py not found. Please run this script from the project root directory.
    pause
    exit /b 1
)

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo 📝 Creating .env file...
    copy .env.example .env
    echo ✓ .env file created. Please update it with your settings.
)

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo 📦 Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Run migrations
echo 🔄 Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Create superuser if needed
echo.
echo 👤 Creating admin user...
python manage.py shell < setup_admin.py

REM Display next steps
echo.
echo ✅ Setup completed!
echo.
echo 📋 Next steps:
echo   1. Start the development server:
echo      python manage.py runserver
echo.
echo   2. Visit the application:
echo      http://127.0.0.1:8000/
echo.
echo   3. Login to admin dashboard:
echo      http://127.0.0.1:8000/auth/login/
echo      Username: admin
echo      Password: admin123
echo.
echo ⚠️  Important: Change the admin password in production!
echo.
pause
