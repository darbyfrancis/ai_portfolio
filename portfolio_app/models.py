from django.db import models
from django.utils.text import slugify

# AIProject Model - Stores information about your AI projects and experiments
class AIProject(models.Model):
    """
    Represents an AI-driven project or experiment.
    This model stores all the details needed to showcase your work on the portfolio.
    """
    
    # Category choices - defines what type of AI project this is
    CATEGORY_CHOICES = [
        ('agents', 'AI Agents'),
        ('generative_video', 'Generative Video'),
        ('generative_image', 'Generative Image'),
        ('django_web_app', 'Django Web App'),
        ('nlp', 'NLP & Language Models'),
        ('computer_vision', 'Computer Vision'),
        ('other', 'Other AI Project'),
    ]
    
    # Title of the project (e.g., "Multi-Agent News Scraper")
    title = models.CharField(
        max_length=200,
        help_text="Name of your AI project or tool"
    )
    
    # What type of project is this?
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='other',
        help_text="Choose the category that best describes this project"
    )
    
    # Plain English explanation of how it works
    description = models.TextField(
        help_text="Explain what this project does and how you built it (vibe coding style!)"
    )
    
    # One-sentence summary of the project
    summary = models.CharField(
        max_length=255,
        blank=True,
        help_text="Quick one-line description of the project"
    )
    
    # Business problem this project solves
    business_problem = models.TextField(
        blank=True,
        help_text="What problem does this project solve?"
    )
    
    # Tools and technologies used (comma-separated or newline-separated)
    tools_used = models.TextField(
        blank=True,
        help_text="List the tools and technologies used (Python, TensorFlow, OpenAI, etc.)"
    )
    
    # Key features of the project
    key_features = models.TextField(
        blank=True,
        help_text="Bullet points or paragraphs describing key features"
    )
    
    # Your specific role and contribution
    your_role = models.TextField(
        blank=True,
        help_text="What was your specific role and contribution to this project?"
    )
    
    # The biggest challenge faced
    challenge = models.TextField(
        blank=True,
        help_text="What was the biggest challenge you faced?"
    )
    
    # What you learned from the project
    lessons_learned = models.TextField(
        blank=True,
        help_text="What did you learn from building this project?"
    )
    
    # Optional: Featured image for the project card
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Upload a screenshot or hero image for this project"
    )
    
    # Optional: Link to embedded video (YouTube, Vimeo, etc.)
    video_url = models.URLField(
        blank=True,
        null=True,
        help_text="Paste an embed URL for a video demo (e.g., YouTube embed link)"
    )
    
    # Optional: Upload a video file directly (MP4, WebM, etc.)
    # Note: You can use either video_url OR video_file, or both!
    video_file = models.FileField(
        upload_to='projects/videos/',
        blank=True,
        null=True,
        help_text="Upload a video file (MP4, WebM, MOV, etc.) instead of a URL"
    )
    
    # Optional: Link to GitHub repository for this project
    github_url = models.URLField(
        blank=True,
        null=True,
        help_text="Link to the GitHub repository for this project"
    )
    
    # Optional: Link to deployed project (e.g., Render, Vercel, Heroku, etc.)
    deployed_url = models.URLField(
        blank=True,
        null=True,
        help_text="Link to the live deployed version (e.g., Render, Vercel)"
    )
    
    # When was this project created?
    created_at = models.DateTimeField(auto_now_add=True)
    
    # When was it last updated?
    updated_at = models.DateTimeField(auto_now=True)
    
    # URL-friendly version of the title (for better URLs)
    slug = models.SlugField(
        unique=True,
        blank=True,
        help_text="Auto-generated URL-friendly name"
    )
    
    # Show on homepage? (useful for drafts or archived projects)
    is_published = models.BooleanField(
        default=True,
        help_text="Check to display this project on the gallery"
    )
    
    class Meta:
        ordering = ['-created_at']  # Show newest projects first
        verbose_name = 'AI Project'
        verbose_name_plural = 'AI Projects'
    
    def save(self, *args, **kwargs):
        """
        Auto-generate slug from title when saving.
        This ensures URL-friendly names without manual entry.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        """
        What appears in Django admin list view.
        Returns the project title so you can easily identify projects.
        """
        return self.title


class Skill(models.Model):
    """
    Represents a skill or technology you're proficient in.
    Used to display on the Skills page.
    """
    
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    # Name of the skill (e.g., "Python", "Django", "OpenAI")
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the skill or technology"
    )
    
    # Category of the skill
    category = models.CharField(
        max_length=50,
        choices=[
            ('programming', 'Programming Languages'),
            ('frameworks', 'Frameworks & Libraries'),
            ('ai_ml', 'AI & Machine Learning'),
            ('databases', 'Databases'),
            ('tools', 'Tools & Platforms'),
            ('other', 'Other'),
        ],
        default='tools',
        help_text="Category this skill belongs to"
    )
    
    # Your proficiency level
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES,
        default='intermediate',
        help_text="Your proficiency level with this skill"
    )
    
    # Years of experience (optional)
    years_experience = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        help_text="Years of experience with this skill"
    )
    
    # Display order on the page
    order = models.IntegerField(
        default=0,
        help_text="Order to display skills on the page (0 = default order)"
    )
    
    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"
