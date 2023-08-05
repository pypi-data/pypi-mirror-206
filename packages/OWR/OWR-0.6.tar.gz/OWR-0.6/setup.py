from setuptools import setup, find_packages
setup(
    name='OWR',
    version='0.6',
    description='Obscene word recognition package',
    url='https://github.com/VladVslv/OWR',
    author='Vlad Vasilev',
    author_email='vpvasilev.work@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=['OWR'],
    install_requires=['huggingsound',
                      'librosa',
                      'Levenshtein',
                      'soundfile',
                      'fonetika',
                      'numpy',
                      'playsound',
                      'pylcs'],
)
