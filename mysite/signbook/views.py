from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
# Create your views here.

def index(request):
	comments=Comment.objects.order_by('-date')
	context = {'comment':comments}
	return render(request, 'sign/index.html', context)

def sign(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
			new_comment.save()
			return redirect('index')
	else:
	    form = CommentForm()

	context = {'form':form}
	return render(request, 'sign/sign.html', context)
