import datetime
import os
from git import Repo


repo_dir = os.path.dirname(os.path.abspath(__file__)) + '/../'
os.chdir(repo_dir)
readme_path = "Readme.md"
random_string = 'Record for ' + str(datetime.datetime.now())

# Read existing content from Readme.md

with open(readme_path, 'r') as file:
    readme_content = file.read()

# Append the random string to the Readme content
new_readme_content = readme_content + f"\n{random_string}"

# Write the updated content back to Readme.md
with open(readme_path, 'w') as file:
    file.write(new_readme_content)

# Commit changes
repo = Repo(repo_dir)
index = repo.index
index.add([readme_path])
index.commit(f"Add new string: {random_string}")

# Push changes to remote repository
origin = repo.remote(name='origin')
origin.push()
print("Update finished")
