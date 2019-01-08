#
# AppEngine-Oil
#
# Copyright (C) 2017 Boris Raicheff
# All rights reserved
#


from setuptools import find_packages, setup


setup(
    name='AppEngine-Oil',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=(
        'click',
        'configobj',
        'oyaml',
    ),
    entry_points={
        'console_scripts': (
            'envinject = scripts.envinject:main',
        ),
    },
)


# EOF
