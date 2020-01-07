# Copyright 2020 BlueCat Networks. All rights reserved.

# Various Flask framework items.
import os
import sys
import codecs

from flask import url_for, redirect, render_template, flash, g

from bluecat import route, util
import config.default_config as config
from main_app import app
from .cmdb_routers_form import GenericFormTemplate

def module_path():
    encoding = sys.getfilesystemencoding()
    return os.path.dirname(os.path.abspath(__file__))


# The workflow name must be the first part of any endpoints defined in this file.
# If you break this rule, you will trip up on other people's endpoint names and
# chaos will ensue.
@route(app, '/cmdb_routers/cmdb_routers_endpoint')
@util.workflow_permission_required('cmdb_routers_page')
@util.exception_catcher
def cmdb_routers_cmdb_routers_page():
    form = GenericFormTemplate()

    return render_template(
        'cmdb_routers_page.html',
        form=form,
        text=util.get_text(module_path(), config.language),
        options=g.user.get_options(),
    )

@route(app, '/cmdb_routers/form', methods=['POST'])
@util.workflow_permission_required('cmdb_routers_page')
@util.exception_catcher
def cmdb_routers_cmdb_routers_page_form():
    form = GenericFormTemplate()

    if form.validate_on_submit():
        g.user.logger.info('SUCCESS')
        flash('success', 'succeed')
        return redirect(url_for('cmdb_routerscmdb_routers_cmdb_routers_page'))
    else:
        g.user.logger.info('Form data was not valid.')
        return render_template(
            'cmdb_routers_page.html',
            form=form,
            text=util.get_text(module_path(), config.language),
            options=g.user.get_options(),
        )
