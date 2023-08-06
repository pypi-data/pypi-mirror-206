# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastel',
 'fastel.ads',
 'fastel.ads.facebook',
 'fastel.auth',
 'fastel.cart',
 'fastel.jwt',
 'fastel.logistics',
 'fastel.logistics.common',
 'fastel.logistics.common.models',
 'fastel.logistics.ecpay',
 'fastel.logistics.ecpay.models',
 'fastel.logistics.sf',
 'fastel.logistics.sf.models',
 'fastel.logistics.tcat',
 'fastel.logistics.trackingmore',
 'fastel.notif',
 'fastel.payment',
 'fastel.payment.common',
 'fastel.payment.common.models',
 'fastel.payment.ecpay',
 'fastel.payment.ecpay.models',
 'fastel.payment.linepay',
 'fastel.payment.linepay.models',
 'fastel.payment.neweb',
 'fastel.payment.neweb.models',
 'fastel.social',
 'fastel.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.2.0,<3.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'boto3>=1.18.56,<2.0.0',
 'cryptography>=35.0.0,<36.0.0',
 'facebook-business>=12.0.1,<13.0.0',
 'fastapi>=0.63.0',
 'google-auth-oauthlib>=0.4.4,<0.5.0',
 'google-auth>=1.32.0,<2.0.0',
 'mongoengine>=0.23.1,<0.24.0',
 'pycrypto>=2.6.1,<3.0.0',
 'pydantic[email]>=1.8.2,<2.0.0',
 'pymongo>=3.12.0,<4.0.0',
 'pytz>=2022.1,<2023.0']

setup_kwargs = {
    'name': 'fastel',
    'version': '2.7.26',
    'description': 'RevtelTech Backend SDK',
    'long_description': None,
    'author': 'Chien',
    'author_email': 'a0186163@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
