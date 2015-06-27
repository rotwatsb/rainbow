import os, datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comments_project.settings')

import django
django.setup()

from comments.models import Comment, Conversation
from django.contrib.auth.models import User


def pop():
    duckman = addUser("DuckMan")
    bufbill = addUser("BuffaloBill")
    steve = addUser("Steve")

    robot = addcon("Favorite Robot", 0, duckman)
    
    princess = addcon("How can we rescue the princess?", 1, bufbill)

    dragon = addcon("How hot is dragon breath?", 2, steve)
    
    #addcom("DragonBreath", "My beard is on fire.")

def addUser(n):
    u = User.objects.create_user(n, "", n)
    u.save()
    return u

def addcon(n, l, c):
    con = Conversation.objects.get_or_create(conversation=n, time_created=datetime.datetime.now(), likes=l, creator=c)[0]
    con.save()
    return con


#def addcom(u, t):
#    c = Comment.objects.get_or_create(user=u,text=t,likes=0)[0]
#    return c

if __name__=='__main__':
    print "Starting Comments population script..."
    pop()
