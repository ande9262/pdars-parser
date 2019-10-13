import setuptools

setuptools.setup(
    name="pdars-parser",
    version="0.0.1",
    author="Cobec Dev Team",
    author_email="helpdesk@cobec.com",
    description="PDARS parser",
    package_dir={"pdars": "src/pdars"},
    py_modules=["pdars.hello_world"]
)