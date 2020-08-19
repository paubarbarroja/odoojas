# -*- coding: utf-8 -*-

from datetime import date, datetime
from odoo import models, fields, api, tools, exceptions, _
from odoo.modules import get_module_resource
import base64
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    

    @api.depends('order_line')
    def _get_productos(self):
        for record in self:
            txt = ""
            for line in record.order_line:
                if txt == "":
                    txt =  line.name
                else:
                    txt = txt + '; ' + line.name
            record.producto_tree = txt

    
    
    producto_tree           = fields.Text(compute='_get_productos',string='Productos',store=True)

    