from setuptools import setup  # type: ignore

long_description = '''
# UP_PPS

UP_PPS is an engine that relies on CP-Sat of ORTOOLS
to solve scheduling problems
'''

setup(name='up_pps',
      version='1.0.3',
      description='up_pps',
      author='ACTOR',
      author_email='ahead@ahead-research.com',
      url='https://github.com/aiplan4eu/up-pps',
      packages=['up_pps', 'up_pps.dataenv', 'up_pps.dataenv.internal', 'up_pps.core','up_pps.core.output', 'up_pps.manager'],
      install_requires=['pip==22.3.1', 'numpy==1.24.1', 'ortools==9.5.2237'],
      python_requires='>=3.7',
      license='APACHE'
      )
