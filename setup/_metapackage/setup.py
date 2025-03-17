import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-sale-prebook",
    description="Meta package for oca-sale-prebook Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-sale_stock_prebook>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
