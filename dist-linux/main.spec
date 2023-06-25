# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
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
a.datas +=[('images/semantic_seg.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/semantic_seg.png', 'images')]
a.datas +=[('images/instance_seg.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/instance_seg.png', 'images')]
a.datas +=[('images/detection.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/detection.png', 'images')]
a.datas +=[('images/denoising.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/denoising.png', 'images')]
a.datas +=[('images/ssl.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/ssl.png', 'images')]
a.datas +=[('images/sr.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/sr.png', 'images')]
a.datas +=[('images/classification.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/classification.png', 'images')]
a.datas +=[('images/semantic_seg_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/semantic_seg_selected.png', 'images')]
a.datas +=[('images/instance_seg_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/instance_seg_selected.png', 'images')]
a.datas +=[('images/detection_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/detection_selected.png', 'images')]
a.datas +=[('images/denoising_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/denoising_selected.png', 'images')]
a.datas +=[('images/ssl_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/ssl_selected.png', 'images')]
a.datas +=[('images/sr_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/sr_selected.png', 'images')]
a.datas +=[('images/classification_selected.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/classification_selected.png', 'images')]
a.datas +=[('images/superminimal_ark_biapy2.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/superminimal_ark_biapy2.png', 'images')]
a.datas +=[('images/horizontal-logo-monochromatic-white.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/horizontal-logo-monochromatic-white.png', 'images')]
a.datas +=[('images/bn_images/back.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/back.png', 'images/bn_images')]
a.datas +=[('images/bn_images/closeAsset 43.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/closeAsset 43.png', 'images/bn_images')]
a.datas +=[('images/bn_images/error.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/error.png', 'images/bn_images')]
a.datas +=[('images/bn_images/goptions.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/goptions.png', 'images/bn_images')]
a.datas +=[('images/bn_images/hideAsset 53.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/hideAsset 53.png', 'images/bn_images')]
a.datas +=[('images/bn_images/home.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/home.png', 'images/bn_images')]
a.datas +=[('images/bn_images/info.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/info.png', 'images/bn_images')]
a.datas +=[('images/bn_images/max.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/max.png', 'images/bn_images')]
a.datas +=[('images/bn_images/restore.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/restore.png', 'images/bn_images')]
a.datas +=[('images/bn_images/run.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/run.png', 'images/bn_images')]
a.datas +=[('images/bn_images/test.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/test.png', 'images/bn_images')]
a.datas +=[('images/bn_images/train.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/train.png', 'images/bn_images')]
a.datas +=[('images/bn_images/error.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/error.png', 'images/bn_images')]
a.datas +=[('images/bn_images/workflow.png', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/workflow.png', 'images/bn_images')]
a.datas +=[('images/bn_images/dot_disable.svg', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/dot_disable.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/dot_enable.svg', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/dot_enable.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/down_arrow.svg', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/down_arrow.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/left_arrow.svg', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/left_arrow.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/right_arrow.svg', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/right_arrow.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/up_arrow.svg', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/bn_images/up_arrow.svg', 'images/bn_images')]
a.datas +=[('images/biapy_logo_icon.ico', '/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/biapy_logo_icon.ico', 'images')]

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
    icon=['/home/dfranco/Documents/0.thesis/BiaPy-GUI/images/biapy_logo_icon.ico']
)
