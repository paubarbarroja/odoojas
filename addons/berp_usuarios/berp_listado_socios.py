# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class report_berp_listado_socios_activos(models.AbstractModel):
    _name = 'report.berp_usuarios.listado_socios'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
                'doc_ids':docids,
                'docs':sorted(self.env['res.partner'].browse(docids).items(),key = lambda kv:(kv[1], kv[0])),
                'data':data,
                }
