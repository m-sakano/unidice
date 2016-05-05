# -*- mode: python -*-

block_cipher = None

data_files = [('tessdata/jpn.traineddata', 'tesseract/tessdata'),
              ('tessdata/eng.traineddata', 'tesseract/tessdata'),
              ('windowicon.ico', '.'),
              ('icon.ico', '.')]

bin_files = [ ('tesseract.exe', 'tesseract'),
              ('msvcrt/msvcp140.dll','.'),
              ('msvcrt/vcruntime140.dll','.')]

a = Analysis(['unidice.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\source'],
             binaries=bin_files,
             datas=data_files,
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
          name='unidice',
          debug=False,
          strip=False,
          upx=False,
          console=False,
          icon='icon.ico',
          version='version')
