# -*- coding: utf-8 -*-
import sys
import os
from .lib.play_files import PlayFiles
from .lib.read_files import ReadFiles


class MmteSettings(object):
    """
    This class provides a basic method to set directory.

    """
    COMMAND_LINE_ARGS = ('--play-dir', '--read-dir')
    COMMAND_LINE_SERVICE = ('play', 'read', 'stop', 'show')

    def __init__(self):
        self._initialized = False
        self._dir_settings = {}
        self._service = []

    def _get_argument_from_cmd_line(self):
        for arg in sys.argv[1:]:
            if arg.split('=')[0] in self.COMMAND_LINE_ARGS:
                try:
                    key = arg.split('=')[0][2:6]
                    value = arg.split('=')[1]
                    self._dir_settings.update({
                        key: value
                    })
                except IndexError:
                    pass

            if arg in self.COMMAND_LINE_SERVICE:
                self._run_service(arg)

        return

    def _run_service(self, arg):
        if not self._dir_settings:
            # set to current directory
            # current_dir = os.path.dirname(os.path.abspath(__file__))
            self._dir_settings.update({
                '--play-dir': '/Users/nuko/Git/my_midterm_exam',
                '--read-dir': '/Users/nuko/Git/my_midterm_exam'
            })

        if arg == 'play':
            while True:
                for content in os.listdir("."):
                    if content.endswith('.mp3'):
                        path = self._dir_settings['--play-dir']+'/'+content
                        print(path)
                        PlayFiles.play(path)

        if arg == 'read':
                    ReadFiles.read()

    def _setup(self):
        if self._initialized:
            return

        if not self._dir_settings:
            raise RuntimeError('Directory settings are not configured')

        self._initialized = True

    def _manage_call(self, func, loop_count=1):
        for count in range(loop_count):
            func()
        return


settings = MmteSettings()