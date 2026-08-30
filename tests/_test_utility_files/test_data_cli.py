

from nimlotherion.config.args import _inst


def mockCLI(
    user=None,
    group=None,
    module=None,
    root_package='pdf_report',
    l_key=None,
    s_key=None,
    SISKUNDE='SIS',
):
    args = []
    if user:
        args += ['--user', user]
    if group:
        args += ['--group', group]
    if module:
        args += ['--module', module]
    if root_package:
        args += ['--root_package', root_package]

    _inst.parse(args)
