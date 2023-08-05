import os
import shutil
import subprocess

def download_nuget(version: str = "", update: bool = False) -> None:
    nuget_path = os.path.join(os.path.dirname(__file__), 'aacommpyDownloader-main', 'nuget.exe')
    installed = False
    for dirname in os.listdir(os.path.dirname(nuget_path)):
        if dirname.startswith('Agito.AAComm.') and os.path.isdir(os.path.join(os.path.dirname(nuget_path), dirname)):
            installed = True
            old_version = dirname.split('.')[2]
            break
    if update and installed:
        shutil.rmtree(os.path.join(os.path.dirname(nuget_path), f'Agito.AAComm.{old_version}'))
    nuget_cmd = [nuget_path, 'install', 'Agito.AAComm', '-OutputDirectory', os.path.join(os.path.dirname(nuget_path)), '-Source', 'https://api.nuget.org/v3/index.json']
    if version != "":
        nuget_cmd.extend(['-Version', version])
    subprocess.run(nuget_cmd, check=True)
    for dirname in os.listdir(os.path.dirname(nuget_path)):
        if dirname.startswith('Agito.AAComm.') and os.path.isdir(os.path.join(os.path.dirname(nuget_path), dirname)):
            new_version = dirname.split('.')[2]
            source_dir = os.path.join(os.path.dirname(nuget_path), f'Agito.AAComm.{new_version}/build/AACommServer')
            dest_dir = os.path.dirname(__file__)
            shutil.copy2(os.path.join(source_dir, 'AACommServer.exe'), dest_dir)
            shutil.copy2(os.path.join(source_dir, 'AACommServerAPI.dll'), dest_dir)
            break
    return None
def nuget_version() -> None:
    nuget_path = os.path.join(os.path.dirname(__file__), 'aacommpyDownloader-main', 'nuget.exe')
    nuget_cmd = [nuget_path, 'list', 'Agito.AAComm', '-AllVersions']
    result = subprocess.run(nuget_cmd, check=True, stdout=subprocess.PIPE, text=True)
    versions = []
    for line in result.stdout.splitlines():
        if 'Agito.AAComm ' in line:
            version = line.split(' ')[-1]
            versions.append(version)
    if len(versions) > 0:
        print(f'The installed versions of Agito.AAComm are: {", ".join(versions)}.')
    else:
        print('Agito.AAComm package is not installed.')
    return None
def update_nuget() -> None:
    download_nuget(update=True)
    return None
