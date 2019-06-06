# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.osv import osv
import logging

_logger = logging.getLogger(__name__)

class berp_marca(models.Model):
    _name = "berp.marca"
    # todo
    #  Pensar bien la manera de mostrar las marcas en los otros formularios,
    #  1-  para crear una variable conjunta de todas como pn/sn/ref.origen/lote de helipistas
    #  2-  o si al contrario se mostrara en O2M y se veran todas las variables en forma de tree
    #_rec_name = "nombre"

    '''
    def hlp_str_to_float_time(time_string):
        fields = time_string.split(":")
        hours = fields[0] if len(fields) > 0 else 0.0
        minutes = fields[1] if len(fields) > 1 else 0.0
        seconds = fields[2] if len(fields) > 2 else 0.0
        return float(hours) + (float(minutes) / 60.0) + (float(seconds) / pow(60.0, 2))
'''

    @api.onchange('atleta')
    def onchange_atleta(self):
        if self.atleta:
            if self.atleta.genero:
                if self.atleta.genero == '1':
                    return {'domain': {'prueba': [('genero', '=', '1')]}}
                else:
                    return {'domain': {'prueba': [('genero', '=', '2')]}}

    @api.onchange('marca_s')
    def onchange_marca_s(self):
        if self.prueba:
            if self.prueba.especialidad:
                especialidad = self.prueba.especialidad
                if self.marca_s:
                    if especialidad == '4' or especialidad == '5':
                        self.marca = float(self.marca_s)
                    else:
                        if self.marca_s.find(":"):
                            tiempo = self.marca_s.split(":")
                            minutos = tiempo[0] if len(tiempo) > 0 else '0'
                            if tiempo[1].find("."):
                                seg_cent = tiempo[1].split(".")
                                segundos = seg_cent[0] if len(seg_cent) > 0 else '0'
                                centesimas = seg_cent[1] if len(seg_cent) > 1 else '0'
                            else:
                                raise exceptions.except_orm(_('Error!!'), _('No has introducido bien la marca'))
                        else:
                            if self.marca_s.find("."):
                                seg_cent = self.marca_s.split(".")
                                segundos = seg_cent[0] if len(seg_cent) > 0 else '0'
                                centesimas = seg_cent[1] if len(seg_cent) > 1 else '0'
                            else:
                                raise exceptions.ValidationError('Error!! \nNo has introducido bien la marca')
                        self.marca = float(segundos)+(float(minutos)*60)+(float(centesimas)/100)



    atleta = fields.Many2one('berp.socio',string="Socio")
    prueba = fields.Many2one('berp.prueba',string="Prueba")
    evento = fields.Many2one('berp.evento',string="Evento")
    marca = fields.Float(string="Marca")
    marca_s = fields.Char(string="Marca", help="Unidad : metros --> '50,50'   ;   tiempo --> '1:30.55'")



    '''
    apellidos           = fields.Char(string='Apellido',required=True)
    ficha               = fields.Date(string='ficha',required=True)
    dni                 = fields.Char(string='dni',required=True)
    edad                = fields.Date(string='edad',required=True)
    genero              = fields.Selection([('1', 'Masculino'),('2', 'Femenino')],string='genero',required=True)
    telefono            = fields.Char(string='telefono',required=True)
    mail                = fields.Char(string='mail',required=True)
    '''