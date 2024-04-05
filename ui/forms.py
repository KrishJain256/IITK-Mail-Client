from django import forms


class loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))

class signupform(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))
    rollno = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Roll No.', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;', 'class': 'form-control'}))

class composeform(forms.Form):
    to = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'To',
                                                              'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;',
                                                              'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject',
                                                              'style': 'width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;',
                                                              'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'style': 'background-color:white; color: black; height: 300px; width: 100%; padding: 10px; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; transition: border-color 0.3s;'}))


