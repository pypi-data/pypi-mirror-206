from setuptools import setup, find_packages

setup(name='create_stc', version='0.1.4', packages=["create_stc"], include_package_data=True, entry_points={'console_scripts': ['create_stc = create_stc.create_streamlit_comp:run']})
