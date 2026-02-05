# Wilson Maina - Personal Portfolio Website

A professional personal portfolio website built with Django, showcasing skills, projects, and experience. Features a custom admin dashboard for managing portfolio content without using Django's built-in admin panel.

## 🎯 Features

### Frontend

- **Home Page**: Hero section with call-to-action buttons, featured projects, and quick stats
- **About Page**: Detailed bio, skills with proficiency levels, and learning journey timeline
- **Projects Page**: Display of portfolio projects with filtering by technology
- **Project Detail Page**: Comprehensive project information with links to GitHub and live demos
- **Contact Page**: Contact form that stores messages in the database
- **Responsive Design**: Mobile-friendly layout using Bootstrap 5
- **Modern UI**: Beautiful gradient backgrounds, smooth animations, and clean typography

### Admin Dashboard

- **Custom Dashboard**: Secure, login-protected admin area at `/dashboard/`
- **Projects Management**: Create, read, update, and delete projects
- **Skills Management**: Manage skills by category with proficiency levels
- **About Section**: Edit personal information, bio, interests, and profile photo
- **Contact Messages**: View and manage messages received from the contact form
- **User Authentication**: Django's built-in authentication with staff-only access

## 📋 Project Structure

```
portfolio2/
├── accounts/                    # Authentication app
│   ├── views.py                # Login/logout views
│   ├── urls.py                 # Auth URLs
│   └── migrations/
├── portfolio/                   # Main portfolio app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # URL routing
│   └── migrations/
├── portfolio_config/            # Project settings
│   ├── settings.py             # Django configuration
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── templates/                   # HTML templates
│   ├── base.html               # Base template with navbar and footer
│   ├── portfolio/              # Frontend templates
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── projects.html
│   │   ├── project_detail.html
│   │   └── contact.html
│   ├── accounts/               # Auth templates
│   │   └── admin_login.html
│   └── dashboard/              # Admin dashboard templates
│       ├── dashboard.html
│       ├── projects_manage.html
│       ├── project_form.html
│       ├── skills_manage.html
│       ├── skill_form.html
│       ├── about_manage.html
│       ├── messages.html
│       └── message_detail.html
├── static/                      # Static files
│   ├── css/
│   │   └── style.css           # Custom CSS
│   ├── js/
│   │   └── script.js           # Custom JavaScript
│   └── images/                 # Static images
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .env.example                # Environment variables example
└── README.md                   # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support

### Step 1: Clone or Navigate to Project

```bash
cd "/path/to/portfolio 2"
```

### Step 2: Activate Virtual Environment

The virtual environment should already be created. Activate it:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `django-dotenv` is not installed:

```bash
pip install python-dotenv
```

### Step 4: Setup Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```bash
cp .env.example .env
```

Edit `.env` and update with your settings:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

To generate a secure SECRET_KEY:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Run Migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create a Superuser (Admin)

Create an admin account for the dashboard:

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:

- Username
- Email
- Password

Example:

```
Username: admin
Email: admin@example.com
Password: ••••••••
```

### Step 7: Collect Static Files (Optional)

For development, Django serves static files automatically. For production:

```bash
python manage.py collectstatic
```

### Step 8: Run Development Server

Start the development server:

```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

## 🚀 Accessing the Application

### Frontend Pages

- **Home**: http://127.0.0.1:8000/
- **About**: http://127.0.0.1:8000/about/
- **Projects**: http://127.0.0.1:8000/projects/
- **Contact**: http://127.0.0.1:8000/contact/

### Admin Dashboard

- **Login**: http://127.0.0.1:8000/auth/login/
- **Dashboard**: http://127.0.0.1:8000/dashboard/

Use the superuser credentials you created in Step 6.

## 📝 Managing Content

### Adding Projects

1. Log in to the dashboard
2. Click "Add New Project" or go to Projects Management
3. Fill in:
   - Project Title
   - Short Description
   - Technologies (comma-separated)
   - Long Description (optional)
   - GitHub URL (optional)
   - Live Demo URL (optional)
   - Project Image
4. Click "Create Project"

### Managing Skills

1. Go to Dashboard → Manage Skills
2. Click "Add New Skill"
3. Enter:
   - Skill Name (e.g., Python, Django, JavaScript)
   - Category (Programming Language, Framework, Tool, Database)
   - Proficiency Level (1-100)
4. Click "Add Skill"

