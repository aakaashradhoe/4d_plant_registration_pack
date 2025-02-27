from setuptools import setup, find_packages

setup(
    name='plant_registration',
    version='0.1.0',
    description='4d Registration of Plant Skeletons',
    author='Giovanni Franzese',
    author_email='g.franzese@tudelft.nl',
    packages=find_packages(),
    install_requires=[],
    # Add other dependencies here
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)