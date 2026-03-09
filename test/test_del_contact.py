# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    app.contact.delete_first_contact()
