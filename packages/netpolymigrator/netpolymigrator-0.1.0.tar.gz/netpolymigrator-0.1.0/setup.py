from setuptools import setup, find_packages

setup(
    name="netpolymigrator",
    version="0.1.0",
    author="Sanjeev Ganjihal",
    author_email="sanjeevrg7@gmail.com",
    description="A tool to migrate Calico and Cilium network policies to Kubernetes native network policies",
    url="https://github.com/sanjeevrg89/NetPolyMigrator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "boto3",
        "click",
        "kubernetes",
        "PyYAML",
    ],
    entry_points={
     "console_scripts": [
         'netpolymigrator=netpolymigrator.cli:cli'
     ],
 }
)
