"""
Setup file for event_bus_conductor Django plugin.
"""

from __future__ import print_function

from setuptools import setup

from utils import get_version, load_requirements


with open("README.rst", "r") as fh:
    README = fh.read()


VERSION = get_version('event_bus_conductor', '__init__.py')
APP_NAME = "event_bus_conductor = event_bus_conductor.apps:EventBusConductorPluginConfig"


setup(
    name='event-bus-conductor',
    version=VERSION,
    author='Raccoon Gang',
    author_email='contact@raccoongang.com',
    description='Event bus conductor',
    license='AGPL',
    long_description=README,
    long_description_content_type='text/x-rst',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
    packages=[
        'event_bus_conductor',
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    zip_safe=False,
    entry_points={
        "lms.djangoapp": [APP_NAME],
        "credentials.djangoapp": [APP_NAME],
    },
)