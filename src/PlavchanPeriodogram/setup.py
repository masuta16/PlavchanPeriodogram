from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='PlavchanPeriodogram',
    version='0.0.1',
    url='https://github.com/masuta16/PlavchanPeriodogram',
    license='MIT License',
    author='Israel Andrade',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='israndade16@hotmail.com',
    keywords='Plavchan Periodgram',
    description=u'It can calculate Plavchan Periodgram',
    packages=['PlavchanPeriodgram'],
    install_requires=['numpy','pandas','datetime','lightkurve','matplotlib'],)