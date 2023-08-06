from setuptools import find_packages, setup

# Read the README.md content
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='airflow-kdb-provider',
    version='0.1.1',
    description='Apache Airflow provider for KDBAirflowOperator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Kabir Jaiswal',
    author_email='kabirjaiswal30@gmail.com',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'apache-airflow>=2.0.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
)
