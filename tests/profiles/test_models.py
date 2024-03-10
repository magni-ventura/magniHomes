import pytest

def test_profile_str(profile):
    '''Test the custom user model string representation'''
    assert profile.__str__() == f"{profile.user.username}'s profile"