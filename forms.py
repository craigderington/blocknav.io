# -*- coding: utf-8 -*-
from wtforms import Form, BooleanField, StringField, PasswordField, validators


class SearchForm(Form):
    search = StringField('Search', [validators.DataRequired()])


class AddressSearchForm(Form):
    addr = StringField('Address', [validators.DataRequired()])


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])