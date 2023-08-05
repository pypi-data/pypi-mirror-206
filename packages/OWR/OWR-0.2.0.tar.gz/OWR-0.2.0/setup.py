from setuptools import setup

setup(
    name='OWR',
    version='0.2.0',
    description='Obscene word recognition package',
    url='https://github.com/VladVslv/OWR',
    author='Vlad Vasilev',
    author_email='vpvasilev.work@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=['owr'],
    install_requires=['json', 'os', 'sys',
                      'huggingsound',
                      'librosa'
                      'Levenshtein',
                      'soundfile',
                      'fonetika',
                      'numpy',
                      'playsound',
                      'pylcs',
                      'logging'],
)
