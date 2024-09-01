# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductCustom(models.Model):
    _name = 'product.custom'
    _description = 'Custom Product Model'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    type = fields.Selection(
        [
            ('fabric', 'Fabric'), 
            ('jeans', 'Jeans'), 
            ('cotton', 'Cotton')
        ],
        string='Type',
        required=True
    )
    buy_price = fields.Float(string='Buy Price', required=True)
    related_supplier_id = fields.Many2one('res.partner', string='Related Supplier', domain=[('is_company', '=', True)])

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Buy Price must be at least 100.')