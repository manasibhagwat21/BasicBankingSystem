from django.contrib import auth, messages
from django.db import models
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os

from .forms import TransferFunds
from .models import Transfer, TransferHistory


def index(request):
    return render(request, 'index.html')


def transfer(request):
    usersL = Transfer.objects.all()
    his = TransferHistory.objects.all()
    if request.method == 'POST':
        sender = request.POST.get('sender')
        name = request.POST.get('name')
        funds = request.POST.get('funds')

        history = TransferHistory(sender=sender, receiver=name, funds=funds)
        history.save()

        sender = Transfer.objects.get(name=sender)
        sender.funds -= int(funds)
        sender.save()
        user = Transfer.objects.get(name=name)
        user.funds += int(funds)
        user.save()

        redirect('index.html')
    p = dict(user=usersL, his=his)
    return render(request, 'transfer.html', p)


def userList(request):
    users = Transfer.objects.all()
    return render(request, 'userList.html', {"user": users})
