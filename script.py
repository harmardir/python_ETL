# Import the required library
import requests
import os

path = "https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip"

# Get the zip file
response = requests.get(path)

# Print the status code
print(response.status_code)

# Save the file locally
local_dir = os.getcwd()
#local_path = f"tmp/data/source/downloaded_at=2021-02-01/PPR-ALL.zip"
local_path = local_dir + "/PPR-ALL.zip"
with open(local_path, "wb") as f:
    f.write(response.content)

# Import the required method
from zipfile import ZipFile

with ZipFile(local_path, "r") as f:
    # Get the list of files
    file_names = f.namelist()
    print(file_names)
    # Extract the CSV file
    csv_file_path = f.extract(file_names[0])
    print(csv_file_path)