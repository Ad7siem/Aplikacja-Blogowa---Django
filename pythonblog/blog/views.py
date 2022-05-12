from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# class view
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(status = 2)
    
class PostDetailView(DetailView):
    model = Post
    slug_field = "slug"
    slug_url_kwarg = "get_slug"
    template_name = "blog/post_detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect(reverse("blog:post_detail", kwargs={"get_slug": form.instance.slug}))

class PostUpdateView(UpdateView):
    model = Post
    slug_field = "slug"
    slug_url_kwarg = "get_slug"
    template_name = "blog/post_create.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect(reverse("blog:post_detail", kwargs={"get_slug": form.instance.slug}))

class PostDeleteView(DeleteView):
    template_name = "blog/post_delete.html"

    def get_success_url(self):
        return reverse("blog:post_list")

    def get_object(self):
        slug = self.kwargs.get("get_slug")
        return get_object_or_404(Post, slug=slug)

# Create your views here.
# def post_list(request):
#     posts = Post.objects.filter(status = 2)
#     paginator = Paginator(posts, 20)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     context = {
#         # "object_list": posts,
#         "object_list": page_obj,
#     }
#     return render(request, "blog/post_list.html", context)

# def post_detail(request, get_slug):
#     post = get_object_or_404(Post, slug = get_slug)
#     context={
#         "object": post
#     }
#     return render(request, "blog/post_detail.html", context)

# def post_create(request):
#     title = "Create"
#     form = PostForm(request.POST or None, request.FILES or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.created_by = request.user
#             form.save()
#             return redirect(reverse("blog:post_detail", kwargs={
#                 "get_slug": form.instance.slug
#             }))

#     context = {
#         "title": title,
#         "form": form,
#     }
#     return render(request, "blog/post_create.html", context)

# def post_update(request, get_slug):
#     title = "Create"
#     post = Post.objects.get(slug = get_slug)

#     form = PostForm(
#         request.POST or None, 
#         request.FILES or None, 
#         instance=post)

#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.created_by = request.user
#             form.save()
#             return redirect(reverse("blog:post_detail", kwargs={
#                 "get_slug": form.instance.slug
#             }))

#     context = {
#         "title": title,
#         "form": form,
#     }
#     return render(request, "blog/post_create.html", context)

# def post_delete(request, get_slug):
#     post = get_object_or_404(Post, slug = get_slug)
#     post.delete()
#     return redirect(reverse("blog:post_list"))