from ast import literal_eval
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _get_contacts_fields_domain(self):
        """To set domain to the field 'unique_contact_ids'"""
        return [
            ('model', '=', 'res.partner'), ('store', '=', True),
            ('ttype', 'in', ['binary', 'char'])]

    is_unique_contact = fields.Boolean(string="Allerta Unicità Contatti",
                                       help="Richiede che i campi selezionati, "
                                            "siano unici")
    unique_contact_ids = fields.Many2many(
        'ir.model.fields', string='Campi Contatti',
        domain=_get_contacts_fields_domain,
        help='Per evitare i contatti, inserire i campi'
             ' da controllare')

    def set_values(self):
        """Inorder to set values in the setting"""
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'duplicate_contact_details_alert.is_unique_contact',
            self.is_unique_contact)
        self.env['ir.config_parameter'].set_param(
            'duplicate_contact_details_alert.unique_contact_ids',
            self.unique_contact_ids.ids)

    @api.model
    def get_values(self):
        """Inorder to get values from the settings"""
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        contact_field_ids = params.get_param(
            'duplicate_contact_details_alert.unique_contact_ids')
        if contact_field_ids:
            res.update(
                is_unique_contact=params.get_param(
                    'duplicate_contact_details_alert.is_unique_contact'),
                unique_contact_ids=[(6, 0, literal_eval(contact_field_ids))],
            )
            return res
        else:
            return res
