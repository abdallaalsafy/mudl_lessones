# -*- coding: utf-8 -*-

import re
from odoo import models, fields, api, _
from ..public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_students(models.Model):
    _name = 'mdl_students'
    _description = 'Model Of Students Data'

    _sql_constraints = [('unique_students_name', 'unique (name)', 'The Name Is Existe Before'),('unique_students_display_name', 'unique (fld_display_name)', 'The Name Is Existe Before')]

    def fnc_renum(self): MainClass().fnc_renum(self)

    @api.onchange('name')
    def fnc_edit_name(self):
        self.fld_display_name = MainClass().fnc_editstring(self.name)

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            val['fld_Sqnce'] = self.env['ir.sequence'].next_by_code('students_sqnce_code')
        return super(cls_students, self).create(vals)

    fld_Sqnce = fields.Char(string='Students Sqnce', readonly="True", default=lambda self: _('New'))
    name = fields.Char(string="Name", required=True, index=True)
    fld_display_name = fields.Char()
    fld_phone = fields.Char(string="Phone")
    active = fields.Boolean(string="Active", default=True)
    fld_father_phone = fields.Char(string="Father Phone")
    description = fields.Text()
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')

