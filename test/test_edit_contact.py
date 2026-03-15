# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange (1, len(old_contacts))
    contact = Contact("123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "6", "July", "2000", "2", "August", "2001")
    contact.contact_id = old_contacts[index-1].contact_id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index-1] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
