from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import os

from .models import Documentation
from .forms import DocUploadForm
from .htmlify import HTMLifier

DOC_DIR = os.path.abspath(os.path.dirname(__name__))+"/docupload/docs/"

def index(request):
    doc_list = Documentation.objects.all()
    template = loader.get_template('docupload/index.html')
    form = DocUploadForm()

    context = {
        'doc_list': doc_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    html = HTMLifier(doc_base_path=DOC_DIR)

    if request.method == 'POST':
        form = DocUploadForm(request.POST, request.FILES)
        if form.is_valid():
            html.convert(request.FILES['doc_file'])
    return HttpResponseRedirect('/doc/')
