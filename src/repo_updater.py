import datetime
from git import Repo

random_string = 'Record for ' + str(datetime.datetime.now())

# Read existing content from Readme.md
md_file = '../Readme.md'
with open(md_file, 'r') as file:
    readme_content = file.read()

# Append the random string to the Readme content
new_readme_content = readme_content + f"\n{random_string}"

# Write the updated content back to Readme.md
with open(md_file, 'w') as file:
    file.write(new_readme_content)

# Commit changes
repo = Repo('../')
index = repo.index
index.add(['Readme.md'])
index.commit(f"Add new string: {random_string}")

# Push changes to remote repository
origin = repo.remote(name='origin')
origin.push()
print("Update finished")
