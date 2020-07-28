from wtforms import StringField,BooleanField,IntegerField,DateField,SubmitField,ValidationError
from flask_wtf import FlaskForm,Form
from wtforms.validators import Email,DataRequired,InputRequired,Length,Required,NumberRange

def my_custom_deal_name_validator(form,field):
    if field.data == 'Test1':
        raise ValidationError('Test1 dea is taken')

class DealForm(Form):
    DealName=StringField(label='Deal Name',validators=[my_custom_deal_name_validator,Length(min=5,max=8,message="Enter valid deal name")])
    DealDate=DateField(label='Deal Date',format='%m/%d/%Y',validators=[DataRequired(message="Please enter deal date")])
    DealQuantity=IntegerField(label='Deal Quantity',validators=[NumberRange(min=100,max=1000,message="Enter valid deal quantity")])
    DealDescription=StringField(label='Deal Description')
    IsLocal=BooleanField(label='Is local')
    Submit=SubmitField('Submit')
