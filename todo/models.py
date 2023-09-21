from django.db import models


# Create your models here.

CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary','low'))
# データベースの設計図の作成


class TodoModel(models.Model):
    Title = models.CharField(max_length=100)
    Memo = models.TextField()
    priority = models.CharField(max_length=50, choices=CHOICE)
    duedate = models.DateField()

    def __str__(self): # 特殊メソッドを使ってタイトルを変更
        return self.Title