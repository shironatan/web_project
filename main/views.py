from django.shortcuts import redirect,render
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.views import View
from .models import Contents,Reviews
from django.db import connection


#home
class Home(View):
    #一覧表示処理
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            #SQLの実行
            with connection.cursor() as cursor:
                cursor.execute("select CL.contents_name,CL.picture,CL.contents_detail,RV.review from \"Contents\" as CL left outer join \"Reviews\" as RV on CL.id = RV.contents_id and user_name_id = %s;",[request.user.id])
                reviews = cursor.fetchall()

                review_list = []
                for review in reviews:
                    inraw = []
                    #contents_name
                    inraw.append(review[0])
                    #picture
                    inraw.append(review[1])
                    #detail
                    inraw.append(review[2])
                    #review
                    inraw.append(review[3])
                    review_list.append(inraw)

            params = {
                'review_list' : review_list
            }
            return render(request, 'recommend/home.html',params)
        else:
            return redirect('/')



