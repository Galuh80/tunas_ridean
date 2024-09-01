# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as dt_format

class ProductCustomController(http.Controller):
    
    def serialize_record(self, record):
        def serialize(obj):
            if isinstance(obj, datetime):
                return obj.strftime(dt_format)
            if isinstance(obj, tuple):
                return list(obj)
            raise TypeError(f"Type {type(obj)} not serializable")
        
        return json.loads(json.dumps(record, default=serialize))

    @http.route('/api/product_custom', type='json', auth='public', methods=['POST'], csrf=False)
    def create_product(self, **kwargs):
        try:
            data = request.jsonrequest
            product = request.env['product.custom'].sudo().create(data)
            return {'status': 'success', 'id': product.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        
    @http.route('/api/product_custom', type='json', auth='public', methods=['GET'], csrf=False)
    def get_all_products(self):
        try:
            products = request.env['product.custom'].sudo().search([])
            product_data = []
            for product in products:
                product_data.append({
                    'id': product.id,
                    'code': product.code,
                    'name': product.name,
                    'type': product.type,
                    'buy_price': product.buy_price,
                    'related_supplier_id': product.related_supplier_id.name if product.related_supplier_id else None,
                    'create_date': product.create_date,
                    'write_date': product.write_date,
                })
            serialized_product = self.serialize_record(product_data)
            return {'status': 'success', 'products': serialized_product}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    @http.route('/api/product_custom/<int:product_id>', type='json', auth='public', methods=['GET'], csrf=False)
    def get_product(self, product_id):
        try:
            product = request.env['product.custom'].sudo().browse(product_id)
            if not product:
                return {'status': 'error', 'message': 'Product not found'}
            product_data = product.read()[0]
            serialized_product = self.serialize_record(product_data)
            return {'status': 'success', 'product': serialized_product}
        except Exception as e:
            return {'status': 'error', 'message': 'Product not found'}

    @http.route('/api/product_custom/<int:product_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_product(self, product_id, **kwargs):
        try:
            data = request.jsonrequest
            product = request.env['product.custom'].sudo().browse(product_id)
            if not product:
                return {'status': 'error', 'message': 'Product not found'}
            product.sudo().write(data)
            return {'status': 'success', 'message': 'Product updated'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    @http.route('/api/product_custom/<int:product_id>', type='json', auth='public', methods=['DELETE'], csrf=False)
    def delete_product(self, product_id):
        try:
            product = request.env['product.custom'].sudo().browse(product_id)
            if not product:
                return {'status': 'error', 'message': 'Product not found'}
            product.sudo().unlink()
            return {'status': 'success', 'message': 'Product deleted'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}


