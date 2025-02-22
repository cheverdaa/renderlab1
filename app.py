from flask import Flask, render_template, redirect, url_for, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from config import Config
from models import db, Brief
from forms import BriefForm, EditBriefForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config.from_object(Config)
app.config['SQLALCHEMY_ECHO'] = True

csrf = CSRFProtect(app)

db.init_app(app)  # Initialize db after app is created
migrate = Migrate(app, db)  # Apply migrations

# Ensure database tables are created
with app.app_context():
    db.create_all()

# Route for brief form
@app.route("/", methods=["GET", "POST"])
def brief():
    form = BriefForm()
    if form.validate_on_submit():
        new_brief = Brief(
            name=form.name.data,
            phone=form.phone.data,
            contact_time = form.contact_time.data if form.contact_time.data else None,
            email=form.email.data,
            product_name=form.product_name.data,
            project_description=form.project_description.data,
            target_audience=form.target_audience.data,
            product_goal=form.product_goal.data,
            existing_website=form.existing_website.data,
            required_features=form.required_features.data,
            competitors=form.competitors.data,
            budget=form.budget.data,
            promotion_channels=form.promotion_channels.data,
            content_manager=form.content_manager.data,
            additional_comments=form.additional_comments.data,
            favorite_examples=form.favorite_examples.data
        )
        db.session.add(new_brief)
        print(form.errors)  # це виведе помилки валідації форми
        try:
            db.session.commit()
            print("Data saved successfully!")
        except Exception as e:
            print(form.errors)
            db.session.rollback()
            print(f"Error saving data: {e}")
        return redirect(url_for("thank_you"))
    return render_template("brief_form.html", form=form)

# Route for displaying submitted briefs
@app.route("/thank-you", methods=["GET", "POST"])
def thank_you():
    briefs = Brief.query.all()
    return render_template("thank_you.html", briefs=briefs)

# Admin page to view all submitted briefs
@app.route("/admin-panel", methods=['GET', 'POST'])
def admin_page():
    form = EditBriefForm()
    briefs = Brief.query.all()
    return render_template("admin.html", briefs=briefs, form=form)

from flask import request, jsonify
from models import db, Brief

@app.route('/edit/<int:brief_id>', methods=['POST'])
def edit_brief(brief_id):
    print("Отримано дані:", json.dumps(request.form.to_dict(), indent=2, ensure_ascii=False))
    brief = Brief.query.get_or_404(brief_id)

    try:
        # Отримуємо дані з форми
        brief.name = request.form.get('name', brief.name)
        brief.phone = request.form.get('phone', brief.phone)
        brief.contact_time = request.form.get('contact_time', brief.contact_time)
        brief.email = request.form.get('email', brief.email)
        brief.product_name = request.form.get('product_name', brief.product_name)
        brief.project_description = request.form.get('project_description', brief.project_description)
        brief.target_audience = request.form.get('target_audience', brief.target_audience)
        brief.product_goal = request.form.get('product_goal', brief.product_goal)
        brief.competitors = request.form.get('competitors', brief.competitors)
        brief.budget = request.form.get('budget', brief.budget)
        brief.promotion_channels = request.form.get('promotion_channels', brief.promotion_channels)
        brief.content_manager = request.form.get('content_manager', brief.content_manager)
        brief.additional_comments = request.form.get('additional_comments', brief.additional_comments)
        brief.favorite_examples = request.form.get('favorite_examples', brief.favorite_examples)

        db.session.commit()  # Обов’язково комітимо зміни!

        return jsonify({"success": True, "updated": {
            "name": brief.name,
            "phone": brief.phone,
            "contact_time": brief.contact_time,
            "email": brief.email,
            "product_name": brief.product_name,
            "project_description": brief.project_description,
            "target_audience": brief.target_audience,
            "product_goal": brief.product_goal,
            "competitors": brief.competitors,
            "budget": brief.budget,
            "promotion_channels": brief.promotion_channels,
            "content_manager": brief.content_manager,
            "additional_comments": brief.additional_comments,
            "favorite_examples": brief.favorite_examples
        }})
    except Exception as e:
        db.session.rollback()  # Відкат, якщо щось пішло не так
        return jsonify({"success": False, "error": str(e)})



@app.route('/delete/<int:brief_id>')
def delete_brief(brief_id):
    brief = Brief.query.get_or_404(brief_id)
    db.session.delete(brief)
    db.session.commit()
    return redirect(url_for('admin_page'))


@app.route('/get-brief/<int:id>')
def get_brief(id):
    brief = Brief.query.get(id)
    if brief:
        return jsonify({
            'id': brief.id,
            'name': brief.name,
            'phone': brief.phone,
            'contact_time': brief.contact_time,
            'email': brief.email,
            'product_name': brief.product_name,
            'project_description': brief.project_description,
            'target_audience': brief.target_audience,
            'product_goal': brief.product_goal,
            'competitors': brief.competitors,
            'budget': brief.budget,
            'promotion_channels': brief.promotion_channels,
            'content_manager': brief.content_manager,
            'additional_comments': brief.additional_comments,
            'favorite_examples': brief.favorite_examples
        })
    return jsonify({'error': 'Brief not found'}), 404




if __name__ == "__main__":
    app.run(debug=False)
