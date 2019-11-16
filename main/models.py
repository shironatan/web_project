from django.db import models
from django.contrib.auth.models import User

class ContentsList(models.Model):
    class Meta:
        #テーブル名を定義
        db_table = 'ContentsList'
    #テーブルのカラムに対応するフィールドを定義
    contents_name = models.CharField(verbose_name='作品名',max_length=255,null=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.contents_name


class Reviews(models.Model):
    class Meta:
        #テーブル名
        db_table = 'Reviews'
    user_name = models.ForeignKey(User,verbose_name='ユーザー名',on_delete=models.CASCADE,null=False)
    contents = models.ForeignKey(ContentsList,verbose_name='作品名',on_delete=models.CASCADE,null=False)
    review = models.IntegerField(verbose_name='評価',default=0,)