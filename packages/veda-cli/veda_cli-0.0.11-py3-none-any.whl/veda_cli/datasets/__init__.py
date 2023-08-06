import typer
from rich.table import Table
from rich.console import Console
from pysondb import db
import os
from datetime import datetime
from airavata_mft_cli import operations as ops
from airavata_mft_cli import config as configcli
from airavata_mft_sdk import mft_client
from airavata_mft_sdk.scp import SCPCredential_pb2
from airavata_mft_sdk.scp import SCPStorage_pb2
from airavata_mft_sdk.common import StorageCommon_pb2


app = typer.Typer()

def get_db():
    return db.getDb(os.path.join(os.path.expanduser('~'), ".veda", "ds.json"))

def get_exec_db():
    return db.getDb(os.path.join(os.path.expanduser('~'), ".veda", "db.json"))

@app.command("list")
def list_datasets():
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
    db_conn = get_db()
    datasets = db_conn.getBy({"type":"Dataset",  "name": dataset_name})
    for ds in datasets:
        print(ds)

def get_file_list(storage_id, root_dir):

    metadata_resp = ops.get_resource_metadata(storage_id + "/" + root_dir)

    file_metadata = metadata_resp.directory.files

    files = []
    for f in file_metadata:
        files.append(f.friendlyName)

    return files

@app.command("register")
def register_dataset(execution_id, dataset_name, dataset_path):
    print("Registring the dataset")

    db_conn = get_exec_db()
    executions = db_conn.getBy({"type":"Execution", "executionId": execution_id})
    execution = executions[0]
    storage_id = execution["storageId"]
    output_dir = execution["outputDir"]

    dataset_path = output_dir + "/" + dataset_path

    db_conn = get_db()
    db_conn.add({
        "type": "Dataset",
        "storageId": storage_id,
        "name": dataset_name, 
        "base_path": dataset_path, 
        "createdTime": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "files": get_file_list(storage_id, dataset_path)})
    
@app.command("copy")
def copy_dataset(dataset_name, target_storage):
    print("Publishing the Dataset to storage " + target_storage)
    db_conn = get_db()
    datasets = db_conn.getBy({"type":"Dataset",  "name": dataset_name})
    if len(datasets) > 0:
        ds = datasets[0]
        ops.copy(ds["storageId"] + "/" + ds["base_path"], target_storage + "/" + ds["name"] + "/")
        ds["storageId"] = target_storage
        db_conn.add(ds)

@app.command("delete")
def delete_dataset(dataset_name):
    db_conn = get_db()
    datasets = db_conn.getBy({"type":"Dataset",  "name": dataset_name})
    for ds in datasets:
        db_conn.deleteById(ds['id'])

