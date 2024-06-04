from setuptools import Extension, setup

setup_args = dict(
    ext_modules=[
        Extension(
            name="cvarint",
            sources=["src/cvarintmodule.c"],
            include_dirs=['src']
        ),
    ]
)

setup(**setup_args)