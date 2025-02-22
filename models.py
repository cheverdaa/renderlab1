# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Brief(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)  # Name and surname
    phone = db.Column(db.String(50), nullable=True)  # Phone number
    contact_time = db.Column(db.String(10), nullable=True)  # Preferred contact time (HH:MM format)
    email = db.Column(db.String(120), nullable=True)  # Email

    product_name = db.Column(db.String(200), nullable=True)  # Product/Company name
    project_description = db.Column(db.Text, nullable=True)  # Short project description
    target_audience = db.Column(db.Text, nullable=True)  # Target audience

    product_goal = db.Column(db.String(100), nullable=True)  # Product/website goal (sales, branding, etc.)
    existing_website = db.Column(db.String(20), nullable=True)  # If they have an existing website (yes/no)
    required_features = db.Column(db.Text, nullable=True)  # Features for the new product/website

    competitors = db.Column(db.Text, nullable=True)  # Competitors
    budget = db.Column(db.String(100), nullable=True)  # Estimated budget
    promotion_channels = db.Column(db.String(200), nullable=True)  # Promotion channels (social media, SEO, etc.)
    content_manager = db.Column(db.String(100), nullable=True)  # Who will manage the content

    additional_comments = db.Column(db.Text, nullable=True)  # Additional comments or wishes
    favorite_examples = db.Column(db.Text, nullable=True)  # Favorite site/product examples
