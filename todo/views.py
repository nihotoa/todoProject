from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class Todolist(ListView):  # 全てのデータをもってくる
    template_name = 'list.html'
    model = TodoModel  # 使用するデータベースの選択


class TodoDetail(DetailView):  # データを一つずつ持ってくる
    template_name = 'detail.html'
    model = TodoModel


class TodoCreate(CreateView):
    template_name = 'create.html'  # 参照するhtmlファイルの名前　
    model = TodoModel
    fields = ('Title', 'Memo', 'priority', 'duedate')  # 送信用フォームに使用するitemをすべて入れる
    success_url = reverse_lazy('list')


class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('Title', 'Memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')