import numbers
import string
from django.core.exceptions import ValidationError


# 특수문자 포함되어 있는지 확인
def contains_special_character(value):
    for char in value:
        if char in string.punctuation:  # string.punctuation : 특수문자를 모아놓은 문자열
            return True
    return False


# 대문자 포함되어 있는지 확인
def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False


# 소문자 포함되어 있는지 확인
def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False


# 숫자 포함되어 있는지 확인
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


class CustomPasswordValidator:  # 비밀번호 유효성 검사는 클래스형 validator 사용한다.
    def validate(self, password, user=None):  # 클래스형 validator는 validate라는 함수를 정의해야 한다.
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self):  # admin 페이지에서 비밀번호를 변경할 때 필요한 내용
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."
        

# 특수문자가 있으면 밸리데이션 에러를 발생시키는 함수
def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자를 포함할 수 없습니다.")


def validate_restaurant_link(value):
    if "place.naver.com" not in value and "place.map.kakao.com" not in value:
        raise ValidationError("place.naver.com 또는 place.map.kakao.com이 들어가야 합니다.")