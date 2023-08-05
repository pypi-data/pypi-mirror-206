# core dependencies
import time
from abba_python import enable_python_hooks, get_java_dependencies, add_brainglobe_atlases
# in order to wait for a jvm shutdown
import jpype
import imagej

import os


if __name__ == '__main__':

    # MAC ISSUE
    # https: // github.com / imagej / pyimagej / issues / 23
    # -- FOR DEBUGGING
    # import imagej.doctor
    # imagej.doctor.checkup()
    # imagej.doctor.debug_to_stderr()
    # -- Atlas
    # Any brainglobe atlas can be used
    # show_atlases()
    # abba_python = Abba("azba_zfish_4um", slicing_mode='sagittal', headless=True)  # or any other brainglobe atlas

    # -- HEADLESS
    # abba_python = Abba('Adult Mouse Brain - Allen Brain Atlas V3', headless=True)  # or any other brainglobe atlas
    # --

    # -- NOT HEADLESS
    # abba = Abba('Adult Mouse Brain - Allen Brain Atlas V3')
    # abba.show_bdv_ui()  # creates and show a bdv view
    ij = imagej.init(get_java_dependencies(), mode="interactive")
    ij.ui().showUI()
    enable_python_hooks(ij)
    add_brainglobe_atlases(ij)

    from scyjava import jimport
    from jpype.types import JString

    # loci.common.DebugTools.enableLogging("OFF");
    DebugTools = jimport('loci.common.DebugTools')
    # DebugTools.enableLogging('OFF')
    DebugTools.enableLogging("INFO");
    # DebugTools.enableLogging("DEBUG");

    import platform
    if platform.system() == 'Windows':
        File = jimport('java.io.File')
        # Now let's set the atlas folder location in a folder with all users access

        AtlasLocationHelper = jimport('ch.epfl.biop.atlas.AtlasLocationHelper')
        directory = os.path.join(os.environ['ProgramData'], 'abba-atlas')

        # create the directory with write access for all users
        try:
            print('Attempt to set ABBA Atlas cache directory to ' + directory)
            os.makedirs(directory, exist_ok=True)
            atlasPath = str(directory)
            AtlasLocationHelper.defaultCacheDir = File(JString(atlasPath))
            print('ABBA Atlas cache directory set to ' + directory)
        except OSError:
            print('ERROR! Could not set ABBA Atlas cache dir')
            # directory already exists ?
            pass
    else:
        print('ERROR! '+platform.system()+' OS not supported yet.')

    # --

    # Wait for the JVM to shut down
    while jpype.isJVMStarted():
        time.sleep(1)

    print("JVM has shut down")
