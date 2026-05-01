from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.mail import send_mail
from django.contrib import messages
from .models import AIProject


def project_list(request):
    """
    Display all published AI projects in a gallery view (homepage).
    
    This function-based view:
    - Queries only published projects from the database
    - Sorts them by newest first (thanks to our model's Meta ordering)
    - Passes them to the template for Bootstrap card rendering
    
    URL: / (home page)
    Template: portfolio/project_list.html
    """
    # Get all published projects, ordered by newest first
    projects = AIProject.objects.filter(is_published=True)
    
    # Prepare context dictionary to pass to template
    context = {
        'projects': projects,
        'project_count': projects.count(),  # Show how many projects we have
    }
    
    # Render the template with the context
    return render(request, 'portfolio/project_list.html', context)


def project_detail(request, slug):
    """
    Display a single AI project with full details.
    
    This function-based view:
    - Fetches a specific project by its URL-friendly slug
    - Returns a 404 error if the project doesn't exist
    - Shows full description, media (image/video), and metadata
    
    URL: /projects/<slug>/ (e.g., /projects/multi-agent-news-scraper/)
    Template: portfolio/project_detail.html
    
    Args:
        slug (str): The URL-friendly identifier for the project
    """
    # Get the project by slug, or raise 404 if not found
    project = get_object_or_404(AIProject, slug=slug, is_published=True)
    
    # Prepare context with the project details
    context = {
        'project': project,
    }
    
    # Render the detail template
    return render(request, 'portfolio/project_detail.html', context)


def about(request):
    """
    Display the About Me page.
    
    This page tells your story - who you are, your background, interests, 
    and what drives you in AI and tech.
    
    URL: /about/
    Template: portfolio/about.html
    """
    context = {
        'page_title': 'About Me',
        'profile_photo': '/static/img/profile.jpg',  # Path to your profile photo
    }
    return render(request, 'portfolio/about.html', context)


def contact(request):
    """
    Display the Contact page with a contact form.
    
    This function-based view:
    - Displays a contact form on GET requests
    - Processes form submission on POST requests
    - Sends an email notification when someone reaches out
    
    URL: /contact/
    Template: portfolio/contact.html
    """
    if request.method == 'POST':
        # Extract form data from POST request
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message_text = request.POST.get('message', '')
        
        # Basic validation
        if name and email and subject and message_text:
            try:
                # Send email notification (configure in settings.py)
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=f"From: {name} ({email})\n\n{message_text}",
                    from_email=email,
                    recipient_list=['darbyfra@gmail.com'],  # Change to your email
                    fail_silently=False,
                )
                # Show success message
                messages.success(request, "✨ Thanks for reaching out! I'll get back to you soon.")
            except Exception as e:
                # Show error message if email fails
                messages.error(request, "Oops! There was an issue sending your message. Please try again.")
        else:
            # Show validation error
            messages.error(request, "Please fill out all fields.")
    
    context = {
        'page_title': 'Contact Me',
    }
    return render(request, 'portfolio/contact.html', context)
