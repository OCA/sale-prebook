import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-sale-prebook",
    description="Meta package for oca-sale-prebook Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-sale_stock_prebook',
        'odoo14-addon-sale_stock_prebook_stock_available_to_promise_release',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
