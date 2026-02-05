#!/bin/bash
# Portfolio Project Setup Script

set -e

echo "🚀 Portfolio Project Setup"
echo "=========================="
echo ""

# Check if in the correct directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found. Please run this script from the project root directory."
    exit 1
fi

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "✓ .env file created. Please update it with your settings."
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🔄 Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser if needed
echo ""
echo "👤 Creating admin user..."
python manage.py shell << EOF
from django.contrib.auth.models import User
from portfolio.models import About, Skill, Project

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✓ Superuser created: username='admin', password='admin123'")
else:
    print("✓ Superuser 'admin' already exists")

# Create About section if it doesn't exist
if not About.objects.exists():
    About.objects.create(
        name="Wilson Maina Njuguna",
        role="Software Engineering Student",
        institution="Kirinyaga University"
    )
    print("✓ About section created")

print("\n✅ Database initialization completed!")
EOF

# Collect static files (optional for production)
echo ""
echo "📁 Optional: Collecting static files..."
echo "  Run: python manage.py collectstatic"

echo ""
echo "✅ Setup completed!"
echo ""
echo "📋 Next steps:"
echo "  1. Start the development server:"
echo "     python manage.py runserver"
echo ""
echo "  2. Visit the application:"
echo "     http://127.0.0.1:8000/"
echo ""
echo "  3. Login to admin dashboard:"
echo "     http://127.0.0.1:8000/auth/login/"
echo "     Username: admin"
echo "     Password: admin123"
echo ""
echo "⚠️  Important: Change the admin password in production!"
echo ""
