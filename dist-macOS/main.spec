# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

datas = [('images', 'images')]
# bioimageio.spec / bioimageio.core read non-.py data files (VERSION, static/*.json)
# at import time via importlib.resources; PyInstaller's import analysis does not
# pick these up automatically, so they must be collected explicitly.
datas += collect_data_files('bioimageio.spec')
datas += collect_data_files('bioimageio.core')

a = Analysis(
    ['main.py'],
    pathex=['/Users/cc-staff/Documents/Dani/BiaPy-GUI'],
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
    [],
    exclude_binaries=True,
    name='BiaPy_bin',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="images/biapy_logo_icon.ico",
)
coll = COLLECT(exe,
   a.binaries,
   a.zipfiles,
   a.datas,
   strip=False,
   upx=False,
   upx_exclude=[],
   name='BiaPy')

app = BUNDLE(
    coll,
    name='BiaPy.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'NSHighResolutionCapable': 'True'},
    icon="images/biapy_logo_icon.ico",
    bundle_identifier=None,
)
