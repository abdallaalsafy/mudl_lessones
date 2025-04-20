# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from odoo.public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_groups(models.Model):
    _name = 'mdl_groups'
    _description = 'Model Of Groups Data'

    def fnc_renum(self): MainClass().fnc_renum(self)

    name = fields.Char(string="Name", required=True, index=True)
    active = fields.Boolean(string="Active", default=True)
    description = fields.Text()
    fld_courses_id = fields.Many2one('mdl_courses', strting='Courses', ondelete='RESTRICT', required=True)
    fld_sttaf_id = fields.Many2one('mdl_sttaf', strting='Sttaf', ondelete='RESTRICT', required=True)
    fld_days = fields.Many2many('mdl_days', string="Days")
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')