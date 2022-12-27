# -*- encoding: utf-8 -*-

import os
import uuid
from datetime import datetime


class Constants(object):
    SEXO_MASCULINO = 'M'
    SEXO_FEMENINO = 'F'

    TIPODOCUMENTO_DNI = '01'
    TIPODOCUMENTO_CE = '02'

    TIPOSEGURO_NINGUNO = '0'


constants = Constants()


def _default_uuid():
    return str(uuid.uuid4())[-1 * constants.SIZE_UUID:]


YEAR_LIST = [
    (str(year), str(year))
    for year in (2016, datetime.now().year)
][::-1]
