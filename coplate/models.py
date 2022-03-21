from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters, validate_restaurant_link


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        validators=[validate_no_special_characters],  # nickname 필드에 validator 추가
        error_messages={"unique": "이미 사용중인 닉네임입니다."},
    )

    def __str__(self):
        return self.email


class Review(models.Model):
    title = models.CharField(max_length=30)
    restaurant_name = models.CharField(max_length=20)
    restaurant_link = models.URLField(validators=[validate_restaurant_link])  # 필드값이 url인지 자동으로 확인해 준다.

    RATING_CHOICES = [
        (1, 1),  # (모델필드에 저장되는 값, 화면에 보이는 값)
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)

    image1 = models.ImageField(upload_to="review_pics")  # media 파일의 url주소를 저장하고 form에 업로드된 파일을 MEDIA_ROOT 안에 넣어준다.
    image2 = models.ImageField(upload_to="review_pics", blank=True)
    image3 = models.ImageField(upload_to="review_pics", blank=True)
    content = models.TextField()  # 길이제한이 없는 char 필드
    dt_created = models.DateTimeField(auto_now_add=True)  # auto_now_add : 모델이 생성된 시간을 자동으로 필드에 넣어준다.
    dt_updated = models.DateTimeField(auto_now=True)  # auto_now : 모델이 마지막으로 저장된 시간을 자동으로 필드에 넣어준다.

    def __str__(self):
        return self.title
