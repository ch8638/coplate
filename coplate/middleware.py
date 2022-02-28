from django.urls import reverse
from django.shortcuts import redirect


class ProfileSetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    # request 프로세싱
    def __call__(self, request):
        if (
            request.user.is_authenticated and  # 유저 로그인 상태 확인
            not request.user.nickname and  # 프로필 설정 확인
            request.path_info != reverse("profile-set")  # 어디로 request 보냈는지 확인
        ):
            return redirect("profile-set")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
