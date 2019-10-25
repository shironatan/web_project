from django.shortcuts import render,redirect
from allauth.account import views as allauthviews
from django.views.generic import CreateView,TemplateView


class Home_view(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(Home_view,self).get_context_data(**kwargs)
        return context
home_view = Home_view.as_view()


class SigninView(allauthviews.LoginView):
    template_name = 'signin/index.html'
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            #ログイン済みだった場合　トップ画面にリダイレクト
            return redirect('/accounts')
        else:
            #ログインされていない場合
            response = super(SigninView, self).dispatch(request, *args, **kwargs)
            return response

    def form_valid(self,form):
        #ログインチェック
        context = form.login(self.request,redirect_url='/accounts')
        context['text'] = 'ログイン完了'
        return context

    def get_context_data(self, **kwargs):
        context = super(SigninView, self).get_context_data(**kwargs)
        return context

signin_view = SigninView.as_view()

class SignupView(allauthviews.SignupView):
    template_name = 'signup/index.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # ログイン済みだった場合　トップ画面にリダイレクト
            return redirect('/accounts')
        else:
            #ログインされていない場合
            response = super(SignupView,self).dispatch(request, *args, **kwargs)
            return response

    def form_valid(self,form):
        #db登録
        self.user = form.save(self.request)
        return redirect('/accounts')

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context


signup_view = SignupView.as_view()

class SignoutView(allauthviews.LogoutView):
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return self.post(*args,**kwargs)
        else:
            return redirect('/accounts')

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/accounts')


signout_view = SignoutView.as_view()

