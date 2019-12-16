from django.shortcuts import render
from django.http import HttpResponse


from .models import Tag, Post


def post_list(request, category_id=None, tag_id=None):
    # content = 'post_line category_id={category_id}, tag_id={tag_id}'.format(
    #     category_id=category_id,
    #     tag_id=tag_id,
    # )
    #
    # return HttpResponse(content)

    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoseNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(category_id=category_id)

    return render(request, 'blog/list.html', context={'post_list': post_list})


def post_detail(request, post_id):
    # return HttpResponse('detail')
    return render(request, 'blog/detail.html', context={'name': 'post_detail'})
