# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from ..public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_courses(models.Model):
    _name = 'mdl_courses'
    _description = 'Model Of Courses Data'

    _sql_constraints = [('unique_courses_name', 'unique (name)', 'The courses Is Existe Before'),('unique_students_display_name', 'unique (fld_display_name)', 'The courses Is Existe Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    @api.onchange('name')
    def fnc_edit_name(self):
        self.fld_display_name = MainClass().fnc_editstring(self.name)

    name = fields.Char(string="Name", required=True, index=True)
    fld_display_name = fields.Char()
    active = fields.Boolean(string="Active", default=True)
    description = fields.Text()
    fld_term = fields.Selection([('a', 'First Term'), ('b', 'Second Term'), ('c', 'No Term')], string="The Term")
    fld_begin = fields.Date(string='Begin Date', default=fields.Date.today)
    fld_end = fields.Date(string='End Date')
    fld_closed = fields.Boolean(string="Closed")
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')