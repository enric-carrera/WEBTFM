from django import forms

typeChoices = (("img/company1.png","type 1"),("img/company21.png","type 2"),) 

class AddClientForm(forms.Form):

    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"insert the name of the company"}))

    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Description of the contract with the client"}))

    expiration_date = forms.DateField(widget=forms.SelectDateWidget, label="Insert the expiration date fo the contract")

    budget = forms.IntegerField(label="Insert the budget of the projects in the contract")

    image = forms.ChoiceField(choices=typeChoices)


# forms.FilePathField(path="client_list/static/img")


