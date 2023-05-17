from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# done using generic listviews
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'


# done by hand
# def post_list(request):
#    post = Post.objects.all()
#    paginator = Paginator(post, 5)
#    page_number = request.GET.get('page', 1)
#    try:
#        posts = paginator.page(page_number)
#    except PageNotAnInteger:
#        posts = paginator.page(1)
#    except EmptyPage:
#        posts = paginator.page(paginator.num_pages)
#    print(f"[INFO] {len(post)} registros! You are at page: {page_number}")
#    return render(request, "blog/post/list.html", {'posts': posts})


def post_detail(request, year, month, day, post):
    print(f'[***INFO***] , Slug: {post}, Year: {year}, Month: {month}, Day;{day}')
    post = get_object_or_404(Post, slug=post, publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})


def get_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments()
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, "blog/post/comment.html", {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

