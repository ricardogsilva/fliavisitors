from django import forms

class VoteForm(forms.Form):
    minVisitor = 1
    maxVisitor = 50
    VISITOR_CHOICES = zip(range(minVisitor, maxVisitor+1), 
                          range(minVisitor, maxVisitor+1))
    #freguesia = forms.integerField()
    #visitors = forms.integerField(initial=1, max_value=50, min_value=1)
    visitors = forms.ChoiceField(choices=VISITOR_CHOICES, initial=(1, 1))
