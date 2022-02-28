from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation


def confirmation_required_redirect(self, request):
    send_email_confirmation(request, request.user)  # 유저에게 인증 이메일을 보낸다.
    return redirect("account_email_confirmation_required")  # 이메일 인증이 필요하다는 페이지로 redirect 해주는 메소드
