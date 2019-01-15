#
# Flask-AppEngine
#
# Copyright (C) 2019 Boris Raicheff
# All rights reserved
#


import os

import click
import configobj
import oyaml


@click.command()
@click.argument('source', nargs=-1, type=click.File('r'))
@click.argument('target', type=click.Path(exists=True))
@click.option('-e', 'env_filename', type=click.Path(exists=True))
def main(source, target, env_filename):
    """"""

    config = configobj.ConfigObj(env_filename).dict()

    for src in source:
        descriptor = oyaml.load(src)
        env_variables = descriptor.get('env_variables') or {}
        env_variables.update(config)
        descriptor['env_variables'] = env_variables
        with open(os.path.join(target, os.path.basename(src.name)), 'w') as stream:
            oyaml.dump(descriptor, stream, default_flow_style=False)


# EOF
