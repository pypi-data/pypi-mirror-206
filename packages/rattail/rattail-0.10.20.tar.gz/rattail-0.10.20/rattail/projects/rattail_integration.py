# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2023 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Generator for 'rattail-integration' projects
"""

import os

import colander

from rattail.projects import PythonProjectGenerator


class RattailIntegrationProjectGenerator(PythonProjectGenerator):
    """
    Generator for projects which integrate Rattail with some other
    system.  This is for generating projects such as rattail-corepos
    and rattail-mailchimp etc.
    """
    key = 'rattail_integration'

    def make_schema(self, **kwargs):
        schema = super(RattailIntegrationProjectGenerator, self).make_schema(**kwargs)

        schema.add(colander.SchemaNode(name='integration_name',
                                       typ=colander.String()))

        schema.add(colander.SchemaNode(name='integration_url',
                                       typ=colander.String()))

        schema.add(colander.SchemaNode(name='extends_config',
                                       typ=colander.Boolean()))

        schema.add(colander.SchemaNode(name='extends_db',
                                       typ=colander.Boolean()))

        return schema

    def normalize_context(self, context):
        context = super(RattailIntegrationProjectGenerator, self).normalize_context(context)

        if not context.get('description'):
            context['description'] = "Rattail integration package for {}".format(
                context['integration_name'])

        context['classifiers'].update(set([
            'Topic :: Office/Business',
        ]))

        context['entry_points'].setdefault('rattail.config.extensions', []).extend([
            "{0} = {0}.config:{1}Config".format(context['pkg_name'], context['studly_prefix']),
        ])

        context['requires']['rattail'] = True

        if 'year' not in context:
            context['year'] = self.app.today().year

        return context

    def generate_project(self, output, context, **kwargs):
        super(RattailIntegrationProjectGenerator, self).generate_project(
            output, context, **kwargs)

        package = os.path.join(output, context['pkg_name'])

        ##############################
        # root package dir
        ##############################

        if context['extends_config']:
            self.generate('package/config.py.mako',
                          os.path.join(package, 'config.py'),
                          context)

        ##############################
        # db package dir
        ##############################

        if context['extends_db']:

            db = os.path.join(package, 'db')
            os.makedirs(db)

            self.generate('package/db/__init__.py',
                          os.path.join(db, '__init__.py'))

            ####################
            # model
            ####################

            model = os.path.join(db, 'model')
            os.makedirs(model)

            self.generate('package/db/model/__init__.py.mako',
                          os.path.join(model, '__init__.py'),
                          context)

            self.generate('package/db/model/customers.py.mako',
                          os.path.join(model, 'customers.py'),
                          context)

            ####################
            # alembic
            ####################

            alembic = os.path.join(db, 'alembic')
            os.makedirs(alembic)

            versions = os.path.join(alembic, 'versions')
            os.makedirs(versions)

            self.generate('package/db/alembic/versions/.keepme',
                          os.path.join(versions, '.keepme'))
