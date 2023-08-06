from setuptools import setup, find_packages

setup(
    name='ddparo',
    version='0.5.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'ddparo=ddparo.ddparo:main'
        ]
    }
)
