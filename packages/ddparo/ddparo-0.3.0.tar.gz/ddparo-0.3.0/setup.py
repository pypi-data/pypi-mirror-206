from setuptools import setup

setup(
    name='ddparo',
    version='0.3.0',
    py_modules=['ddparo'],
    install_requires=[
        'requests',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'ddparo = ddparo:main'
        ]
    }
)
