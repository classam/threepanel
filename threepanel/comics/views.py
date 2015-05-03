import logging

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from dashboard.views import render

from .models import Comic, Blog
from .forms import ComicForm, BlogForm


logger = logging.getLogger(__name__)


def home(request):
    hero = Comic.hero()
    return render(request, "comics/home.html", {'hero': hero})


def single_by_numerical_order(request, n):
    """ redirect to single by slug """
    comic = get_object_or_404(Comic, order=n)
    return HttpResponseRedirect(reverse("comics.views.single",
                                kwargs={'slug': comic.slug}))


def single(request, comic_slug):
    comic = get_object_or_404(Comic, slug=comic_slug)
    return render(request, "comics/single.html", {'slug': comic_slug,
                                                  'comic': comic})


@login_required
def manage(request):
    backlog = Comic.backlog()
    archives = Comic.archives()
    hero = Comic.hero()
    return render(request, "comics/manage.html", {
        'backlog': backlog,
        'archives': archives,
        'hero': hero})


@login_required
def trash(request):
    # trash = Comic.trash()
    pass


@login_required
def create(request):
    if request.method == 'POST':
        form = ComicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Comic Created!')
            return HttpResponseRedirect(reverse("comics.views.manage"))
    else:
        form = ComicForm()

    return render(request, 'comics/create.html', {'form': form})


@login_required
def update(request, comic_slug):
    comic = get_object_or_404(Comic, slug=comic_slug)
    print("Updating comic!")
    if request.method == 'POST':
        form = ComicForm(request.POST, instance=comic)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Comic Updated!')
            return HttpResponseRedirect(reverse("comics.views.manage"))
    else:
        form = ComicForm(instance=comic)

    return render(request, 'comics/update.html', {'form': form, 'slug': comic_slug})


@login_required
def delete(request, comic_slug):
    comic = get_object_or_404(Comic, slug=comic_slug)
    comic.hide()
    logger.info("{} deleted".format(comic))
    messages.add_message(request, messages.INFO,
                         "\"{}\" Deleted".format(comic.title))
    return HttpResponseRedirect(reverse('comics.views.manage'))


@login_required
def create_blog(request, comic_slug):
    comic = get_object_or_404(Comic, slug=comic_slug)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Blog Created!')
            return HttpResponseRedirect(reverse("comics.views.manage"))
    else:
        form = BlogForm(initial={'comic':comic})

    return render(request, 'comics/create_blog.html', {'form': form, 'comic_slug': comic_slug})


@login_required
def update_blog(request, comic_slug, slug):
    blog = get_object_or_404(Blog, comic__slug=comic_slug, slug=slug)
    print("Blog {} Updated".format(blog))
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        print("BUTTS")
        print(form)
        print("----")
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Blog Updated!')
            return HttpResponseRedirect(reverse("comics.views.manage"))
    else:
        form = BlogForm(instance=blog)

    return render(request, 'comics/update_blog.html', {'form': form, 'comic_slug': comic_slug, 'slug': slug})


@login_required
def delete_blog(request, comic_slug, slug):
    blog = get_object_or_404(Blog, comic__slug=comic_slug, slug=slug)
    blog.hide()
    logger.info("{} deleted".format(blog))
    messages.add_message(request, messages.INFO,
                         "\"{}\" Deleted".format(blog.title))
    return HttpResponseRedirect(reverse('comics.views.manage'))
