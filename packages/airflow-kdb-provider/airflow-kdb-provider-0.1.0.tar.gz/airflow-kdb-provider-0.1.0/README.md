# KDBAirflowOperator
A light weight KDB operator for Apache Airflow
KDBAirflowOperator
KDBAirflowOperator is a custom Apache Airflow operator that can be used to execute KDB+/q scripts from within Airflow DAGs. KDB+/q is a high-performance, column-oriented database that is popular in the financial industry. This operator allows for seamless integration between Airflow and KDB+/q, making it easier to automate data pipelines that involve KDB+/q.

Installation
To use this operator, you must first clone the repository from Github:


```python 
git clone https://github.com/kabir12345/KDBAirflowOperator.git 
```
Once you have cloned the repository, you can install the operator and its dependencies by running the following command:

```python 
pip install -e KDBAirflowOperator
```

This will install the operator in editable mode (-e option), which allows you to make changes to the code and have those changes reflected immediately without the need to reinstall.


Usage
To use the KDBAirflowOperator in your Airflow DAG, you must first import it and create an instance of the operator. Here is an example:
 
```python 
from KDBOperator import KDBOperator
kdb_operator = KDBOperator(
    task_id='run_kdb_script',
    command='/path/to/kdb_script.q',
    params={'param1': 'value1', 'param2': 'value2'},
    conn_id='kdb_conn',
    dag=dag) 
 ```

In this example, we create an instance of the KDBOperator and specify the following parameters:

task_id: the task ID for this operator
command: the path to the KDB+/q script that we want to execute
params: a dictionary of parameters that will be passed to the KDB+/q script as command-line arguments
conn_id: the connection ID for the KDB+/q server that we want to use (this should be defined in Airflow's Connections interface)
dag: the DAG that this operator belongs to
Once you have created an instance of the KDBOperator, you can add it to your DAG like any other Airflow operator:


```python 
some_other_operator >> kdb_operator >> some_other_operator2
```

In this example, we have added the kdb_operator to our DAG and specified that it should be executed after some_other_operator and before some_other_operator2.








