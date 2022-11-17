# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['view.py'],
    pathex=['file.py', 'parallel.py', 'utils.py'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'eventlet.hubs.epolls', 
        'eventlet.hubs.kqueue', 
        'eventlet.hubs.selects',
        'dns.asyncbackend',
        'dns.asyncquery',
        'dns.asyncresolver',
        'dns.versioned',
        'dns.dnssec',
        'dns.e164',
        'dns.edns',
        'dns.entropy',
        'dns.exception',
        'dns.flags',
        'dns.grange',
        'dns.hash',
        'dns.inet',
        'dns.ipv4',
        'dns.ipv6',
        'dns.message',
        'dns.name',
        'dns.namedict',
        'dns.node',
        'dns.opcode',
        'dns.query',
        'dns.rcode',
        'dns.rdata',
        'dns.rdataclass',
        'dns.rdataset',
        'dns.rdatatype',
        'dns.renderer',
        'dns.resolver',
        'dns.reversename',
        'dns.rrset',
        'dns.set',
        'dns.tokenizer',
        'dns.tsig',
        'dns.tsigkeyring',
        'dns.ttl',
        'dns.update',
        'dns.version',
        'dns.wiredata',
        'dns.zone'
    ],
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
    name='view',
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
