# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.fields.datetime import TimeField
from wtforms.validators import DataRequired, Email, Optional

class BriefForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    phone = StringField("Контактний телефон", validators=[Optional()])
    contact_time = TimeField("Зручний час для звʼязку", validators=[Optional()])
    email = StringField("Електронна пошта", validators=[Email(), DataRequired()])

    product_name = StringField("Назва продукту або компанії", validators=[Optional()])
    project_description = TextAreaField("Опис проєкту", validators=[Optional()])
    target_audience = TextAreaField("Хто ваші клієнти?", validators=[Optional()])

    product_goal = SelectField('Основна мета', choices=[
        ('Продаж', 'Продаж'),
        ('Службовий сайт', 'Службовий сайт'),
        ('Інформування', 'Інформування'),
        ('Реклама', 'Реклама')
    ], validators=[Optional()])
    existing_website = SelectField("Чи є сайт?", choices=[("yes", "Так"), ("no", "Ні")])
    required_features = TextAreaField("Необхідні функції", validators=[DataRequired()])

    competitors = TextAreaField("Конкуренти", validators=[Optional()])
    budget = StringField("Бюджет", validators=[Optional()])
    promotion_channels = StringField("Канали просування", validators=[Optional()])

    content_manager = StringField("Контент-менеджер", validators=[Optional()])
    additional_comments = TextAreaField("Додаткові коментарі", validators=[Optional()])
    favorite_examples = TextAreaField("Приклади сайтів", validators=[Optional()])

    submit = SubmitField("Надіслати")

class EditBriefForm(FlaskForm):
    name = StringField("Ім'я", validators=[DataRequired()])
    phone = StringField("Контактний телефон", validators=[Optional()])
    contact_time = TimeField("Зручний час для звʼязку", validators=[Optional()])
    email = StringField("Електронна пошта", validators=[Email(), DataRequired()])

    product_name = StringField("Назва продукту або компанії", validators=[Optional()])
    project_description = TextAreaField("Опис проєкту", validators=[Optional()])
    target_audience = TextAreaField("Хто ваші клієнти?", validators=[Optional()])

    product_goal = SelectField('Основна мета', choices=[
        ('Продаж', 'Продаж'),
        ('Службовий сайт', 'Службовий сайт'),
        ('Інформування', 'Інформування'),
        ('Реклама', 'Реклама')
    ], validators=[Optional()])

    existing_website = SelectField("Чи є сайт?", choices=[("yes", "Так"), ("no", "Ні")])
    required_features = TextAreaField("Необхідні функції", validators=[DataRequired()])

    competitors = TextAreaField("Конкуренти", validators=[Optional()])
    budget = StringField("Бюджет", validators=[Optional()])
    promotion_channels = StringField("Канали просування", validators=[Optional()])

    content_manager = StringField("Контент-менеджер", validators=[Optional()])
    additional_comments = TextAreaField("Додаткові коментарі", validators=[Optional()])
    favorite_examples = TextAreaField("Приклади сайтів", validators=[Optional()])

    submit = SubmitField("Зберегти")

