from django.template import RequestContext
from django.shortcuts import render
from comments.models import Conversation, Comment
from comments.forms import CommentForm, ConversationForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime

# this comment is also new
def index(request):
#    request.session.set_test_cookie()
    conversations_list = Conversation.objects.order_by('-likes')
    context_dict = {'conversations' : conversations_list}
    #comments_list = Comment.objects.order_by('-likes')
    #context_dict = {'comments' : comments_list}
    
    
    visits = request.session.get('visits')
    
    if not visits:
        visits = 1
    
    reset_last_visit_time = False
    
    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).days > 0:
            visits = visits + 1
            reset_last_visit_time = True

    else:
        reset_last_visit_time = True
    
    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    
    context_dict['visits'] = visits

    return render(request, 'comments/index.html', context_dict)

def conversation(request, conversation_name_slug):
    context_dict = {}
    try:
        conversation = Conversation.objects.get(slug=conversation_name_slug)
        context_dict['conversation_name'] = conversation.name
        context_dict['conversation_name_slug'] = conversation_name_slug
        comments = Comment.objects.filter(conversation=conversation)
        context_dict['comments'] = comments
        context_dict['conversation'] = conversation
        
    except Conversation.DoesNotExist:
        pass

    return render(request, 'comments/conversation.html', context_dict)

def dummy(request):
      return render(request, 'comments/dummy.html', {})

@login_required
def add_conversation(request):

    if request.method == 'POST':
        conv_form = ConversationForm(data=request.POST)
        if conv_form.is_valid():

            conversation = conv_form.save(commit=False)
            conversation.creator = User.objects.get(username=request.user.username)
            conversation.save()
            return HttpResponseRedirect('/comments/')
        else:
            print conv_form.errors
    else:
        conv_form = ConversationForm()

    return render(request, 'comments/add_conversation.html', {'form' : conv_form})

@login_required
def add_comment(request, conversation_name_slug):
    
    try:
        conv = Conversation.objects.get(slug=conversation_name_slug)
    except Conversation.DoesNotExist:
        conv = None

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if conv:
                comment = form.save(commit=False)
                comment.user = User.objects.get(username=request.user.username)
                comment.conversation = conv
                comment.likes = 0
                comment.save()
                return HttpResponseRedirect(('/comments/' + conversation_name_slug + '/'))
        else:
            print form.errors
    else:
        form = CommentForm()

    #return dummy(request, conversation_name_slug)
    
    return render(request, 'comments/add_comment.html', {'form' : form, 'conversation_name_slug' : conversation_name_slug})


@login_required
def restricted(request):
    return HttpResponse("Yea, you can see this cuz u logged in, dog.")
