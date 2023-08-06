import sys
import os
import logging
import subprocess
import shutil
import tempfile
import platform
import urllib.request
import zipfile

_log = logging.getLogger( __name__ )

def download_djot(djot_version="^0.2", node_version='19.9.0'):
    _log.info( 'Downloading djot' )
    # make a temp directory
    _log.debug( 'Creating temp directory' )
    temp_dir = tempfile.mkdtemp()
    _log.debug( 'Created temp directory at: %s' % temp_dir )

    # download a portable version of node/npm to the node directory
    _download_node(node_version, temp_dir)

    # download djot
    _download_djot(djot_version, temp_dir)

def _download_node(node_version, node_dir):
    _log.info( 'Downloading a portable version of node and npm' )
    node_platform = ""
    node_extension = ""
    if platform.system() == "Windows":
        node_platform = "win"
        node_extension = "zip"
    elif platform.system() == "Darwin":
        if platform.processor() == "i386":
            node_platform = "darwin-x64"
        else:
            node_platform = "darwin-arm64"
        node_extension = "tar.gz"
    node_url = f'https://nodejs.org/dist/v{node_version}/node-v{node_version}-{node_platform}-x86.{node_extension}'
    # download the node zip file
    node_zip = os.path.join( node_dir, 'node.zip' )
    _log.debug( 'Downloading node from: %s' % node_url )
    _log.debug( 'Saving node to: %s' % node_zip )
    urllib.request.urlretrieve( node_url, node_zip )
    # unzip the node zip file
    _log.debug( 'Unzipping node' )
    with zipfile.ZipFile( node_zip, 'r' ) as zip_ref:
        zip_ref.extractall( node_dir )
    # rename the new node directory
    node_dir_name = 'node-v%s-win-x86' % node_version
    node_dir_new_name = 'node'
    node_dir_new = os.path.join( node_dir, node_dir_new_name )
    node_dir_old = os.path.join( node_dir, node_dir_name )
    _log.debug( 'Renaming node directory from: %s' % node_dir_old )
    _log.debug( 'Renaming node directory to: %s' % node_dir_new )
    os.rename( node_dir_old, node_dir_new )
        # delete the zip file
        # wait for it to not be in use
    _log.debug( 'Deleting node zip file' )
    os.remove( node_zip )
    _log.info( 'Downloaded node' )

def _download_djot(djot_version, temp_dir):
    global package_json
    _log.info( 'Downloading djot' )
    # make a dir besides our node dir for the djot files
    djot_dir = os.path.join(temp_dir, 'djot')
    _log.debug( 'Creating djot directory at: %s' % djot_dir )
    os.mkdir(djot_dir)
    # put our package_json variable in a file in the djot dir. Replace the version with the version we want
    package_json = package_json.replace("%DJOT_VERSION%", djot_version)
    package_json_path = os.path.join(djot_dir, 'package.json')
    _log.debug( 'Creating package.json at: %s' % package_json_path )
    with open(package_json_path, 'w') as f:
        f.write(package_json)
    # run npm install in the djot dir
    _log.info( 'Retrieving packages...' )
    # store current working idr
    cwd = os.getcwd()
    # switch to the djot dir
    os.chdir(djot_dir)
    # run npm install from ../node/npm  
    subprocess.run(['..\\node\\npm.cmd', 'install'])
    subprocess.run(['..\\node\\npm.cmd', 'install', '-g', 'pkg'])
    _log.info("All packages retrieved")
    # package
    _log.info( 'Packaging djot' )
    os.system("pkg -t latest -C gzip .")
    _log.info( 'Packaged djot' )
    
    # locate our package
    djot_executable = "djot"
    # if we are on windows, then add ".exe" to the end of the executable
    if platform.system() == "Windows":
        djot_executable += ".exe"
    # make our target folder
    target_folder = DEFAULT_TARGET_FOLDER[sys.platform]
    target_folder = os.path.expanduser(target_folder)
    _log.debug( 'Creating target folder at: %s' % target_folder )
    try:
        os.mkdir(target_folder)
    except FileExistsError:
        pass
    # move the executable to the target folder
    # if it already exists, delete it
    try:
        os.remove(os.path.join(target_folder, djot_executable))
    except FileNotFoundError:
        pass
    os.rename(djot_executable, os.path.join(target_folder, djot_executable))
    # make sure it's executable
    os.chmod(os.path.join(target_folder, djot_executable), 0o755)
    # switch back to our stored cwd
    os.chdir(cwd)
    # delete the temp dir
    _log.debug( 'Deleting temp directory at: %s' % temp_dir)
    _log.info( 'Deleting temp directory' )
    shutil.rmtree(temp_dir)
    _log.info( 'Downloaded djot' )

DEFAULT_TARGET_FOLDER = {
    "win32": "~\\AppData\\Local\\djot",
    "linux": "~/bin",
    "darwin": "~/Applications/djot"
}

package_json = """{
  "name": "djot",
  "version": "1.0.0",
  "description": "",
  "bin": "./node_modules/@djot/djot/lib/cli.js",
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@djot/djot": "%DJOT_VERSION%"
  }
}
"""