from django.template import loader
from django.http import HttpResponse


def lawyers(request):
    #return HttpResponse("welcome!")
    template = loader.get_template('lawyershome.html')
    return HttpResponse(template.render())

