from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog(request):
    post_blog = Blog.objects.all().order_by("-id")
    page_number = request.GET.get("page")
    p = Paginator(post_blog, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)
    context = {
        'post_blog':post_blog,
        'page_obj': page_obj
    }

    return render(request, 'blog.html', context)



