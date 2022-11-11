from django.http import Http404, HttpResponseNotAllowed, FileResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib import messages

from .forms import UploadPdfFileForm
from .utils import (
    get_files_by_session_id, save_file_by_session_id, get_file_by_session_id
)


def get_or_create_session_key(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    return request.session.session_key


def index(request):
    return render(request, 'adaptive/index.html')


def user_data(request, key):
    if request.method != 'POST':
        raise HttpResponseNotAllowed(('POST',))

    if key not in settings.USER_DATA_KEYS:
        raise Http404

    value = request.POST.get(key, settings.USER_DATA_KEYS[key]['default'])
    next_path = request.POST.get('next', 'index')

    response = redirect(next_path)
    response.set_cookie(key, value)

    return response


def pdf_files(request):
    session_key = get_or_create_session_key(request)

    if request.method == 'POST':
        form = UploadPdfFileForm(request.POST, request.FILES)

        if form.is_valid():
            save_file_by_session_id(session_key, form.cleaned_data['file'])
            messages.success(request, 'Файл успешно сохранен')
            
            return redirect('pdf_files')
    else:
        form = UploadPdfFileForm()

    context = {
        'form': form,
        'files': get_files_by_session_id(session_key),
    }

    return render(request, 'adaptive/pdf_files.html', context=context)


def download_pdf_file(request, filename):
    session_key = get_or_create_session_key(request)
    path = get_file_by_session_id(session_key, filename)

    if path is None:
        raise Http404

    return FileResponse(open(path, 'rb'))
