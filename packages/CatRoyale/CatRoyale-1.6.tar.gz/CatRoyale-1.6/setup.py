from setuptools import setup

setup(
    name="CatRoyale",
    version="1.6",
    description="A cat themed battle royale game",
    author="Tarsoly Barnabás",
    author_email="tarsoly.barnabas2002@gmail.com",
    url="https://github.com/Iseroo/Python-kotprog",
    packages=["classes", "assets"],
    py_modules=["main"],
    install_requires=["pygame", "webcolors", "PIL", "ordered_set"],
    include_package_data=True,
)
