from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView


# Create your views here.
def index(request):
    return render(request, "coplate/index.html")


class CustomPasswordChangeView(PasswordChangeView):
<<<<<<< HEAD
    def get_success_url(self):  # 폼이 성공적으로 처리되면 어디로 리디렉션할 것인지 처리해주는 함수

class ReviewDetailView(DetailView):
    model = Review
    template_name = "coplate/review_detail.html"
    pk_url_kwarg = "review_id"


class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):  # Access Mixin은 먼저 실행되어야 해서 제네릭 뷰 왼쪽에 써야 한다.
    model = Review
    form_class = ReviewForm
    template_name = "coplate/review_form.html"

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def form_valid(self, form):  # 입력받은 데이터가 유효할 때 데이터로 채워진 모델 오브젝트를 만들고 오브젝트를 저장하는 메소드
        # view에서 현재 user에 접근할 때는 request.user를 사용
        # 저장될 폼에 새로운 속성을 추가하려면 form.instance에 속성을 추가하고 꼭 CreateView의 form_vaild 메소드를 호출해야 한다. 호출하지 않으면 폼이 저장되지 않는다.
        form.instance.author = self.request.user  # 함수형에서는 request가 view 파라미터로 전달. 클래스형 뷰에서는 self.request로 접근해야 한다.
        return super().form_valid(form)  # super는 ReviewCreateView의 상위 클래스, 즉 CreateView를 의미

    def get_success_url(self):
        # self.object는 현재 제네릭 뷰가 다루고 있는 object라고 생각하면 된다.
        return reverse("review-detail", kwargs={"review_id": self.object.id})  # review-detail에 id를 파라미터로 넘긴다.

    def test_func(self, user):  # user가 뷰에 접근할 수 있는지 여부를 boolean 값으로 return 한다.
        return EmailAddress.objects.filter(user=user, verified=True).exists()


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "coplate/review_form.html"
    pk_url_kwarg = "review_id"

    raise_exception = True
    redirect_unauthenticated_users = False  # default 값 False

    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id": self.object.id})

    def test_func(self, user):  # 리뷰의 작성자와 로그인된 유저가 같은지 확인
        review = self.get_object()
        return review.author == user


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "coplate/review_confirm_delete.html"
    pk_url_kwarg = "review_id"

    raise_exception = True

    def get_success_url(self):
        return reverse("index")

    def test_func(self, user):
        review = self.get_object()
        return review.author == user


class ProfileView(DetailView):  # DetailView : 유저 인스턴스 하나를 template으로 전달
    model = User
    template_name = "coplate/profile.html"
    pk_url_kwarg = "user_id"  # urls.py에서 <int:user_id>로 넘겨줬기 때문에 user_id로 받는다.
    context_object_name = "profile_user"

    # 유저의 리뷰를 보여줄 것이기 때문에 리뷰를 template으로 전달되는 context에 추가해야 한다.
    def get_context_data(self, **kwargs):  # 추가 데이터를 넣기 위해서 get_context_data를 오버라이드 한다.(context의 type은 dictionary)
        context = super().get_context_data(**kwargs)  # 기존의 context를 가져온다.
        user_id = self.kwargs.get("user_id")  # url로 전달되는 파라미터는 self.kwargs로 접근할 수 있다.
        context["user_reviews"] = Review.objects.filter(author__id=user_id).order_by("-dt_created")[:4]  # -dt_created : 생성일 내림차순
        return context


class UserReviewListView(ListView):  # ListView : model에 해당하는 모든 object(리뷰의 리스트)를 template으로 전달한다.
    model = Review
    template_name = "coplate/user_review_list.html"
    context_object_name = "user_reviews"  # user_reviews 이름으로 view에서 template로 넘겨준다.
    paginate_by = 4

    # get_queryset 메소드를 오버라이드할 때는 그냥 디스플레이 하고 싶은 오브젝트 리스트를 리턴해 주면 된다.
    # 기존의 queryset을 변형(기존의 queryset에 오브젝트 추가/삭제)하는 것이 아니라 아예 새로운 queryset을 리턴해 주는 거기 때문에
    # super()를 사용해서 상위 클래스의 get_queryset을 호출할 필요가 없다.
    def get_queryset(self):  # ListView가 전달하는 object를 바꾸고 싶으면 get_queryset을 오버라이드 한다.(object 여러개)
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(author__id=user_id).order_by('-dt_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))  # 찾는 유저가 없으면 404에러 발생
        return context


class ProfileSetView(LoginRequiredMixin, UpdateView):  # 이미 생성되어 있는 유저 object에 프로필 관련 필드를 설정해주는 역할 -> UpdateView가 적합
    model = User
    form_class = ProfileForm
    template_name = "coplate/profile_set_form.html"

    def get_object(self, queryset=None):  # object 하나
        return self.request.user  # 현재 유저를 return

    def get_success_url(self):  # UpdateView는 항상 업데이트 후 redirect 할 url을 명시해줘야 한다.
        return reverse("index")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):  # 이미 생성되어 있는 유저 object에 프로필 관련 필드를 설정해주는 역할 -> UpdateView가 적합
    model = User
    form_class = ProfileForm
    template_name = "coplate/profile_update_form.html"

    def get_object(self, queryset=None):  # object 하나
        return self.request.user  # 현재 유저를 return

    def get_success_url(self):  # UpdateView는 항상 업데이트 후 redirect 할 url을 명시해줘야 한다.
        return reverse("profile", kwargs=({"user_id": self.request.user.id}))  # url name : profile


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):  # 폼이 성공적으로 처리되면 어디로 리디렉션할 것인지 처리해주는 함수
        return reverse("profile", kwargs=({"user_id": self.request.user.id}))
=======
    def get_success_url(self):  # 폼이 성공적으로 처리되면 어디로 리디렉션할 것인지 처리해주는 함수
        return reverse("index")
>>>>>>> parent of 94f5cf8 (commit_coplate)
