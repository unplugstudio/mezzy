import os
import subprocess
import atexit
import signal

from django.conf import settings

from mezzanine.core.management.commands.runserver import Command \
    as MezzanineRunserverCommand


class Command(MezzanineRunserverCommand):
    '''
    A custom implementation of runserver that also runs grunt.
    You must set ``settings.GRUNT_PATH`` to the absolute path of the Gruntfile.
    https://lincolnloop.com/blog/simplifying-your-django-frontend-tasks-grunt/
    '''

    def inner_run(self, *args, **options):
        self.start_grunt()
        return super(Command, self).inner_run(*args, **options)

    def start_grunt(self):
        self.stdout.write('>>> Starting grunt')
        self.grunt_process = subprocess.Popen(
            ['grunt', '--gruntfile', str(settings.GRUNT_PATH)],
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('>>> Grunt process on pid {0}'.format(self.grunt_process.pid))

        def kill_grunt_process(pid):
            self.stdout.write('>>> Closing grunt process')
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_grunt_process, self.grunt_process.pid)
