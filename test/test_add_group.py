# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.create(Group("fsdfsd66fsdf", "fsd6fsdfsdf", "fsdf6sdfsdf"))

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))
