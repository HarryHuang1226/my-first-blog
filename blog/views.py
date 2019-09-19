from django.shortcuts import render

# that will render (put together) our template blog/post_list.html.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
# Create your views here.
