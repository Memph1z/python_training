# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact("This is a test")
    app.session.logout()