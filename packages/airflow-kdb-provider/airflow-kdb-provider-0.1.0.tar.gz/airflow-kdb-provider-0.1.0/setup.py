from setuptools import find_packages, setup

setup(
    name='airflow-kdb-provider',
    version='0.1.0',
    description='Apache Airflow provider for KDBAirflowOperator',
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
