import pytest

def test_user_str(base_user):
    '''Test the custom user model string representation'''
    assert base_user.__str__() == f"{base_user.username}"

def test_user_short_name(base_user):
    '''Test the custom user model string representation'''
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    '''Test the custom user model string representation'''
    full_name = f"{base_user.first_name.title()}{base_user.last_name.title()}"
    assert base_user.get_full_name() == full_name

def test_base_user_email_is_normalized(base_user):
    '''Test the that the new users email is normalized'''
    email = base_user.email
    assert base_user.email == base_user.email.lower()

def test_superuser_email_is_normalized(superuser):
    '''Test the that the superusers email is normalized'''
    email = superuser.email
    assert superuser.email == email.lower()

def test_super_user_is_not_staff(user_factory):
    '''Test that an error is raised when an admin has is staff set to false'''
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_staff=True"


def test_superuser_user_is_not_superuser(user_factory):
    '''Test that an error is raised when an admin user is not a superuser'''
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superusers must have is_superuser=True"

def test_create_user_with_no_email(user_factory):
    '''Test that creating a user with no email raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Users must have an email address"

def test_create_user_with_no_username(user_factory):
    '''Test creating a new user with no username raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "Users must submit a username"

def test_create_user_with_no_first_name(user_factory):
    '''Test creating a new user with no first name raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must submit a first name"

def test_create_user_with_no_last_name(user_factory):
    '''Test creating a new user with no last name raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Users must submit a last name"


def test_create_superuser_with_no_email(user_factory):
    '''Test that creating a superuser with no email raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is__superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"

def test_create_superuser_with_no_password(user_factory):
    '''Test that creating a superuser with no password raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(is__superuser=True, password=None)
    assert str(err.value) == "Superusers must have a password"

def test_superuser_email_is_incorrect(user_factory):
    '''Test that creating a superuser with an incorrect email raises an error'''
    with pytest.raises(ValueError) as err:
        user_factory.create(email="<EMAIL>", is__superuser=True, is_staff=True)
    assert str(err.value) == "You must provide a valid email address"