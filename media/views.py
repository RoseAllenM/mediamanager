from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView

from .forms import ManifestForm
from .models import Manifest, Media


class MediaDetailView(DetailView):
    model = Media


class MediaListView(ListView):
    model = Media


def manifest_list(request):
    # Handle file upload.
    if request.method == 'POST':
        form = ManifestForm(request.POST, request.FILES)
        if form.is_valid():
            manifest_file = Manifest(
                manifest_file=request.FILES['manifest_file'],
            )
            manifest_file.save()

            # Redirect to the manifest list after POST.
            return HttpResponseRedirect(
                reverse('mediamanager.media.views.manifest_list'),
            )
    else:
        form = ManifestForm()  # A empty, unbound form.

    # Load manifest_files for the list page.
    manifest_files = Manifest.objects.all()

    # Render list page with the manifest_files and the form.
    return render_to_response(
        'media/manifest_list.html',
        {'manifest_files': manifest_files, 'form': form},
        context_instance=RequestContext(request),
    )
