from setuptools import setup

setup(
    name="CatRoyale",
    version="1.18",
    description="A cat themed battle royale game",
    author="Tarsoly Barnabás",
    author_email="tarsoly.barnabas2002@gmail.com",
    url="https://github.com/Iseroo/Python-kotprog",
    packages=["cat_royale"],
    install_requires=["pygame", "webcolors", "pillow", "ordered_set"],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'CatRoyale = cat_royale.main:main_func'
        ]
    },

)
