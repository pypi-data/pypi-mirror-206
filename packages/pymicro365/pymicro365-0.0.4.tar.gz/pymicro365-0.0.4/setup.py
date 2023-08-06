from setuptools import setup

setup(
    name="pymicro365",
    version="0.0.4",
    author="Informatic365",
    author_email="chen.runkang1@gmail.com",
    description="This is a module to simplify closing the PC",
    long_description="This is a module to simplify functions of the MicroSoftware",
    url="https://sites.google.com/view/infocommunity365/projects/pymicro365",
    packages=["pymicro365"],
    python_requires=">=3.10",
    install_requires=[
        "customtkinter>=5.1.2"
    ],
)