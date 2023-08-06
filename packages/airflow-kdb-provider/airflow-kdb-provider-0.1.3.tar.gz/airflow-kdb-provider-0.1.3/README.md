# Airflow KDB Provider

A lightweight KDB provider for Apache Airflow, featuring the `KDBAirflowOperator`. This provider allows for seamless integration between Airflow and KDB+/q, making it easier to automate data pipelines that involve KDB+/q.

## Installation

You can install the Airflow KDB Provider package from PyPI using the following command:

```bash
pip install airflow-kdb-provider
```
## Usage
To use the KDBAirflowOperator in your Airflow DAG, you must first import it and create an instance of the operator. Here is an example:

from airflow_kdb_provider.operators.kdb_operator import KDBOperator
```python
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

