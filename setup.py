from setuptools import setup, find_packages

setup(
    name="kanye-quotes-app",
    version="0.1.0",
    author="Demk662",
    author_email="rodrigueloredon@gmail.com",
    description="Une simple application Tkinter qui affiche des lyrics de Kanye West.",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "requests",
        "Pillow",
    ],
    entry_points={
        'gui_scripts': [
            'kanye-quotes-app = main:main',  # Adjust this if your main function is named differently
        ],
    },
)