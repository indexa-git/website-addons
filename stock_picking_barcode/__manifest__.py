# Copyright 2016-2017 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2016 Pavel Romanchenko
# Copyright 2017 Artyom Losev
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": "Barcode scanner support for Stock Picking",
    "summary": """The module allows you to process Pickings by barcode scanner via special page /barcode/web (the same as it was in odoo 8.0)""",
    "category": "Warehouse",
    "images": ["images/stock_picking_barcode_main.png"],
    "version": "13.0.1.1.1",
    "author": "IT-Projects LLC, Kolushov Alexandr",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info/team/KolushovAlexandr",
    "license": "Other OSI approved licence",  # MIT
    "price": 89.00,
    "currency": "EUR",
    "depends": ["stock", "web_editor", "website"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/package_report.xml",
        "views/stock.xml",
        "views/stock_view.xml",
        "views/stock_dashboard.xml",
    ],
    "qweb": ["static/src/xml/picking.xml"],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": False,
    "auto_install": False,
}
