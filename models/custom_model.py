# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CustomProductManufacturer(models.Model):
    _name = 'product.manufacturer'
    _description = 'Product Manufacturer'

    name = fields.Char('Manufacturer', required=True)


class CustomProductModel(models.Model):
    _name = 'product.model'
    _description = 'Product Model'

    name = fields.Char('Model', required=True)
    parent_id = fields.Many2one('product.manufacturer', 'Manufacturer')


class CustomProductTemplate(models.Model):
    _inherit = 'product.template'

    manufacturer = fields.Many2one('product.manufacturer', 'Manufacturer')
    model = fields.Many2one('product.model', 'Model')

    @api.onchange('manufacturer')
    def create_domain(self):
        data_model = self.env['product.model'].search([('parent_id', '=',
                                                        self.manufacturer.id)])
        models = [data.id for data in data_model]
        self.model=False
        return {'domain': {'model': [('id','in',models)]}}
