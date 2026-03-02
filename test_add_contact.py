# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login("admin", "secret")
    app.add_new_contact(Contact("djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "5", "June", "1900", "1", "July", "1901"))
    app.logout()