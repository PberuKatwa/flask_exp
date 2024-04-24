from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, BooleanField, SelectField,IntegerField
from wtforms.validators import DataRequired, Length, Email


class AppointmentForm(FlaskForm):
    client_name = StringField('Client Name123',
                              validators=[DataRequired(), Length(max=15, min=4)])
    email = EmailField('Email',
                       validators=[DataRequired(), Length(max=25)])
    phone = IntegerField('Phone', validators=[DataRequired(), Length(max=15)])

    legal_service = SelectField('Which legal service do you want', choices=[('law 1', 'law 1'),
                                                                            ('law 2', 'law 2')])
    case_filed = BooleanField('Is the case filed')
    case_filed_number = StringField('Case file number')
    additional_information = TextAreaField('Additional Information',
                                           validators=[Length(max=70)])

    submit_appointment = SubmitField('SUBMIT')
