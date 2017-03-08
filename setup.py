from setuptools import setup

setup(
    name='gitflow-gitlab',
    version='0.1.0',
    description='Git Flow commands to be using with Git Lab API',
    url='http://github.com/rafaellott/gitflow-gitlab',
    author='Rafael Lott',
    author_email='me@rafaellott.eti.br',
    license='MIT',
    packages=['gfgl'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gfgl=gfgl.gfgl:gfgl
    ''',
    zip_safe=False
)
