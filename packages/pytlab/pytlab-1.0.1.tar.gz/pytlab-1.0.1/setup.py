from setuptools import setup

setup(
    name='pytlab',
    version='1.0.1',
    description='Make matrix and array mathematics operations easier in python',
    author='Ghellab Abderrahmane (Rhaym)',
    author_email='ghellab.abderrahmane@univ-boumerdes.dz',
    packages=['pytlab'],
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
    ]
)
