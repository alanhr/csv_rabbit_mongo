from csv_read.model.User import User


def __is_exists(user):
    user_find = User.objects(email=user.get('email')).first()
    
    return True if user_find else False


def create(user):
    if __is_exists(user):
        raise Exception('this email {} was already registered'.format(
            user.get('email')
        ))

    return User.objects.create(**user)
