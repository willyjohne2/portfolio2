# 🚀 Quick Start Guide - Portfolio Website

## Installation (5 minutes)

### Step 1: Navigate to Project

```bash
cd "path/to/portfolio 2"
```

### Step 2: Activate Virtual Environment

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Setup Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Admin User

```bash
python manage.py createsuperuser
```

Example:

- Username: `admin`
- Email: `admin@example.com`
- Password: Choose a secure password

Or use the pre-created account:

- Username: `admin`
- Password: `admin123`

### Step 6: Run Development Server

```bash
python manage.py runserver
```

## 🌐 Access the Website

- **Frontend**: http://127.0.0.1:8000/
- **Admin Dashboard**: http://127.0.0.1:8000/auth/login/
- **Home**: http://127.0.0.1:8000/
- **About**: http://127.0.0.1:8000/about/
- **Projects**: http://127.0.0.1:8000/projects/
- **Contact**: http://127.0.0.1:8000/contact/

## 📝 Common Tasks

### Add a Project

1. Log in to dashboard: http://127.0.0.1:8000/auth/login/
2. Click **"Add New Project"**
3. Fill in:
   - Title
   - Description
   - Technologies (comma-separated)
   - Upload image (optional)
   - GitHub URL (optional)
   - Live URL (optional)
4. Click **"Create Project"**

### Add a Skill

1. Go to Dashboard → **"Manage Skills"**
2. Click **"Add New Skill"**
3. Fill in:
   - Skill name (e.g., Python, Django)
   - Category (Language, Framework, Tool, Database)
   - Proficiency (1-100 slider)
4. Click **"Add Skill"**

### Update About Section

1. Go to Dashboard → **"Edit About"**
2. Update:
   - Full Name
   - Role
   - Institution
   - Bio
   - Interests
   - Profile Photo
3. Click **"Update About Section"**

### View Contact Messages

1. Go to Dashboard → **"View Messages"**
2. Click on a message to see details
3. Click **"Reply via Email"** to respond

## 📁 File Structure

Important files to know:

- `manage.py` - Django management script
- `templates/` - HTML templates
- `static/` - CSS, JavaScript, images
- `portfolio/models.py` - Database models
- `portfolio/views.py` - View functions
- `portfolio/urls.py` - URL routing
- `portfolio_config/settings.py` - Django settings
- `db.sqlite3` - SQLite database (created after migration)

## 🎨 Customization

### Change Colors

Edit `static/css/style.css`:

```css
:root {
  --primary-color: #667eea;
  --secondary-color: #764ba2;
}
```

### Update Navigation

Edit `templates/base.html` - modify the navbar section

### Change Content

Edit `templates/portfolio/*.html` files

## ⚠️ Important Notes

1. **Development Only**: The current setup is for development. For production, update:
   - `DEBUG=False` in `.env`
   - Generate a new `SECRET_KEY`
   - Change admin password
   - Update `ALLOWED_HOSTS`

2. **Static Files**: In development, Django serves them automatically. For production:

   ```bash
   python manage.py collectstatic
   ```

3. **Images**:
   - Save project images in `media/projects/`
   - Save profile image in `media/profile/`
   - Use placeholder images (via.placeholder.com) by default

4. **Database**:
   - SQLite is fine for development
   - For production, use PostgreSQL or MySQL

## 🐛 Troubleshooting

### "No module named 'django'"

```bash
pip install -r requirements.txt
```

### "No such table: portfolio_project"

```bash
python manage.py migrate
```

### "Port 8000 is already in use"

```bash
python manage.py runserver 8001
```

### Template not found

Ensure templates directory structure matches the expected paths

### Static files not loading

Make sure `DEBUG=True` in development, or run:

```bash
python manage.py collectstatic
```

## 📚 Further Customization

### Add More Pages

1. Create view in `portfolio/views.py`
2. Create template in `templates/portfolio/`
3. Add URL route in `portfolio/urls.py`
4. Add navbar link in `templates/base.html`

### Add More Fields to Projects

1. Edit `portfolio/models.py`
2. Create migration: `python manage.py makemigrations`
3. Apply migration: `python manage.py migrate`
4. Update form in `templates/dashboard/project_form.html`

### Style with Custom CSS

Add custom styles to `static/css/style.css`

## 🔒 Security Tips

- Never commit `.env` files with sensitive data
- Change default admin password immediately
- Use environment variables for secret keys
- Enable HTTPS in production
- Keep Django and dependencies updated

## 📞 Need Help?

- Django docs: https://docs.djangoproject.com/
- Bootstrap docs: https://getbootstrap.com/docs/
- Font Awesome: https://fontawesome.com/icons/

---

Happy coding! 🎉
