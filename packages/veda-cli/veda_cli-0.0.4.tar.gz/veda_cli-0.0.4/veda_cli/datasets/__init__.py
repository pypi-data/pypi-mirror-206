import typer
from rich.table import Table
from rich.console import Console
from pysondb import db
import os
from datetime import datetime
from airavata_mft_cli import operations as ops


app = typer.Typer()

def get_db():
    return db.getDb(os.path.join(os.path.expanduser('~'), ".veda", "ds.json"))

@app.command("list")
def list_daatasets():
    console = Console()
    table = Table()

    table.add_column('Dataset Name', justify='left')
    table.add_column('Description', justify='left')
    table.add_column('Tags', justify='left')

    table.add_row('ECCO-NASA-V4', 'NASA Hosted ECCO V4 Dataset', 'OCEAN, CLIMATE')

    db_conn = get_db()
    dss = db_conn.getBy({"type":"Dataset"})

    for ds in dss:
        table.add_row(ds["name"], "Replica available in storage " + ds["storageId"], 'CUSTOM')

    console.print(table)

@app.command("info")
def dataset_info(dataset_name):
    print("Printing dataset info")


def get_file_list(root_dir):
    files = [os.path.relpath(os.path.join(dirpath, file), root_dir) 
             for (dirpath, dirnames, filenames) in os.walk(root_dir) for file in filenames]

    return files

@app.command("register")
def register_dataset(dataset_name, dataset_path):
    print("Registring the dataset")
    db_conn = get_db()
    db_conn.add({
        "type": "Dataset",
        "storageId": "local-agent",
        "name": dataset_name, 
        "base_path": dataset_path, 
        "createdTime": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "files": get_file_list(dataset_path)})
    
@app.command("publish")
def publish_dataset(dataset_name, storage_id):
    print("Publishing the Dataset to storage " + storage_id)
    db_conn = get_db()
    datasets = db_conn.getBy({"type":"Dataset", "storageId": "local-agent", "name": dataset_name})
    if len(datasets) > 0:
        ds = datasets[0]
        ops.copy(ds["storageId"] + "/" + ds["base_path"], storage_id + "/" + ds["name"] + "/")
        ds["storageId"] = storage_id
        db_conn.add(ds)