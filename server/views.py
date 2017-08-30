# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import datetime, time

# Create your views here.

def index(request):
    return render(request, 'server/login.html')

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('viewchats')
    else:
        return render(request, 'server/login.html', {"message": 'Wrong Credentials! Try Again.'})

def viewchats(request):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('/home/lionel/Downloads/ctsapp-41576-firebase-adminsdk-l4x9l-ef1b9bbf18.json')

    firebase_admin.initialize_app(cred, {'databaseURL': 'https://ctsapp-41576.firebaseio.com/'})

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    ref = db.reference('chats')
    snapshot = ref.order_by_key().get()
    for key, value in snapshot.items():
        print('chat by {0}'.format(key, value))
    context = {"chats": snapshot.items()}
    firebase_admin.delete_app(firebase_admin.get_app())
    return render(request, 'server/chats.html', context)

def viewchat(request, user):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('/home/lionel/Downloads/ctsapp-41576-firebase-adminsdk-l4x9l-ef1b9bbf18.json')

    firebase_admin.initialize_app(cred, {'databaseURL': 'https://ctsapp-41576.firebaseio.com/'})
    ref = db.reference(user)
    snapshot = ref.order_by_key().get()
    context = {"messages": snapshot.items(), "user": user}
    firebase_admin.delete_app(firebase_admin.get_app())
    return render(request, 'server/chat.html', context)

def sendmessage(request, user):
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    # Fetch the service account key JSON file contentMultiValueDictKeyErrors
    cred = credentials.Certificate('/home/lionel/Downloads/ctsapp-41576-firebase-adminsdk-l4x9l-ef1b9bbf18.json')

    firebase_admin.initialize_app(cred, {'databaseURL': 'https://ctsapp-41576.firebaseio.com/'})
    ref = db.reference(user)
    message = request.POST.get('textmessage','')
    # We can also chain the two calls together
    ref.push({'messageText': message, 'messageUser': 'admin', 'messageTime': 0})
    firebase_admin.delete_app(firebase_admin.get_app())
    return HttpResponseRedirect('/server/viewchat/'+user)
