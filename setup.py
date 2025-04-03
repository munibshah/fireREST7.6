from setuptools import setup, find_packages

setup(
    name="firerest76",  # New package name
    version="1.2.5",  # Keep the same version or update as necessary
    description="Python API client for Cisco Firepower Management Center (FMC)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",  # Assuming markdown for README
    author="Oliver Kaiser",
    author_email="oliver.kaiser@outlook.com",
    maintainer="Rafal Chrabaszcz, Munib Shah",  # Added Mushah as a maintainer
    maintainer_email="rchrabas@cisco.com, mushah@cisco.com",  # Added Mushah's email
    license="GPL-3.0-only",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["firerest76", "firerest76.fmc"]),  # Updated package names
    python_requires=">=3.9",
    install_requires=[  # List your dependencies
        "requests>=2.23.0",
        "packaging>=20.3",
    ],
    include_package_data=True,
    zip_safe=False,
)
