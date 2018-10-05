from setuptools import setup, find_packages, glob

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_all_files(dirname):
    return dirname, glob.glob(dirname + '/**/*.*', True)


setup(
    name='Dalton',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/mariohm1311/Dalton',
    license='GPLv3',
    author='mariohm1311',
    author_email='',
    description='Molecular Dynamics and Conformational Analysis using Metropolis Monte Carlo in Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn',
        'seaborn',
        'matplotlib'
    ],
    data_files=[get_all_files(x) for x in ['geom', 'input', 'output', 'plot']],
    package_data={
        '.': ['./*.py']
    }
)
