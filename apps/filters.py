# -*- encoding: utf-8 -*-

import os

from datetime import timedelta
from flask import current_app as app

from . utils import constants

HOURS_OFFSET = int(os.getenv('HOURS_OFFSET', -5))


@app.template_filter('date_format')
def date_format(value):
    if value:
        value += timedelta(hours=HOURS_OFFSET)
        return value.strftime(constants.DATE_FORMAT)
    return ''


@app.template_filter('time_format')
def time_format(value):
    if value:
        value += timedelta(hours=HOURS_OFFSET)
        return value.strftime(constants.TIME_FORMAT)
    return ''


@app.template_filter('datetime_format')
def datetime_format(value):
    if value:
        value += timedelta(hours=HOURS_OFFSET)
        return value.strftime(constants.DATETIME_FORMAT)
    return ''
