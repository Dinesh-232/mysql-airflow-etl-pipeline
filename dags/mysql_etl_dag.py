
from datetime import timedelta
import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


# Default arguments
default_args = {
    "owner": "dinesh",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}


# Create DAG
with DAG(
    dag_id="mysql_etl_pipeline",
    default_args=default_args,
    description="MySQL to Python ETL Pipeline",
    start_date=pendulum.datetime(
        2026, 11, 3, tz="Asia/Kolkata"
    ),
    schedule="*/5 * * * *",
    catchup=False,
    tags=["mysql", "python", "ETL"],
) as dag:

    run_etl = BashOperator(
        task_id="execute_etl_script",
        bash_command="bash $HOME/airflow_project/scripts/wrapper.sh ",
    )
