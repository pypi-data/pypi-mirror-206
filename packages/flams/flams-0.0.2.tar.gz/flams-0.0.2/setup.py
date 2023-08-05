from setuptools import setup, find_packages

setup(
    name="flams",
    version="0.0.2",
    description="Find Lysine Acylation & other Modification Sites",
    readme="README.md",
    python_requires=">=3.10",
    packages=find_packages(
        include=["flams*"],
    ),
    entry_points={
        'console_scripts': [
            'FLAMS = flams.flams:main'
        ]
    },
    install_requires=[
        "appdirs",
        "biopython",
        "requests",
    ]
)
