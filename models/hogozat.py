# -*- coding: utf-8 -*-

import re

from odoo import models, fields, api, _
from odoo.public_class import MainClass
from odoo.exceptions import ValidationError, UserError


class cls_hogozat(models.Model):
    _name = 'mdl_hogozat'
    _description = 'Model Of hogozat Data'

    def fnc_renum(self): MainClass().fnc_renum(self)

    fld_students_id = fields.Many2one('mdl_students', strting='Students', ondelete='RESTRICT', required=True)
    fld_courses_id = fields.Many2one('mdl_courses', strting='Courses', ondelete='RESTRICT', required=True)
    fld_sttaf_id = fields.Many2one('mdl_sttaf', strting='Sttaf', ondelete='RESTRICT', required=True)
    fld_groups_id = fields.Many2one('mdl_groups', strting='Groups', ondelete='SET NULL')
    description = fields.Text()
    fld_sonum = fields.Integer(string='SoNum', compute='fnc_renum')