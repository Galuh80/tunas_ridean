# -*- coding: utf-8 -*-
import logging
import colorlog
import psycopg2
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
))
logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class TestProductCustom(TransactionCase):

    def setUp(self):
        super(TestProductCustom, self).setUp()
        self.ProductCustom = self.env['product.custom']
        self.ResPartner = self.env['res.partner']

        self.supplier = self.ResPartner.create({
            'name': 'Test Supplier',
            'is_company': True,
        })

    def test_create_product_custom(self):
        product = self.ProductCustom.create({
            'code': 'P001',
            'name': 'Test Product',
            'type': 'fabric',
            'buy_price': 150.0,
            'related_supplier_id': self.supplier.id,
        })
        self.assertEqual(product.code, 'P001')
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.type, 'fabric')
        self.assertEqual(product.buy_price, 150.0)
        self.assertEqual(product.related_supplier_id, self.supplier)
        logger.info("TEST PASSED")

    def test_buy_price_constraint(self):
        try:
            product = self.ProductCustom.create({
                'code': 'P002',
                'name': 'Test Product 2',
                'type': 'jeans',
                'buy_price': 120.0,
                'related_supplier_id': self.supplier.id,
            })
            if product.buy_price > 100:
                logger.info("TEST PASSED")
            else:
                logger.error("TEST FAILED, Buy price < 100")
        except ValidationError:
            logger.error("TEST FAILED, Buy price < 100")

    def test_update_product_custom(self):
        product = self.ProductCustom.create({
            'code': 'P003',
            'name': 'Test Product 3',
            'type': 'cotton',
            'buy_price': 200.0,
            'related_supplier_id': self.supplier.id,
        })
        product.write({
            'name': 'Updated Product 3',
            'buy_price': 250.0,
        })
        self.assertEqual(product.name, 'Updated Product 3')
        self.assertEqual(product.buy_price, 250.0)
        logger.info("TEST PASSED")

    def test_delete_product_custom(self):
        product = self.ProductCustom.create({
            'code': 'P004',
            'name': 'Test Product 4',
            'type': 'fabric',
            'buy_price': 300.0,
            'related_supplier_id': self.supplier.id,
        })
        product_id = product.id
        product.unlink()
        product_deleted = self.ProductCustom.search([('id', '=', product_id)])
        self.assertFalse(product_deleted)
        logger.info("TEST PASSED")
    
    def test_missing_field(self):
        with self.assertRaises(psycopg2.errors.NotNullViolation) as cm:
            self.ProductCustom.create({
                'code': 'P005',
                # 'name' is missing
                'type': 'fabric',
                'buy_price': 100.0,
                'related_supplier_id': self.supplier.id,
            })
        exception = cm.exception
        self.assertIn('null value in column "name"', str(exception))
        logger.info("TEST PASSED, NotNullViolation raised as expected")
