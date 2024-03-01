from setuptools import setup, find_packages

setup(
    name='cann_calculator',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'lilzey_generator==0.1.0',
        'tea_weather_app==0.1.3',
    ],
    entry_points={
        'console_scripts': [
            'cann-calculator=cann_calculator.main:run',
        ],
    },
    author='cann',
    author_email='savemefromthedark777@gmail.com',
    description='A calculator application by Cann',
    bugtrack_url='https://github.com/cann072000/cann_calculator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    project_urls={
        'Source': 'https://github.com/cann072000/cann_calculator',
    },
)
