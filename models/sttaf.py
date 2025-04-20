# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from ..public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_sttaf(models.Model):
    _name = 'mdl_sttaf'
    _description = 'Model Of Sttaf'

    _sql_constraints = [('unique_sttaf_name', 'unique (name)', 'The Name Is Existe Before'),('unique_sttaf_display_name', 'unique (fld_display_name)', 'The Name Is Existe Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    @api.onchange('name')
    def fnc_edit_name(self):
        self.fld_display_name = MainClass().fnc_editstring(self.name)

    name = fields.Char(string="Name", required=True, index=True)
    fld_display_name = fields.Char()
    active = fields.Boolean(string="Active", default=True)
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')

