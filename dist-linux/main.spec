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
a.datas +=[('images/semantic_seg.png', '/data/dfranco/BiaPy-GUI/images/semantic_seg.png', 'images')]
a.datas +=[('images/instance_seg.png', '/data/dfranco/BiaPy-GUI/images/instance_seg.png', 'images')]
a.datas +=[('images/detection.png', '/data/dfranco/BiaPy-GUI/images/detection.png', 'images')]
a.datas +=[('images/denoising.png', '/data/dfranco/BiaPy-GUI/images/denoising.png', 'images')]
a.datas +=[('images/ssl.png', '/data/dfranco/BiaPy-GUI/images/ssl.png', 'images')]
a.datas +=[('images/sr.png', '/data/dfranco/BiaPy-GUI/images/sr.png', 'images')]
a.datas +=[('images/classification.png', '/data/dfranco/BiaPy-GUI/images/classification.png', 'images')]
a.datas +=[('images/semantic_seg_selected.png', '/data/dfranco/BiaPy-GUI/images/semantic_seg_selected.png', 'images')]
a.datas +=[('images/instance_seg_selected.png', '/data/dfranco/BiaPy-GUI/images/instance_seg_selected.png', 'images')]
a.datas +=[('images/detection_selected.png', '/data/dfranco/BiaPy-GUI/images/detection_selected.png', 'images')]
a.datas +=[('images/denoising_selected.png', '/data/dfranco/BiaPy-GUI/images/denoising_selected.png', 'images')]
a.datas +=[('images/ssl_selected.png', '/data/dfranco/BiaPy-GUI/images/ssl_selected.png', 'images')]
a.datas +=[('images/sr_selected.png', '/data/dfranco/BiaPy-GUI/images/sr_selected.png', 'images')]
a.datas +=[('images/classification_selected.png', '/data/dfranco/BiaPy-GUI/images/classification_selected.png', 'images')]
a.datas +=[('images/superminimal_ark_biapy2.png', '/data/dfranco/BiaPy-GUI/images/superminimal_ark_biapy2.png', 'images')]
a.datas +=[('images/docker_logo.png', '/data/dfranco/BiaPy-GUI/images/docker_logo.png', 'images')]
a.datas +=[('images/classification_label.png', '/data/dfranco/BiaPy-GUI/images/classification_label.png', 'images')]
a.datas +=[('images/classification_raw.png', '/data/dfranco/BiaPy-GUI/images/classification_raw.png', 'images')]
a.datas +=[('images/denoising_raw.png', '/data/dfranco/BiaPy-GUI/images/denoising_raw.png', 'images')]
a.datas +=[('images/denoising_pred.png', '/data/dfranco/BiaPy-GUI/images/denoising_pred.png', 'images')]
a.datas +=[('images/detection_csv_input.png', '/data/dfranco/BiaPy-GUI/images/detection_csv_input.png', 'images')]
a.datas +=[('images/detection_label.png', '/data/dfranco/BiaPy-GUI/images/detection_label.png', 'images')]
a.datas +=[('images/detection_raw.png', '/data/dfranco/BiaPy-GUI/images/detection_raw.png', 'images')]
a.datas +=[('images/instance_seg_label.png', '/data/dfranco/BiaPy-GUI/images/instance_seg_label.png', 'images')]
a.datas +=[('images/instance_seg_raw.png', '/data/dfranco/BiaPy-GUI/images/instance_seg_raw.png', 'images')]
a.datas +=[('images/semantic_seg_raw.png', '/data/dfranco/BiaPy-GUI/images/semantic_seg_raw.png', 'images')]
a.datas +=[('images/semantic_seg_label.png', '/data/dfranco/BiaPy-GUI/images/semantic_seg_label.png', 'images')]
a.datas +=[('images/sr_pred.png', '/data/dfranco/BiaPy-GUI/images/sr_pred.png', 'images')]
a.datas +=[('images/sr_raw.png', '/data/dfranco/BiaPy-GUI/images/sr_raw.png', 'images')]
a.datas +=[('images/ssl_raw.png', '/data/dfranco/BiaPy-GUI/images/ssl_raw.png', 'images')]
a.datas +=[('images/ssl_pred.png', '/data/dfranco/BiaPy-GUI/images/ssl_pred.png', 'images')]

a.datas +=[('images/bn_images/back.png', '/data/dfranco/BiaPy-GUI/images/bn_images/back.png', 'images/bn_images')]
a.datas +=[('images/bn_images/closeAsset 43.png', '/data/dfranco/BiaPy-GUI/images/bn_images/closeAsset 43.png', 'images/bn_images')]
a.datas +=[('images/bn_images/error.png', '/data/dfranco/BiaPy-GUI/images/bn_images/error.png', 'images/bn_images')]
a.datas +=[('images/bn_images/goptions.png', '/data/dfranco/BiaPy-GUI/images/bn_images/goptions.png', 'images/bn_images')]
a.datas +=[('images/bn_images/hideAsset 53.png', '/data/dfranco/BiaPy-GUI/images/bn_images/hideAsset 53.png', 'images/bn_images')]
a.datas +=[('images/bn_images/home.png', '/data/dfranco/BiaPy-GUI/images/bn_images/home.png', 'images/bn_images')]
a.datas +=[('images/bn_images/info.png', '/data/dfranco/BiaPy-GUI/images/bn_images/info.png', 'images/bn_images')]
a.datas +=[('images/bn_images/max.png', '/data/dfranco/BiaPy-GUI/images/bn_images/max.png', 'images/bn_images')]
a.datas +=[('images/bn_images/restore.png', '/data/dfranco/BiaPy-GUI/images/bn_images/restore.png', 'images/bn_images')]
a.datas +=[('images/bn_images/run.png', '/data/dfranco/BiaPy-GUI/images/bn_images/run.png', 'images/bn_images')]
a.datas +=[('images/bn_images/test.png', '/data/dfranco/BiaPy-GUI/images/bn_images/test.png', 'images/bn_images')]
a.datas +=[('images/bn_images/train.png', '/data/dfranco/BiaPy-GUI/images/bn_images/train.png', 'images/bn_images')]
a.datas +=[('images/bn_images/error.png', '/data/dfranco/BiaPy-GUI/images/bn_images/error.png', 'images/bn_images')]
a.datas +=[('images/bn_images/workflow.png', '/data/dfranco/BiaPy-GUI/images/bn_images/workflow.png', 'images/bn_images')]
a.datas +=[('images/bn_images/dot_disable.svg', '/data/dfranco/BiaPy-GUI/images/bn_images/dot_disable.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/dot_enable.svg', '/data/dfranco/BiaPy-GUI/images/bn_images/dot_enable.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/down_arrow.svg', '/data/dfranco/BiaPy-GUI/images/bn_images/down_arrow.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/left_arrow.svg', '/data/dfranco/BiaPy-GUI/images/bn_images/left_arrow.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/right_arrow.svg', '/data/dfranco/BiaPy-GUI/images/bn_images/right_arrow.svg', 'images/bn_images')]
a.datas +=[('images/bn_images/up_arrow.svg', '/data/dfranco/BiaPy-GUI/images/bn_images/up_arrow.svg', 'images/bn_images')]
a.datas +=[('images/biapy_logo_icon.ico', '/data/dfranco/BiaPy-GUI/images/biapy_logo_icon.ico', 'images')]

a.datas +=[('images/detection_raw.png', '/data/dfranco/BiaPy-GUI/images/detection_raw.png', 'images')]

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
    icon=['/data/dfranco/BiaPy-GUI/images/biapy_logo_icon.ico']
)
