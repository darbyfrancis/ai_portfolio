"""
URL configuration for the portfolio_app.

This file defines all the URL routes for displaying projects on the portfolio.
"""
from django.urls import path
from . import views

app_name = 'portfolio'  # Namespace for reverse() lookups (e.g., 'portfolio:project_list')

urlpatterns = [
    # Gallery / Home page - shows all published projects
    # URL: http://yoursite.com/
    path('', views.project_list, name='project_list'),
    
    # Project detail page - shows full details for one project
    # URL: http://yoursite.com/projects/project-slug/
    # Example: http://yoursite.com/projects/multi-agent-news-scraper/
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    
    # About Me page
    # URL: http://yoursite.com/about/
    path('about/', views.about, name='about'),
    
    # Contact page with form
    # URL: http://yoursite.com/contact/
    path('contact/', views.contact, name='contact'),
]
