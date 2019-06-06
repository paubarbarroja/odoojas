# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api, exceptions
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"

    '''
    !!--- Domain dinamico a partir de un onchange ---!!
    return {'domain': {'prueba': [('genero', '=', '1')]}}
    '''

    @api.onchange('atleta')
    def onchange_atleta(self):
        if self.atleta:
            if self.atleta.fecha_nac:
                nacimiento = self.atleta.fecha_nac
                '''hoy = date.today()
                diferencia = hoy - nacimiento
                self.categoria = str(int(diferencia.days/365))
                '''
                fecha = nacimiento.strftime('%Y-%m-%d').split('-')
                año = fecha[0]
                self.categoria = año
                if año == "1996" or año == "":
                    año = "a"
    #todo tengo el año en string -- comprobar de que año es i poner categoria en el campo


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
        hola = 1
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




    '''
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
    '''