from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post, Comment
from .forms import PostForm, EditForm , CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request):
#	return render(request,'home.html',{})


class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']
	paginate_by = 5

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class =  PostForm
	template_name = 'add_post.html'


class UpdatePostView(UpdateView):
	model = Post
	form_class =  EditForm
	template_name = 'update_post.html'


class AddCommentView(CreateView):
	model = Comment
	form_class =  CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'
	success_url = reverse_lazy('home')
	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

def SearchPost(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		results = Post.objects.filter(title__contains=searched)
		return render(request, 'search_post.html',{'searched':searched,'results':results})
	else:
		return render(request, 'search_post.html',{})
		



#def LikeView(request, pk):
#	post = get_object_or_404(Post,id=request.POST.get('post_id'))
#	post.likes.add(request.user)
#	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