### Editing About Section

1. Go to Dashboard → Edit About
2. Update:
   - Full Name
   - Role/Title
   - Institution
   - Bio
   - Interests
   - Experience Level
   - Profile Photo
3. Click "Update About Section"

### Viewing Contact Messages

1. Go to Dashboard → View Messages
2. Click on a message to view details
3. Click "Reply via Email" to respond
4. Delete messages as needed

## 🎨 Customization

### Update Personal Information

Edit the `About` model in Django admin or through the dashboard:

- Change name, role, institution
- Update bio and interests
- Upload a profile photo

### Customize Styling

Edit `static/css/style.css` to change:

- Colors (modify CSS variables in `:root`)
- Fonts (update `font-family`)
- Spacing and sizing
- Animations

Key CSS Variables:

```css
--primary-color: #667eea;
--secondary-color: #764ba2;
--dark-color: #2d3748;
--light-color: #f7fafc;
```

### Update Navigation

Edit `templates/base.html` to:

- Add/remove navigation links
- Change logo or branding
- Modify social media links
- Update footer content

### Customize Templates

All HTML templates are in the `templates/` directory:

- Frontend templates in `templates/portfolio/`
- Dashboard templates in `templates/dashboard/`
- Shared templates in `templates/includes/`

## 🔐 Security Notes

### For Production:

1. **Set DEBUG to False**:

   ```
   DEBUG=False
   ```

2. **Generate a secure SECRET_KEY**:

   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

3. **Update ALLOWED_HOSTS**:

   ```python
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Enable HTTPS**:

   ```
   SECURE_SSL_REDIRECT=True
   SESSION_COOKIE_SECURE=True
   CSRF_COOKIE_SECURE=True
   ```

5. **Use environment variables for sensitive data**:
   - Never commit `.env` files
   - Use `.env.example` as a template

6. **Change default passwords**:
   - Update superuser password regularly

## 📦 Database Models

### About

Stores personal information displayed on the About page.

```python
- name (CharField)
- role (CharField)
- institution (CharField)
- bio (TextField)
- interests (TextField)
- experience_level (CharField)
- profile_image (ImageField)
- updated_at (DateTimeField)
```

### Skill

Stores skills organized by category with proficiency levels.

```python
- name (CharField)
- category (CharField) - Programming Language, Framework, Tool, Database
- proficiency (IntegerField) - 1-100
- order (IntegerField) - for sorting
```

### Project

Stores portfolio projects with detailed information.

```python
- title (CharField)
- description (TextField)
- long_description (TextField)
- image (ImageField)
- technologies (CharField)
- github_url (URLField)
- live_url (URLField)
- order (IntegerField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### ContactMessage

Stores messages from the contact form.

```python
- name (CharField)
- email (EmailField)
- message (TextField)
- created_at (DateTimeField)
- is_read (BooleanField)
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'django'"

**Solution**: Ensure virtual environment is activated and dependencies are installed:

```bash
pip install -r requirements.txt
```

### Issue: "No such table: portfolio_project"

**Solution**: Run migrations:

```bash
python manage.py migrate
```

### Issue: "Static files not loading (404 errors)"

**Solution**: Ensure DEBUG=True in development or run:

```bash
python manage.py collectstatic
```

### Issue: "Login redirect loop"

**Solution**: Ensure the login URL is correct in `accounts/views.py` and settings are configured properly.

## 📚 Technologies Used

- **Backend**: Django 4.2
- **Database**: SQLite (development), can be changed to PostgreSQL for production
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Image Handling**: Pillow

## 🌟 Features Implemented

✅ Responsive design with Bootstrap  
✅ Custom admin dashboard  
✅ CRUD operations for projects  
✅ Skills management with proficiency levels  
✅ Contact form with database storage  
✅ Project showcase with filtering  
✅ About section management  
✅ User authentication  
✅ Modern UI with animations  
✅ Mobile-friendly layout  
✅ Placeholder image support  
✅ CSRF protection  
✅ Message management system  
✅ Custom CSS and JavaScript

## 📞 Contact & Support

For issues or questions, please refer to the Django documentation:

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Font Awesome Icons](https://fontawesome.com/icons/)

## 📄 License

This project is personal and can be customized freely.

---

**Version**: 1.0.0  
**Last Updated**: February 2026  
**Author**: Wilson Maina Njuguna  
**Institution**: Kirinyaga University
