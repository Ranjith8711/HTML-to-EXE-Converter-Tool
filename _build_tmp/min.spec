# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules

hiddenimports = ['webview', 'webview.platforms.winforms']
hiddenimports += collect_submodules('webview')


a = Analysis(
    ['C:\\Users\\LENOVO\\Pictures\\new one\\_build_tmp\\_min_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\LENOVO\\Pictures\\new one\\_build_tmp\\min.html', '.')],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='min',
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
)
