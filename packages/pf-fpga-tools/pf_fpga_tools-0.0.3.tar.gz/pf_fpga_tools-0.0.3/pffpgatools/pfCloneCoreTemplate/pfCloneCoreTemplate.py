# SPDX-FileCopyrightText: 2023-present Didier Malenfant
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import sys
import getopt
import zipfile
import tempfile
import shutil

from pffpgatools.__about__ import __version__
from pffpgatools.utils import Utils


# -- Classes
class pfCloneCoreTemplate:
    """A tool to clone the Github core template."""

    def __init__(self, args):
        """Constructor based on command line arguments."""

        try:
            self.branch_name = None

            # -- Gather the arguments
            opts, arguments = getopt.getopt(args, 'hvb:', ['help', 'version', 'branch='])

            for o, a in opts:
                if o in ('-h', '--help'):
                    pfCloneCoreTemplate.printUsage()
                    sys.exit(0)
                elif o in ('-v', '--version'):
                    pfCloneCoreTemplate.printVersion()
                    sys.exit(0)
                elif o in ('-b', '--branch'):
                    self.branch_name = a

            nb_of_arguments: int = len(arguments)
            if nb_of_arguments != 1:
                raise RuntimeError('Invalid arguments. Maybe start with `pfCloneCoreTemplate --help?')

            self.destination_folder: str = arguments[0]

        except getopt.GetoptError:
            print('Unknown option or argument. Maybe start with `pfCloneCoreTemplate --help?')
            sys.exit(0)

    def main(self) -> None:
        if Utils.commandExists('git') is False:
            raise RuntimeError('You must have git installed on your machine to continue.')

        repo_folder = os.path.join(self.destination_folder, 'pf-core-template')
        if os.path.exists(repo_folder):
            shutil.rmtree(repo_folder)

        print('Cloning core template in \'' + repo_folder + '\'.')

        command_line = ['git', 'clone', '--depth', '1']

        if self.branch_name is not None:
            command_line.append('--branch')
            command_line.append(self.branch_name)

        command_line.append('https://github.com/DidierMalenfant/pf-core-template.git')

        Utils.shellCommand(command_line, from_dir=self.destination_folder, silent_mode=True)

    @classmethod
    def printUsage(cls) -> None:
        pfCloneCoreTemplate.printVersion()
        print('')
        print('usage: pfCloneCoreTemplate <options> destination_folder')
        print('')
        print('The following options are supported:')
        print('')
        print('   --help/-h          - Show a help message.')
        print('   --version/-v       - Display the app\'s version.')
        print('')

    @classmethod
    def printVersion(cls) -> None:
        print('🛠️  pfCloneCoreTemplate v' + __version__ + ' 🛠️')


def main():
    try:
        # -- Remove the first argument (which is the script filename)
        build = pfCloneCoreTemplate(sys.argv[1:])

        if build is not None:
            build.main()
    except Exception as e:
        print(e)
        sys.exit(1)
    except KeyboardInterrupt:
        print('Execution interrupted by user.')
        sys.exit(1)


if __name__ == '__main__':
    main()
