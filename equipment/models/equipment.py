# -*-coding: utf-8 -*-

from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
import re

class Equipments(models.Model):
    _name = 'equipment'
    _inherit = 'mail.thread'
    _description = 'Equipments'

    name = fields.Char('Name', size=200, required=True,
                       track_visibility="onchange")
    code = fields.Char('Code', size=30, required=True,
                       track_visibility="onchange")
    origin_of_production = fields.Char(
        'Origin Of Production', size=300, required=True, track_visibility="onchange")
    production_date = fields.Date('Production Date', track_visibility='onchange')

    _sql_constraint = [
        ('unique_code', 'unique(code)', 'Code must be unique per equipment'),
    ]

    @api.multi
    @api.constrains('code')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.code):
                raise ValidationError(_("Please Provide valid Code."))