# -*- coding: utf-8 -*-
from datetime import date, datetime
from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"

    @api.onchange('atleta')
    def onchange_atleta(self):
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
                    self.categoria = "Master"
                else:
                    if edad > 22:
                        self.categoria = "Senior"
                    else:
                        if edad > 19:
                            self.categoria = "Sub 23"
                        else:
                            if edad > 17:
                                self.categoria = "Sub 20"
                            else:
                                if edad > 15:
                                    self.categoria = "Sub 18"
                                else:
                                    if edad > 13:
                                        self.categoria = "Sub 16"
        else:
            self.categoria = ""


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
                if min_seg.find(":"):
                    tiempo_v2 = min_seg.split(":")
                    minutos = tiempo_v2[0] if len(tiempo_v2) > 0 else '0'
                    segundos = tiempo_v2[1] if len(tiempo_v2) > 1 else '0'
                else:
                    segundos = min_seg
                    minutos = '0'
            self.marca = float(segundos)+(float(minutos)*60)+(float(centesimas)/100)

    @api.onchange('marca')
    def onchange_marca(self):
        if self.marca:
            if self.prueba:
                puntos_por_prueba_ids = self.env['berp.puntos_hungaros'].search([('prueba','=',self.prueba.id),('marca','=',self.marca)])
                for id in puntos_por_prueba_ids:
                    object = self.env['berp.puntos_hungaros'].browse(id)
                    if self.marca == object.id.marca:
                        self.puntos_hungaros = object.id.puntos


    #todo Comprobar la tabla de los puntos hungaros y poner los puntos que equivalen a la marca introducida.

    atleta = fields.Many2one('berp.socio',string="Socio")
    genero_atleta = fields.Selection(related="atleta.genero", store="True")
    prueba = fields.Many2one('berp.prueba',string="Prueba")
    evento = fields.Many2one('berp.evento',string="Evento")
    fecha = fields.Date(related="evento.fecha",store="True")
    marca = fields.Float(string="Marca")
    marca_s = fields.Char(string="Marca", help="Unidad : metros --> '50,50'   ;   tiempo --> '1:30.55'", default="00:00.00")
    hide = fields.Boolean(string='Hide',default=False)
    puntos_hungaros = fields.Many2one('berp.puntos_hungaros',string="Puntos Hungaros")
    categoria = fields.Char(string="Categoria")
