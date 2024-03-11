from odoo import fields, models


class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor'

    f_name = fields.Char('First Name')
    l_name = fields.Char('Last Name')
    image = fields.Binary()
    patient_ids = fields.Many2many('hms.patient')