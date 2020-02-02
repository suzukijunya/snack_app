from django import forms
from.models import Friend, Message, Store

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'mail', 'phone_number', 'address', 'access', 'business_hours', 'store_type']

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

class CheckForm(forms.Form):
    str = forms.CharField(label='String')
    
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('You input "NO"!')

class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']