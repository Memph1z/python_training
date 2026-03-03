# -*- coding: utf-8 -*-

def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group("This is a test")
    app.session.logout()