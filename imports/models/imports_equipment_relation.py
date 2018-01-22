# -*-coding: utf-8 -*-

from odoo import fields, api, models, _

class ImportsEquipmentRelation(models.Model):
    _name = 'import.equipment.relation'
    _inherit = 'mail.thread'

    imports_id = fields.Many2one('imports','Import', required=True)
    equipment_id = fields.Many2one('equipment','Equipment', track_visibility='onchange')
    quantity = fields.Float('Quantity', track_visibility='onchange')
    cost = fields.Float('Cost', related='imports_id.lot_id.cost', track_visibility='onchange', readonly=True)
    total_cost = fields.Float('Total cost', compute='_compute_total_cost', readonly=True)

    @api.multi
    @api.depends('cost', 'quantity')
    def _compute_total_cost(self):
        for record in self:
            record.total_cost = record.quantity * record.cost

    _sql_constraint = [
        ('unique_equipment', 'unique(equipment_id)', 'Equipment must be unique per lot'),
    ]