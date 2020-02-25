# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class report_berp_listado_socios_activos(models.AbstractModel):
    _name = 'report.berp_usuarios.listado_socios'

    @api.model
    def _get_report_values(self, docids, data=None):

        _logger.error('heloudaaaaaa --> %r',docids)
        return {
                'doc_ids':docids,
                'docs':self.env['res.partner'].browse(docids),
                'data':data,
                }
