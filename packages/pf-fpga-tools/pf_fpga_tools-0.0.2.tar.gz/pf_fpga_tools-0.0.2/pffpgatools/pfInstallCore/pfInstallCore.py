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
class pfInstallCore:
    """A tool to install a zipped up core file onto a given volume (SD card or Pocket in USB access mode)."""

    def __init__(self, args):
        """Constructor based on command line arguments."""

        try:
            # -- Gather the arguments
            opts, arguments = getopt.getopt(args, 'hv', ['help', 'version'])

            for o, a in opts:
                if o in ('-h', '--help'):
                    pfInstallCore.printUsage()
                    sys.exit(0)
                elif o in ('-v', '--version'):
                    pfInstallCore.printVersion()
                    sys.exit(0)

            nb_of_arguments: int = len(arguments)
            if nb_of_arguments != 2:
                raise RuntimeError('Invalid arguments.Maybe start with `pfInstallCore --help?')

            self.zip_filename: str = arguments[0]
            self.install_volume_name: str = arguments[1]

            components = os.path.splitext(self.zip_filename)
            if len(components) != 2 or components[1] != '.zip':
                raise RuntimeError('Can only install zipped up core files.')

            if not os.path.exists(self.zip_filename):
                raise RuntimeError('File \'' + self.zip_filename + '\' does not exist.')

        except getopt.GetoptError:
            print('Unknown option or argument. Maybe start with `pfInstallCore --help?')
            sys.exit(0)

    def main(self) -> None:
        # -- In a temporary folder.
        with tempfile.TemporaryDirectory() as tmp_dir:
            # -- Unzip the file.
            with zipfile.ZipFile(self.zip_filename, 'r') as zip_ref:
                zip_ref.extractall(tmp_dir)

            print('Copying core files...')

            # -- Copy Cores/ProjectFreedom.pfx1/* to Volume/Cores/ProjectFreedom.pfx1
            core_src_folder = os.path.join(tmp_dir, 'Cores', 'ProjectFreedom.pfx1')
            if not os.path.isdir(core_src_folder):
                raise RuntimeError('Cannot find \'' + core_src_folder + '\' in the core release zip file.')

            core_dest_folder = os.path.join(self.install_volume_name, 'Cores', 'ProjectFreedom.pfx1')
            os.makedirs(core_dest_folder, exist_ok=True)
            for file in os.listdir(core_src_folder):
                shutil.copy(os.path.join(core_src_folder, file), core_dest_folder)

            print('Copying platforms files...')

            # -- Copy Platforms/pfx1.json to Volume/Platforms/pfx1.json
            platforms_src_folder = os.path.join(tmp_dir, 'Platforms')
            if not os.path.isdir(platforms_src_folder):
                raise RuntimeError('Cannot find \'' + platforms_src_folder + '\' in the core release zip file.')

            platforms_dest_folder = os.path.join(self.install_volume_name, 'Platforms')
            os.makedirs(platforms_dest_folder, exist_ok=True)
            shutil.copy(os.path.join(platforms_src_folder, 'pfx1.json'), platforms_dest_folder)

            # -- Copy Platforms/_images/pfx1.bin to Volume/Platforms/_images/pfx1.bin
            platforms_src_folder = os.path.join(tmp_dir, 'Platforms', '_images')
            if not os.path.isdir(platforms_src_folder):
                raise RuntimeError('Cannot find \'' + platforms_src_folder + '\' in the core release zip file.')

            platforms_dest_folder = os.path.join(self.install_volume_name, 'Platforms', '_images')
            os.makedirs(platforms_dest_folder, exist_ok=True)
            shutil.copy(os.path.join(platforms_src_folder, 'pfx1.bin'), platforms_dest_folder)

        print('Ejecting \'' + self.install_volume_name + '\'.')
        Utils.shellCommand(['diskutil', 'eject', self.install_volume_name])

    @classmethod
    def printUsage(cls) -> None:
        pfInstallCore.printVersion()
        print('')
        print('usage: pfInstallCore <options> zip_file dest_volume')
        print('')
        print('The following options are supported:')
        print('')
        print('   --help/-h          - Show a help message.')
        print('   --version/-v       - Display the app\'s version.')
        print('')

    @classmethod
    def printVersion(cls) -> None:
        print('🛠️  pfInstallCore v' + __version__ + ' 🛠️')


def main():
    try:
        # -- Remove the first argument (which is the script filename)
        build = pfInstallCore(sys.argv[1:])

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
