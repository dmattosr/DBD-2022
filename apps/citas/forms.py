# -*- encoding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class StateForm(FlaskForm):
    cmd = StringField(
        'State',
        id='state',
        validators=[DataRequired()])


class CommentForm(FlaskForm):
    comment = StringField(
        'Comment',
        id='comment',
        validators=[DataRequired()])


class UploadForm(FlaskForm):
    file = StringField(
        'Archivo',
        id='file',
        validators=[DataRequired()])
