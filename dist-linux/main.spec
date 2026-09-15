# -*- mode: python ; coding: utf-8 -*-

import importlib.metadata as importlib_metadata

from PyInstaller.utils.hooks import collect_data_files, copy_metadata

block_cipher = None


def _collect_all_dist_metadata():
    # Several packages in the dependency tree (imageio, bioimageio.*, ...) read
    # their own installed-package metadata (dist-info/METADATA) at import time
    # via importlib.metadata, e.g. to resolve __version__. PyInstaller's import
    # analysis only follows Python imports, so it never bundles that metadata
    # unless told to explicitly -- causing importlib.metadata.PackageNotFoundError
    # at runtime for whichever package happens to do this. Rather than chasing
    # these one at a time across build/run cycles, bundle the metadata for every
    # distribution installed in the build environment; it's a few KB each.
    collected = []
    seen = set()
    for dist in importlib_metadata.distributions():
        name = dist.metadata.get("Name")
        if not name or name in seen:
            continue
        seen.add(name)
        try:
            collected += copy_metadata(name)
        except Exception:
            pass
    return collected


datas = [('images', 'images')]
# bioimageio.spec / bioimageio.core read non-.py data files (VERSION, static/*.json)
# at import time via importlib.resources; PyInstaller's import analysis does not
# pick these up automatically, so they must be collected explicitly.
datas += collect_data_files('bioimageio.spec')
datas += collect_data_files('bioimageio.core')
datas += _collect_all_dist_metadata()

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BiaPy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images/biapy_logo_icon.ico']
)
