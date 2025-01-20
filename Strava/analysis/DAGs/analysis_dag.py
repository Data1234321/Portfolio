# -- Public Imports
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

# Default arguments that will be passed onto the DAG
default_args = {
    'owner': 'Tom Billington',
    'depends_on_past': False,
    'email': ['tm.billington@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        'Strava_Analysis',
        default_args=default_args,
        description='Analyse strava details',
        schedule_interval="05 5 * * *",  # UTC Time
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=["Strava", "ETL", "Analysis"],
) as dag:
    task1 = DockerOperator(
        task_id="Strava_Analysis",
        image="strava_analysis:0.0.1",
        api_version="auto",
        auto_remove=True,
        command=[
            "sh",
            "-c",
            """
            poetry run python --all
            """,
        ],
        docker_url="unix://var/run/docker.sock",
        network_mode="host",
        force_pull=False,
        mount_tmp_dir=False,
    )

    # Task Dependencies
    task1
