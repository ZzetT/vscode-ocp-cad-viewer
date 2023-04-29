from setuptools import setup, find_packages

setup_args = {
    "name": "ocp_vscode",
    "version": "0.93.0",
    "description": "OCP CAD Viewer for VSCode",
    "long_description": "An extension to show OCP cad CAD objects (CadQuery, build123d) in VS Code via pythreejs",
    "include_package_data": True,
    "python_requires": ">=3.9",
    "install_requires": ["ocp-tessellate>=1.0.2", "requests", "orjson"],
    "packages": find_packages(),
    "zip_safe": False,
    "author": "Bernhard Walter",
    "author_email": "b_walter@arcor.de",
    "url": "https://github.com/bernhard-42/vscode-ocp-cad-viewer",
    "keywords": ["vscode", "widgets", "CAD", "cadquery"],
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Framework :: IPython",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
}

setup(**setup_args)
