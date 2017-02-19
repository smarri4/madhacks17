from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.http import HttpResponse
import logging
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

apikey = '4068fb9868181126f8b7bd67a0dd9306'
logger = logging.getLogger(__name__)

class NameForm(forms.Form):
    dining = forms.CharField(label='Dining:', max_length=100)
    clothing = forms.CharField(label='Clothing:', max_length=100)
    gas = forms.CharField(label='Gas:', max_length=100)
    others = forms.CharField(label='Others:', max_length=100)
    total = forms.CharField(label='Total:', max_length=100)

def plan_form(request):
    t = get_template('visualize/pages/forms.html')
    html = t.render()
    return HttpResponse(html)

@csrf_exempt
def plan_your_budget(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return HttpResponseRedirect('/index')

    # if a GET (or any other method) we'll create a blank form
    else:
        t = get_template('visualize/pages/forms.html')
        html = t.render()
        return HttpResponse(html)
