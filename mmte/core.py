# -*- coding: utf-8 -*-
import sys


class MmteSettings(object):
    """
    This class provides a basic method to set directory.

    """
    COMMAND_LINE_ARGS = ('--play-dir', '--read-dir')
    COMMAND_LINE_SERVICE = ('play', 'read', 'stop', 'show')

    def __init__(self):
        self._initialized = False
        self._dir_settings = {}

        self._get_argument_from_cmd_line()
        # print(bool({}))

    def _get_argument_from_cmd_line(self):
        for arg in sys.argv[1:]:
            for lib_arg in self.COMMAND_LINE_ARGS:
                if arg.startswith(lib_arg):
                    try:
                        self._dir_settings.update({
                            arg.split('=')[0]: arg.split('=')[1]
                        })
                    except IndexError:
                        pass
        return

    def _setup(self):
        if self._initialized:
            return

        if not self._dir_settings:
            raise RuntimeError('Directory settings are not configured')

        self._initialized = True

settings = MmteSettings()