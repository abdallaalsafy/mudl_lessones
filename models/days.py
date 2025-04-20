# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from ..public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_days(models.Model):
    _name = 'mdl_days'
    _description = 'Model Of Days Of Week'

    name = fields.Char(string="Name")