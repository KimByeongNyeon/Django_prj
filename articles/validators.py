from django.core.exceptions import ValidationError


def title_validate(value):
    if (len(value) > 9) or (len(value) <= 0):
        err = '제목은 0 글자 초과 9글자 미만으로 적어주세요'
        raise ValidationError(err)
