# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.add(Contact("djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "djhfkjs", "5", "June", "1900", "1", "July", "1901"))
