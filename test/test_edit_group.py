# -*- coding: utf-8 -*-

def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="Test group", header="Test header", footer="Test footer"))
    app.session.logout()