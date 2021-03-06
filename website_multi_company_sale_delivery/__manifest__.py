# Copyright 2018 Ildar Nasyrov <https://it-projects.info/team/iledarn>
# License MIT (https://opensource.org/licenses/MIT).
{
    "name": """Real Multi Website (eCommerce Delivery extension)""",
    "summary": """Configure Delivery Carriers list per website""",
    "category": "eCommerce",
    # "live_test_url": "http://apps.it-projects.info/shop/product/website-multi-company?version=11.0",
    "images": ["images/website_multi_company_sale_delivery_main.png"],
    "version": "13.0.1.0.2",
    "application": False,
    "author": "IT-Projects LLC, Ildar Nasyrov",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info/team/iledarn",
    "license": "Other OSI approved licence",  # MIT
    "price": 10.00,
    "currency": "EUR",
    "depends": ["website_sale_delivery", "ir_rule_website", "website_multi_company"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "security/website_multi_company_sale_delivery_security.xml",
        "security/ir.model.access.csv",
        "views/delivery_views.xml",
    ],
    "qweb": [],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": False,
}
