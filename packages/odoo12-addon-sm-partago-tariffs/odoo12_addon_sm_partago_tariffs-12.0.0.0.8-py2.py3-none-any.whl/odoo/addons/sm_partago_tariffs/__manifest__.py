# -*- coding: utf-8 -*-
{
    'name': "sm_partago_tariffs",

    'summary': """
    Dynamic and complex carsharing tariffs for the system
  """,

    'description': """
    Dynamic and complex carsharing tariffs for the system
  """,

    'author': "Som Mobilitat",
    'website': "http://www.sommobilitat.coop",

    'category': 'Mobility',
    'version': '12.0.0.0.8',

    'depends': [
        'base',
        'vertical_carsharing',
        'sm_partago_db',
        'sm_carsharing_structure',
        'sm_partago_usage',
        'sm_partago_user'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'email_tmpl/abouttoexpire_tariff_email.xml',
        'email_tmpl/notification_tariff_created.xml',
        'views/views.xml',
        'views/views_cron.xml',
        'views/views_tariff.xml',
        'views/views_carconfig_price_group.xml',
        'views/views_carconfig_tariff_group.xml',
        'views/views_tariffmodel_price_group.xml',
        'views/views_tariff_history.xml',
        'views/views_tariff_model.xml',
        'views/views_members.xml',
        'views/views_reservation_compute.xml',
        'views/views_cs_carconfig.xml',
        'views/views_res_config_settings.xml',
        'views/views_carsharing_user_request.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}
