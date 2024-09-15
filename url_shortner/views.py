import random
import string

from django.shortcuts import redirect, render
from url_shortner.forms import UrlForm
from app.models import UrlModel


def UrlShort(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)

        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url = form.cleaned_data['url']
            new_url = UrlModel(url=url, slug=slug)
            new_url.save()

            request.user.UrlShort.add(new_url)
            return redirect('/')
    else:
        form = UrlForm()

    data = UrlModel.objects.all()
    context = {
        'form': form,
        'data': data
    }

    return render(request, 'index.html', context)


def urlRedirect(request, slugs):
    data = UrlModel.objects.get(slug=slugs)
    return redirect(data.url)
