import ast
from odoo import api, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model_create_multi
    def create(self, vals_list):
        """For checking fields is unique while creating a new contacts."""
        unique_contact_ids = self.env[
            'ir.config_parameter'].sudo().get_param(
            'duplicate_contact_details_alert.unique_contact_ids')
        for vals in vals_list:
            if unique_contact_ids:
                fields_list = ast.literal_eval(unique_contact_ids)
                for x in fields_list:
                    contact_fields = self.env['ir.model.fields'].browse(x)
                    field_vals = contact_fields.name
                    if vals.get(field_vals):
                        partner = self.env['res.partner'].search(
                            [(field_vals, '=', vals.get(field_vals))], limit=1)
                        if partner:
                            raise ValidationError(
                                _("%s è già usata"
                                  " per il contatto %s.") %
                                (contact_fields.name, partner.name))
                else:
                    res = super(ResPartner, self).create(vals)
                    return res
            else:
                res = super(ResPartner, self).create(vals)
                return res

    def write(self, vals):
        """For checking fields is unique while updating a records in
        contacts."""
        unique_contact_ids = self.env[
            'ir.config_parameter'].sudo().get_param(
            'duplicate_contact_details_alert.unique_contact_ids')
        if unique_contact_ids:
            fields_list = ast.literal_eval(unique_contact_ids)
            for x in fields_list:
                contact_fields = self.env['ir.model.fields'].browse(x)
                field_vals = contact_fields.name
                if vals.get(field_vals):
                    partner = self.env['res.partner'].search(
                        [(field_vals, '=', vals.get(field_vals))], limit=1)
                    if partner:
                        raise ValidationError(
                            _("%s è già usata"
                              " per il contatto %s.") %
                            (contact_fields.name, partner.name))
            else:
                res = super(ResPartner, self).write(vals)
                return res
        else:
            res = super(ResPartner, self).write(vals)
            return res
