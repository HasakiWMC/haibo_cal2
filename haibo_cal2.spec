# -*- mode: python -*-

block_cipher = None


a = Analysis(['haibo_cal2'],
             pathex=['C:\\Users\\leon\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'E:\\python_project\\haibo_cal2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='haibo_cal2',
          debug=False,
          strip=False,
          upx=True,
          console=True )
