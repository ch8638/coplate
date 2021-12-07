from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView


# Create your views here.
def index(request):
    return render(request, "coplate/index.html")


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):  # 폼이 성공적으로 처리되면 어디로 리디렉션할 것인지 처리해주는 함수
        return reverse("index")
