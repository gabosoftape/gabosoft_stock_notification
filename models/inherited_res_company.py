# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models

class Company(models.Model):
	_inherit = 'res.company'



	notification_base = fields.Selection([('on_hand','Cantidad a mano'),('fore_cast','Prevista')],string='Notificacion basada en: ',default='on_hand')
	notification_products = fields.Selection([('for_all','Global para todos los productos'),('fore_product',' Individual para todos los productos ')],string='Cantidad minima basada en',default='for_all')
	min_quantity = fields.Float(string = 'Cantidad limite')
	notification_user_id = fields.Many2one('res.users',string = 'Usuario para Notificacion')
