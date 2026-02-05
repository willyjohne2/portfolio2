# 🎓 Wilson Maina - Personal Portfolio Website

## Complete Implementation Guide

---

## 📖 Table of Contents

1. [Project Overview](#project-overview)
2. [What's Included](#whats-included)
3. [Quick Start](#quick-start)
4. [File Structure](#file-structure)
5. [Features Overview](#features-overview)
6. [Admin Dashboard Guide](#admin-dashboard-guide)
7. [Customization Guide](#customization-guide)
8. [Troubleshooting](#troubleshooting)
9. [Production Deployment](#production-deployment)

---

## 📌 Project Overview

This is a **professional personal portfolio website** built with:

- **Backend**: Django 4.2 (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (easily switchable to PostgreSQL)
- **Icons**: Font Awesome 6
- **Admin Panel**: Custom dashboard (no Django admin)

**Created for**: Wilson Maina Njuguna  
**Institution**: Kirinyaga University (2nd Year Software Engineering)

---

## ✨ What's Included

### ✅ Pages

- Home (hero, projects preview, skills)
- About (bio, skills with proficiency bars, timeline)
- Projects (project gallery)
- Project Details (full project information)
- Contact (contact form)
- Admin Login
- Admin Dashboard

### ✅ Admin Features

- Project CRUD (Create, Read, Update, Delete)
- Skills Management
- About Section Editing
- Contact Messages Viewing

### ✅ Design Features

- Responsive design (mobile, tablet, desktop)
- Professional color scheme (purple gradient)
- Smooth animations
- Modern UI components
- Placeholder image support

### ✅ Technical Features

- CSRF protection
- User authentication
- Form validation
- Image upload
- Database models
- Environment variables

---

## 🚀 Quick Start

### 1. Navigate to Project

```bash
cd "path/to/portfolio 2"
```

### 2. Activate Virtual Environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (if needed)

```bash
python manage.py createsuperuser
```

Or use pre-created: `admin` / `admin123`

### 6. Start Server

```bash
python manage.py runserver
```

### 7. Visit Website

- **Frontend**: http://127.0.0.1:8000/
- **Dashboard**: http://127.0.0.1:8000/auth/login/

---

## 📂 File Structure

```
portfolio2/
│
├── accounts/                      # Authentication app
│   ├── views.py                  # Login/logout views
│   ├── urls.py                   # Auth URLs
│   ├── models.py                 # AdminProfile model
│   └── migrations/
│
├── portfolio/                     # Main app
│   ├── models.py                 # Database models
│   ├── views.py                  # All views (frontend + dashboard)
│   ├── urls.py                   # URL routing
│   └── migrations/
│
├── portfolio_config/             # Project settings
│   ├── settings.py              # Django configuration
│   ├── urls.py                  # Main URL config
│   ├── wsgi.py                  # WSGI config
│   └── asgi.py                  # ASGI config
│
├── templates/                    # HTML templates
│   ├── base.html               # Base template (navbar + footer)
│   ├── portfolio/              # Frontend templates
│   │   ├── index.html         # Home page
│   │   ├── about.html         # About page
│   │   ├── projects.html      # Projects listing
│   │   ├── project_detail.html # Project details
│   │   └── contact.html       # Contact form
│   ├── accounts/              # Auth templates
│   │   └── admin_login.html   # Login page
│   └── dashboard/             # Admin dashboard
│       ├── dashboard.html
│       ├── projects_manage.html
│       ├── project_form.html
│       ├── skills_manage.html
│       ├── skill_form.html
│       ├── about_manage.html
│       ├── messages.html
│       └── message_detail.html
│
├── static/                      # Static files
│   ├── css/
│   │   └── style.css          # Custom CSS (500+ lines)
│   ├── js/
│   │   └── script.js          # Custom JS (400+ lines)
│   └── images/                # Placeholder images
│
├── manage.py                    # Django management
├── requirements.txt             # Dependencies
├── .env.example                # Environment template
├── README.md                   # Full documentation
├── QUICK_START.md             # Quick guide
├── IMPLEMENTATION_SUMMARY.md  # What was built
├── setup.sh                   # Linux/macOS setup
└── setup.bat                  # Windows setup
```

---

## 🎯 Features Overview

### Frontend Pages

#### 🏠 Home Page

- Hero section with name and intro
- Call-to-action buttons
- Featured projects showcase
- Skills preview by category
- Statistics cards
- Call-to-action section

#### 👤 About Page

- Profile photo
- Personal information
- Full bio
- Skills with proficiency bars
- Learning journey timeline
- Interests and experience level

#### 📁 Projects Page

- Project cards grid
- Project images
- Tech stack badges
- Links to GitHub and live demos
- Responsive layout

#### 📄 Project Detail Page

- Large project image
- Full description
- Technologies used
- GitHub link
- Live demo link
- Related projects
- Breadcrumb navigation

#### ✉️ Contact Page

- Contact form with validation
- Contact information
- Social media links
- Bootstrap form styling

### Admin Dashboard

#### 📊 Dashboard Home

- Statistics overview
- Quick action buttons
- Feature descriptions

#### 📚 Projects Management

- List all projects
- Create new project
- Edit project details
- Delete project
- Image upload support
- Tech stack editing

#### ⭐ Skills Management

- Skill cards with proficiency bars
- Add new skill
- Edit skill
- Delete skill
- Category selection
- Proficiency slider (1-100)

#### 👥 About Section

- Edit personal information
- Update bio and interests
- Change profile photo
- Upload new image

#### 💬 Contact Messages

- View all messages
- Message cards with preview
- Mark as read
- View full message
- Reply via email
- Delete messages

---

## 🔧 Admin Dashboard Guide

### Accessing the Dashboard

1. Navigate to: http://127.0.0.1:8000/auth/login/
2. Enter credentials:
   - Username: `admin`
   - Password: `admin123` (or your custom password)
3. Click "Login"
4. You'll be redirected to dashboard

### Managing Projects

**To Add a Project:**

1. Click "Add New Project" on dashboard or projects page
2. Fill in all fields:
   - Title
   - Short description
   - Long description (optional)
   - Technologies (comma-separated)
   - GitHub URL (optional)
   - Live URL (optional)
   - Project image
3. Click "Create Project"

**To Edit a Project:**

1. Go to "Manage Projects"
2. Click "Edit" on any project
3. Modify fields
4. Click "Update Project"

**To Delete a Project:**

1. Go to "Manage Projects"
2. Click "Delete" (confirm deletion)

### Managing Skills

**To Add a Skill:**

1. Go to "Manage Skills"
2. Click "Add New Skill"
3. Enter:
   - Skill name (e.g., Django)
   - Category (Language/Framework/Tool/Database)
   - Proficiency (use slider)
4. Click "Add Skill"

**To Edit a Skill:**

1. Go to "Manage Skills"
2. Click "Edit" on skill
3. Update information
4. Click "Update Skill"

### Editing About Section

1. Click "Edit About"
2. Update fields:
   - Name
   - Role/Title
   - Institution
   - Bio
   - Interests
   - Experience Level
   - Profile Photo
3. Click "Update About Section"

### Managing Contact Messages

**To View Messages:**

1. Click "View Messages"
2. Browse all messages (newest first)
3. Unread messages marked with "NEW" badge

**To Read a Message:**

1. Click "View" on any message
2. See full message details
3. Message automatically marked as read

**To Reply:**

1. Click "Reply via Email"
2. Reply in your email client

**To Delete:**

1. Click "Delete"
2. Confirm deletion

---

## 🎨 Customization Guide

### Change Colors

Edit `static/css/style.css`:

```css
:root {
  --primary-color: #667eea; /* Main purple */
  --secondary-color: #764ba2; /* Dark purple */
  --dark-color: #2d3748; /* Text color */
  --light-color: #f7fafc; /* Light bg */
}
```

### Update Personal Information

**Option 1: Via Dashboard**

1. Log in to dashboard
2. Click "Edit About"
3. Update all fields
4. Click "Update About Section"

**Option 2: Via Database**

```bash
python manage.py shell
```

```python
from portfolio.models import About
about = About.objects.first()
about.name = "Your Name"
about.bio = "Your bio"
about.save()
```

### Customize Navbar

Edit `templates/base.html`:

- Change brand/logo
- Add/remove navigation links
- Modify styling classes

### Update Footer

Edit `templates/base.html`:

- Change contact information
- Add social media links
- Update copyright

### Modify Homepage

Edit `templates/portfolio/index.html`:

- Change hero section text
- Update featured projects display
- Modify statistics
- Change CTA section

### Add New Page

1. Create view in `portfolio/views.py`:

```python
def my_page(request):
    return render(request, 'portfolio/my_page.html')
```

2. Create template `templates/portfolio/my_page.html`

3. Add URL in `portfolio/urls.py`:

```python
path('my-page/', views.my_page, name='my_page'),
```

4. Add link in `templates/base.html` navbar

### Style with CSS

Add to `static/css/style.css`:

```css
.my-class {
  background: #667eea;
  padding: 1rem;
  border-radius: 0.5rem;
}
```

---

## 🐛 Troubleshooting

### Error: "No module named 'django'"

**Solution:**

```bash
pip install -r requirements.txt
```

### Error: "No such table: portfolio_project"

**Solution:**

```bash
python manage.py migrate
```

### Error: "Port 8000 already in use"

**Solution:**

```bash
python manage.py runserver 8001
```

### Static files not loading (CSS/JS 404)

**Solution:**

1. Ensure `DEBUG=True` in development
2. Check file paths
3. Clear browser cache
4. Restart server

### Images not displaying

**Solution:**

1. Check image upload path
2. Verify file exists in `media/` folder
3. Use placeholder images if needed

### Login redirect loop

**Solution:**

1. Ensure user is marked as `is_staff=True`
2. Check login URL configuration
3. Clear session cookies

---

## 🚀 Production Deployment

### Security Checklist

- [ ] Change SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Update ALLOWED_HOSTS
- [ ] Change admin password
- [ ] Enable HTTPS
- [ ] Set secure cookie settings
- [ ] Create .env file (don't commit)
- [ ] Use PostgreSQL instead of SQLite

### Environment Setup

Create `.env` file:

```
SECRET_KEY=your-secure-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### Generate Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Collect Static Files

```bash
python manage.py collectstatic
```

### Switch to PostgreSQL

1. Install: `pip install psycopg2-binary`
2. Update settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Use Gunicorn

```bash
pip install gunicorn
gunicorn portfolio_config.wsgi
```

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [Font Awesome Icons](https://fontawesome.com/icons/)
- [Python Documentation](https://docs.python.org/)

---

## 🎉 You're Ready!

Your professional portfolio website is now fully functional.

### Next Steps:

1. ✅ Customize with your content
2. ✅ Add your projects
3. ✅ Update about section
4. ✅ Add skills
5. ✅ Deploy to production
6. ✅ Share your portfolio!

### Support:

- Refer to README.md for detailed documentation
- Check QUICK_START.md for common tasks
- Review IMPLEMENTATION_SUMMARY.md for feature list

---

**Happy Coding! 🚀**

_Portfolio Website | Django | Python | Bootstrap | JavaScript_

Last Updated: February 2026
