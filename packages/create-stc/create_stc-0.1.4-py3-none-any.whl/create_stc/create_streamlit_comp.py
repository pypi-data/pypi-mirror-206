import sys
import os
from shutil import copytree, ignore_patterns
import pkg_resources


def replace_component_name(file_path, component_name):
	with open(file_path, "r") as f:
		file_content = f.read()
	new_content = file_content.replace("my_component", component_name)
	with open(file_path, "w") as f:
		f.write(new_content)


def component_name_with_dash(component_name):
	return component_name.replace("_", "-", 1)


def run():
	args = sys.argv[1:]
	component_name = "my_component"
	if len(args) == 0:
		_component_name = input("Enter your component name (Default my_component): ")
		if _component_name:
			component_name = _component_name
	else:
		component_name = args[0]

	print(f"Scaffolding project in {os.path.abspath(f'./{component_name}')}...")

	template_folder = pkg_resources.resource_filename(__name__, "template")
	new_folder = f"./{component_name}"
	copytree(template_folder, new_folder, ignore=ignore_patterns("node_modules", "package-lock.json", ".eslintcache", "build", "dist", "*.egg-info"))

	component_folder = f"{new_folder}/my_component"
	os.rename(component_folder, f"{new_folder}/{component_name}")

	setup_file = f"{new_folder}/setup.py"
	manifest_file = f"{new_folder}/MANIFEST.in"
	init_file = f"{new_folder}/{component_name}/__init__.py"
	package_json_file = f"{new_folder}/{component_name}/frontend/package.json"

	replace_component_name(setup_file, component_name)
	replace_component_name(manifest_file, component_name)
	replace_component_name(init_file, component_name)
	replace_component_name(package_json_file, component_name_with_dash(component_name))

	print("Done! Now run:")
	print(f" cd {new_folder}/{component_name}/frontend")
	print(" npm install")
	print(" npm start")
	print("Open a new terminal and run:")
	print(f" cd {new_folder}")
	print(" streamlit run main.py")