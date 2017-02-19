from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def purchases_for_month(request):
    id = int(request.GET.get('id'))
    type = request.GET.get('type', 'default')
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
