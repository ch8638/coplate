from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # review urls
    path("", views.IndexView.as_view(), name="index"),
    path("reviews/<int:review_id>/", views.ReviewDetailView.as_view(), name="review-detail"),
    # <int:review_id> : id 값을 넘겨준다.
    path("reviews/new/", views.ReviewCreateView.as_view(), name="review-create"),
    path("reviews/<int:review_id>/edit/", views.ReviewUpdateView.as_view(), name="review-update"),
    path("reviews/<int:review_id>/delete", views.ReviewDeleteView.as_view(), name="review-delete"),

    # profile urls
    path("user/<int:user_id>/", views.ProfileView.as_view(), name="profile"),
    path('user/<int:user_id>/reviews/', views.UserReviewListView.as_view(), name="user-review-list"),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    path("edit-profile/", views.ProfileUpdateView.as_view(), name="profile-update"),
]
