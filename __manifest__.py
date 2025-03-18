{
    'name': 'TECH 3.0 Common Module',
    'version': '1.0',
    'summary': 'Aggiunge le personalizzazioni TECH Odoo 18',
    'description': 'Possibilità di cambiare Favicon, Windows Tab Name, Rimuove Powered By Odoo, nella sezione generali->contatti spacifica l\' unicità dei contatti',
    'author': 'TECH 3.0 Srl',
    'depends': ['base','base_setup','web'],
    'data': [
        'views/settings/inherit_res_config_settings_view.xml',
        'views/settings/web_login.xml',
        'views/settings/portal_templates.xml',
        'views/settings/webclient_templates.xml',
        'views/settings/res_company_views.xml',
        'views/settings/templates.xml',
        'views/contact/res_config_settings_views.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'tech_common_settings/static/src/js/web_window_title_customize.js',
        ],
    },

    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}