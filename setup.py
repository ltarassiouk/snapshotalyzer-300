from setuptools import setup

setup(
    name='snapshotalyzer-300',
    version='0.1',
    author="Luba",
    author_email="luba@acloud.guru",
    description="SnapshotAlyzer 30000 is a tool to manage AWS EC2 snapshots, instanses,  or volumes",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/ltarassiouk/snapshotalyzer-300",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
