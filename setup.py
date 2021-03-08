from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as f:
    required = f.read().splitlines()

setup(
    name="joint_bert",
    version="0.0.1",
    description="join bert model for intent slot",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Singularsun/JointBert",
    packages=find_packages(exclude=["data", "tests"]),  # same as name
    install_requires=required,
    include_package_data=True,
    python_requires=">=3.6",
)
