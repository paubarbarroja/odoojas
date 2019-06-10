# -*- coding: utf-8 -*-
from datetime import date, datetime
from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"

    #raise exceptions.except_orm(_('Error!!'), _('No has introducido bien la marca'))

    @api.multi
    def _get_categoria(self):
        if self.atleta:
            if self.atleta.fecha_nac:
                nacimiento = self.atleta.fecha_nac
                hoy = date.today()
                fecha_hoy = hoy.strftime('%Y-%m-%d').split('-')
                fecha = "31-12-" + fecha_hoy[0]
                date_object = datetime.strptime(fecha, '%d-%m-%Y').date()
                diferencia = date_object - nacimiento
                edad_final_temporada = str(int(diferencia.days/365))
                edad = int(edad_final_temporada)

                if edad > 34:
                    categoria = "Master"
                else:
                    if edad > 22:
                        categoria = "Senior"
                    else:
                        if edad > 19:
                            categoria = "Sub 23"
                        else:
                            if edad > 17:
                                categoria = "Sub 20"
                            else:
                                if edad > 15:
                                    categoria = "Sub 18"
                                else:
                                    if edad > 13:
                                        categoria = "Sub 16"

        else:
            categoria = ""
        return categoria

    @api.onchange('atleta')
    def onchange_socio(self):
        categoria = self._get_categoria()
        self.categoria = categoria
        self.prueba = False
        self.marca = False
        self.marca_s = False


    @api.onchange('prueba')
    def onchange_prueba(self):
        if self.prueba:
            if self.prueba.especialidad:
                if self.prueba.especialidad == '4' or self.prueba.especialidad == '5':
                    self.hide = True
                else:
                    self.hide = False


    @api.onchange('marca_s')
    def onchange_marca_s(self):
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
                        while not puntos_por_prueba_ids:
                            marca = round((marca - 0.01),2)
                            puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', self.prueba.id), ('marca', '=', marca)])
                    else:
                        while not puntos_por_prueba_ids:
                            marca = round((marca - 0.01),2)
                            puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', self.prueba.id), ('marca', '=', marca)])
                    for id in puntos_por_prueba_ids:
                        object = self.env['berp.puntos_hungaros'].browse(id)
                        if marca == object.id.marca:
                            id = object.id.id
        return id


    @api.onchange('marca')
    def onchange_marca(self):
        if self.marca:
            if self.prueba.especialidad == '4' or self.prueba.especialidad == '5':
                self.marca_s = str(self.marca)
            self.puntos_hungaros = self._get_puntos_hungaros()

    @api.multi
    def write(self, values):
        categoria = self._get_categoria()
        puntos_hungaros = self._get_puntos_hungaros()
        values.update({'categoria':categoria,'puntos_hungaros':puntos_hungaros})
        res = super(berp_marca, self).write(values)
        return res



    @api.model
    def create(self, values):
        id = False
        categoria = ""
        if 'atleta' in values:
            atleta = self.env['berp.socio'].browse(values['atleta'])
            nacimiento = atleta.fecha_nac
            hoy = date.today()
            fecha_hoy = hoy.strftime('%Y-%m-%d').split('-')
            fecha = "31-12-" + fecha_hoy[0]
            date_object = datetime.strptime(fecha, '%d-%m-%Y').date()
            diferencia = date_object - nacimiento
            edad_final_temporada = str(int(diferencia.days / 365))
            edad = int(edad_final_temporada)

            if edad > 34:
                categoria = "Master"
            else:
                if edad > 22:
                    categoria = "Senior"
                else:
                    if edad > 19:
                        categoria = "Sub 23"
                    else:
                        if edad > 17:
                            categoria = "Sub 20"
                        else:
                            if edad > 15:
                                categoria = "Sub 18"
                            else:
                                if edad > 13:
                                    categoria = "Sub 16"

        if 'prueba' in values:
            prueba = self.env['berp.prueba'].browse(values['prueba'])
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
                        for id in puntos_por_prueba_ids:
                            object = self.env['berp.puntos_hungaros'].browse(id)
                            if marca == object.id.marca:
                                id = object.id.id
                                if prueba.especialidad == '4' or prueba.especialidad == '5':
                                    values.update({'marca_s': str(marca), 'hide': True})
                    else:
                        if prueba.especialidad == '4' or prueba.especialidad == '5':
                            if self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '<', marca), ('marca', '!=', 0.00)]):
                                raise exceptions.except_orm(_('Error!!'), _(self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '<', marca), ('marca', '!=', 0.00)])))
                                '''while not puntos_por_prueba_ids:
                                    marca = round((marca - 0.01), 2)
                                    puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '=', marca)])
                                values.update({'marca_s': str(marca), 'hide': True})'''
                        else:
                            if self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '>', marca), ('marca', '!=', 0.00)]):
                                while not puntos_por_prueba_ids:
                                    marca = round((marca - 0.01), 2)
                                    puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba', '=', prueba.id), ('marca', '=', marca)])
                        for id in puntos_por_prueba_ids:
                                object = self.env['berp.puntos_hungaros'].browse(id)
                                if marca == object.id.marca:
                                    id = object.id.id

        values.update({'categoria': categoria, 'puntos_hungaros': id})
        res = super(berp_marca, self).create(values)
        return res

    atleta = fields.Many2one('berp.socio',string="Socio")
    genero_atleta = fields.Selection(related="atleta.genero", store="True")
    prueba = fields.Many2one('berp.prueba',string="Prueba")
    evento = fields.Many2one('berp.evento',string="Evento")
    fecha = fields.Date(related="evento.fecha",store="True")
    marca = fields.Float(string="Marca")
    marca_s = fields.Char(string="Marca_s", help="Unidad : metros --> '50,50'   ;   tiempo --> '1:30.55'", default="00:00.00")
    hide = fields.Boolean(string='Hide',default=False)
    puntos_hungaros = fields.Many2one('berp.puntos_hungaros',string="Puntos Hungaros")
    categoria = fields.Char(string="Categoria")
    importado = fields.Boolean(string="Importado",default=False)