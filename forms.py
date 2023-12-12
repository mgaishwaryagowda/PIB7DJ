#class studentform(forms.Form):
#    student_ID = forms.IntegerField()
#   student_name=forms.CharField()
#   course=forms.CharField()
#   jdate=forms.DateField()

# creating a form using models
from django.forms import ModelForm
from Hello.models import students
class studentform(ModelForm):
    class Meta:
        model=students
        # fields='all'
        fields=['student_ID','student_name','course','jdate']
        labels={'student_ID':'ID','student_name':'Name','course':'Course','jdate':'Joining Date'}
#Creating a form to add an student.
form=studentform()
