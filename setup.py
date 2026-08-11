from setuptools import setup, find_packages
setup(
    name="tat-public", version="0.1.0",
    author="Marat Sultanov",
    url="https://github.com/maratsultanov2/TAT-ROOT",
    packages=find_packages(where="src"), package_dir={"": "src"},
    install_requires=["numpy","scipy","matplotlib","pandas"],
)
