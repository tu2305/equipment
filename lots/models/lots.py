# -*-coding: utf-8 -*-

from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
import re

class Lots(models.Model):
    _name = 'lots'
    _inherit = 'mail.thread'
    _description = 'Lots'

    name = fields.Char('Name', size=200, required=True,
                       track_visibility="onchange")
    code = fields.Char('Code', size=30, required=True,
                       track_visibility="onchange")
    equipment_id = fields.Many2one('equipment','Equipment', required=True, track_visibility="onchange")
    equipment_code = fields.Char('Equipment Number', related='equipment_id.code', readonly=True)
    quantity = fields.Float('Quantity', track_visibility='onchange')
    cost = fields.Float('Cost', track_visibility='onchange')
    total_cost = fields.Float('Total Cost', compute='_compute_total_cost', readonly=True)
    date_added = fields.Date('Date Added', required=True, track_visibility='onchange')

    _sql_constraint = [
        ('unique_code_equipment', 'unique(code,equipment_id)', 'Code must be unique per equipment in lot'),
    ]

    @api.multi
    @api.constrains('code')
    def _compute_special_character_code(self):
        for record in self:
            if not re.match("^[a-zA-Z0-9_/\\\\]*$", record.code):
                raise ValidationError(_("Please Provide valid Code."))

    @api.multi
    @api.depends('cost','quantity')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.quantity * record.cost