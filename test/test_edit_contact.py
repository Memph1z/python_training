# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "123", "6", "July", "2000", "2", "August", "2001")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
