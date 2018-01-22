# -*-coding: utf-8 -*-

from odoo import fields, api, models, _

class Imports(models.Model):
    _name = 'imports'
    _inherit = 'mail.thread'
    _description = 'Imports'

    lot_id = fields.Many2one ('lots', 'Lot', required=True, track_visibility='onchange')
    lot_code = fields.Char('Lot Code', related='lot_id.code', readonly=True)
    imports_equipment_rela_ids = fields.One2many('import.equipment.relation','imports_id',string='equipment(s)')
    price = fields.Float('Total Price', compute='_compute_price',readonly=True)

    @api.multi
    @api.depends('imports_equipment_rela_ids')
    def _compute_price(self):
            for record in self.imports_equipment_rela_ids:
                self.price += record.total_cost