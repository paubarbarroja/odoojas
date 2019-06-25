# -*- coding: utf-8 -*-
from datetime import date, datetime
from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"

    # raise exceptions.except_orm(_('Error!!'), _('No has introducido bien la marca'))


    '''####################################################'''
    '''########  Funcion onchange del campo atleta ########'''
    '''####################################################'''
    @api.onchange('atleta')
    def onchange_socio(self):
        self.categoria = self.atleta.categoria
        self.prueba = False
        self.marca = False
        self.marca_s = False


    '''####################################################'''
    '''########  Funcion onchange del campo prueba ########'''
    '''####################################################'''
    @api.onchange('prueba')
    def onchange_prueba(self):
        if self.prueba:
            if self.prueba.especialidad:
                if self.prueba.especialidad == '4' or self.prueba.especialidad == '5':
                    self.hide = True
                else:
                    self.hide = False


    '''#####################################################'''
    '''########  Funcion onchange del campo marca_s ########'''
    '''#####################################################'''
    @api.onchange('marca_s')
    def onchange_marca_s(self):
        if not self.marca:
            if self.marca_s:
                if self.marca_s.find("."):
                    tiempo = self.marca_s.split(".")
                    min_seg = tiempo[0] if len(tiempo) > 0 else '0'
                    centesimas = tiempo[1] if len(tiempo) > 1 else '0'
                    if min_seg.find(":") == 2:
                        tiempo_v2 = min_seg.split(":")
                        minutos = tiempo_v2[0] if len(tiempo_v2) > 0 else '0'
                        segundos = tiempo_v2[1] if len(tiempo_v2) > 1 else '0'
                    else:
                        segundos = min_seg
                        minutos = '0'
                self.marca = float(segundos)+(float(minutos)*60)+(float(centesimas)/100)



    def _get_puntos_hungaros(self):
        id = False
        if self.marca:
            if self.prueba:
                marca = self.marca
                puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba','=',self.prueba.id),('marca','=',marca)])
                if puntos_por_prueba_ids:
                    for id in puntos_por_prueba_ids:
                        object = self.env['berp.puntos_hungaros'].browse(id)
                        if marca == object.id.marca:
                            id = object.id.id
                else:
                    if self.prueba.especialidad == '4' or self.prueba.especialidad == '5':
                        if self.env['berp.puntos_hungaros'].search([('prueba', '=', self.prueba.id), ('marca', '<', marca), ('marca', '!=', 0.00)]):
                            while not puntos_por_prueba_ids:
                                marca = round((marca - 0.01),2)
                                puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', self.prueba.id), ('marca', '=', marca)])
                    else:
                        if self.env['berp.puntos_hungaros'].search([('prueba', '=', self.prueba.id), ('marca', '>', marca), ('marca', '!=', 0.00)]):
                            while not puntos_por_prueba_ids:
                                marca = round((marca - 0.01),2)
                                puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', self.prueba.id), ('marca', '=', marca)])
                    for id in puntos_por_prueba_ids:
                        object = self.env['berp.puntos_hungaros'].browse(id)
                        if marca == object.id.marca:
                            id = object.id.id

        if not id:
            id = 1
        return id


    '''###################################################'''
    '''########  Funcion onchange del campo marca ########'''
    '''###################################################'''
    @api.onchange('marca')
    def onchange_marca(self):
        if self.marca:
            if self.prueba.especialidad == '4' or self.prueba.especialidad == '5':
                self.marca_s = str(self.marca)
            self.puntos_hungaros = self._get_puntos_hungaros()



    '''###############################################'''
    '''########  Override de la funcion Write ########'''
    '''###############################################'''
    @api.multi
    def write(self, values):
        categoria = self._get_categoria()
        puntos_hungaros = self._get_puntos_hungaros()
        values.update({'categoria':categoria,'puntos_hungaros':puntos_hungaros})
        res = super(berp_marca, self).write(values)
        return res



    '''################################################'''
    '''########  Override de la funcion Create ########'''
    '''################################################'''
    @api.model
    def create(self, values):
        id = False
        if 'prueba' in values:
            prueba = self.env['berp.prueba'].browse(values['prueba'])
            if prueba.especialidad != '4' and prueba.especialidad != '5':
                if 'marca_s' in values:
                    marca_s = values['marca_s']
                    if marca_s != "0.0":
                        if marca_s.find("."):
                            tiempo = marca_s.split(".")
                            min_seg = tiempo[0] if len(tiempo) > 0 else '0'
                            centesimas = tiempo[1] if len(tiempo) > 1 else '0'
                            if min_seg.find(":") == 2:
                                tiempo_v2 = min_seg.split(":")
                                minutos = tiempo_v2[0] if len(tiempo_v2) > 0 else '0'
                                segundos = tiempo_v2[1] if len(tiempo_v2) > 1 else '0'
                            else:
                                segundos = min_seg
                                minutos = '0'
                        values.update({'marca': (float(segundos) + (float(minutos) * 60) + (float(centesimas) / 100))})
            if 'marca' in values:
                if values['marca'] != 0:
                    marca = values['marca']
                    puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '=', marca)])
                    if puntos_por_prueba_ids:
                        for ids in puntos_por_prueba_ids:
                            object = self.env['berp.puntos_hungaros'].browse(ids)
                            if marca == object.id.marca:
                                id = object.id.id
                                if prueba.especialidad == '4' or prueba.especialidad == '5':
                                    values.update({'marca_s': str(marca), 'hide': True})
                    else:
                        if prueba.especialidad == '4' or prueba.especialidad == '5':
                            if self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '<', marca), ('marca', '!=', 0.00)]):
                                while not puntos_por_prueba_ids:
                                    marca = round((marca - 0.01), 2)
                                    puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '=', marca)])
                                values.update({'marca_s': str(marca), 'hide': True})
                            else:
                                id = 1
                        else:
                            if self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '>', marca), ('marca', '!=', 0.00)]):
                                while not puntos_por_prueba_ids:
                                    marca = round((marca - 0.01), 2)
                                    puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '=', marca)])
                            else:
                                id = 1
                        for ids in puntos_por_prueba_ids:
                                object = self.env['berp.puntos_hungaros'].browse(ids)
                                if marca == object.id.marca:
                                    id = object.id.id

        values.update({'puntos_hungaros': id})
        res = super(berp_marca, self).create(values)
        return res


    '''###########################################'''
    '''###########################################'''
    '''########  Campos de la clase marca ########'''
    '''###########################################'''
    '''###########################################'''

    atleta = fields.Many2one('berp.socio',string="Socio", required="True")
    genero_atleta = fields.Selection(related="atleta.genero", store="True")
    prueba = fields.Many2one('berp.prueba',string="Prueba", required="True")
    evento = fields.Many2one('berp.evento',string="Evento", required="True")
    fecha = fields.Date(related="evento.fecha",store="True")
    marca = fields.Float(string="Marca")
    marca_s = fields.Char(string="Marca_s", help="Unidad : metros --> '50.50'   ;   tiempo --> '1:30.55'", default="00:00.00")
    hide = fields.Boolean(string='Hide',default=False)
    puntos_hungaros = fields.Many2one('berp.puntos_hungaros',string="Puntos Hungaros")
    categoria = fields.Char(related="atleta.categoria", store="True")
    importado = fields.Boolean(string="Importado",default=False)