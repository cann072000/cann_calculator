from setuptools import setup, find_packages

setup(
    name='cann_calculator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.19.5',
    ],
    entry_points={
        'console_scripts': [
            'cann-calculator=cann_calculator.main:run',
        ],
    },
    author='cann',
    author_email='savemefromthedark777@gmail.com',
    description='A calculator application by Cann',
    url='https://github.com/cann072000/cann_calculator',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/cann072000/cann_calculator',
    },
)
