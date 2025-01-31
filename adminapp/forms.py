from userapp.models import Attorneys,case_categories,Types_Law,case_studies,Blog
from adminapp.models import lawyer
from clientapp.models import clients
from django import forms


class Attorneys_edit_Form(forms.ModelForm):
    class Meta:
        model = Attorneys
        fields = ['name', 'profession', 'image']

class case_categories_edit_Form(forms.ModelForm):
    class Meta:
        model = case_categories
        fields = ['case_categories']
        
class types_edit_Form(forms.ModelForm):
    class Meta:
        model = Types_Law
        fields = ['law_tittle','point','detail','image']
        
class case_studies_Form(forms.ModelForm):
    class Meta:
        model = case_studies
        fields = ['case_studies_tittle','category','detail','case_studies_date','case_studies_image']
        
class blog_edit_Form(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['tittle','image','des']
        
class add_lawyer(forms.ModelForm):
    class Meta:
        model = lawyer
        fields = ['name','email','password']

class add_clients_forms(forms.ModelForm):
    class Meta:
        model = clients
        fields = ['name','email','password','lid']
        

class update_lawyer_profile(forms.ModelForm):
    class Meta:
        model = lawyer
        fields = ['name','age']