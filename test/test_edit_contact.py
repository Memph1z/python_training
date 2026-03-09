# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact("123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "6", "July", "2000", "2", "August", "2001"))
