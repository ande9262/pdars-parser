import setuptools

# to include yum dependencies (or can add with bdist_rpm --requires my-package)
#from setuptools.command.bdist_rpm import bdist_rpm
# RPM_REQUIRED_DEPS = "my-yum-package-to-install"
#
# def custom_make_spec_file(self):
#     spec = self._original_make_spec_file()
#     line_description = "%description"
#     spec.insert(spec.index(line_description) - 1, "requires: %s" % RPM_REQUIRED_DEPS)
#     return spec
# bdist_rpm._original_make_spec_file = bdist_rpm._make_spec_file
# bdist_rpm._make_spec_file = custom_make_spec_file

setuptools.setup(
    name="pdars-parser",
    version="0.0.1",
    author="Cobec Dev Team",
    author_email="helpdesk@cobec.com",
    description="PDARS parser",
    package_dir={"pdars": "src/pdars"},
    py_modules=["pdars.hello_world"],
    data_files=[("/usr/local/sbin", ["src/mgr_pdars_parser.sh"])]
)