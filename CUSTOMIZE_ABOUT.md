# How to Customize Your About Page

## 📸 Adding Your Profile Photo

### Option 1: Using Static Image (Recommended for URLs under 2.5MB)

1. **Prepare your photo**
   - Take a square photo or crop it to be square (e.g., 400x400 pixels)
   - Save it as `profile.jpg` or `profile.png`

2. **Add the photo to your project**
   - Place your photo in: `portfolio_app/static/img/profile.jpg`
   
3. **Refresh the page**
   - Go to http://127.0.0.1:8003/about/
   - Your photo should now appear in a circular frame!

### Option 2: Using a URL

If you want to use a photo from the internet:

1. Edit `portfolio_app/views.py` (the `about` function)
2. Change the `profile_photo` line to your image URL:
   ```python
   'profile_photo': 'https://example.com/your-photo.jpg',
   ```

---

## ✏️ Customizing Your Bio Text

Edit the file: `templates/portfolio/about.html`

### Section 1: Quick Bio (Top section)
Look for:
```html
<h3 class="mb-3">Hi, I'm Darby!</h3>
```

Replace "Darby" with your name and update the paragraph below with YOUR story.

### Section 2: "My Journey" section
Find the paragraph starting with `<p class="lead text-secondary mb-4">` and replace with your story.

### Section 3: Skills sections
Update the skill lists in these sections:
- 🤖 AI & Machine Learning
- 💻 Backend & Tools
- 🎨 Frontend & Design
- 🚀 Learning Focus

### Section 4: My Philosophy
Update the quote and philosophy paragraph.

---

## 🎨 Example Customization

**Before:**
```html
<h3 class="mb-3">Hi, I'm Darby!</h3>
<p class="lead text-secondary mb-4">
    👋 Welcome to my AI Innovation Portfolio! I'm a passionate developer...
</p>
```

**After:**
```html
<h3 class="mb-3">Hi, I'm Your Name!</h3>
<p class="lead text-secondary mb-4">
    👋 I'm a software engineer based in [City], specialized in building AI-powered applications.
</p>
```

---

## 📁 File Locations

When editing:
- **Template:** `templates/portfolio/about.html`
- **View Logic:** `portfolio_app/views.py`
- **Profile Photo:** `portfolio_app/static/img/profile.jpg`

After editing, just refresh the page—Django will automatically reload the changes!

---

## 💡 Tips

- Keep your bio natural and authentic
- Use emojis sparingly but effectively
- Match the tone with your portfolio vibe
- The page looks best with a clean, square profile photo
- Update your skills list as you learn new things!

Good luck! 🚀
