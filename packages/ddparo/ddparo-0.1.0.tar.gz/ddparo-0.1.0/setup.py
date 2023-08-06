from setuptools import setup

setup(
    name='ddparo',
    version='0.1.0',
    py_modules=['paro'],
    install_requires=[
        'requests',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'ddparo = paro:main'
        ]
    }
)
