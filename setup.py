from setuptools import setup

setup(
    name="mmte",
    packages=["mmte", "mmte.lib"],
    entry_points = {
        "console_scripts": [
            "mmte = mmte.__main__:main",
        ]
    }
)