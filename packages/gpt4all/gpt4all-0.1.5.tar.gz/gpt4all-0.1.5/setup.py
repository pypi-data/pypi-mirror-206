from setuptools import setup, find_packages, Extension
import os
import platform
import shutil

from Cython.Build import cythonize

package_name = "gpt4all"

# Define the location of your prebuilt C library files
SRC_CLIB_DIRECtORY = "../../llmodel/"
SRC_CLIB_BUILD_DIRECTORY = "../../llmodel/build"

LIB_NAME = "llmodel"


DEST_CLIB_DIRECTORY = os.path.abspath(f"{package_name}/{LIB_NAME}_DO_NOT_MODIFY")
DEST_CLIB_BUILD_DIRECTORY = os.path.abspath(os.path.join(DEST_CLIB_DIRECTORY, "build"))
# LIB_BUILD_DIR is where Cython extension will look for library via rpath
LIB_BUILD_DIR = os.path.abspath(f"{LIB_NAME}_DO_NOT_MODIFY/build")
HOME_DIR = os.path.abspath(".")

system = platform.system()

def get_c_shared_lib_extension():
    
    if system == "Darwin":
        return "dylib"
    elif system == "Linux":
        return "so"
    elif system == "Windows":
        return "dll"
    else:
        raise Exception("Operating System not supported")
    

lib_ext = get_c_shared_lib_extension()


def copy_prebuilt_C_lib(src_dir, src_build_dir, dest_dir, dest_build_dir):
    files_copied = 0

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for item in os.listdir(src_dir):
        # copy over header files to dest dir
        if item.endswith(".h"):
            s = os.path.join(src_dir, item)
            d = os.path.join(dest_dir, item)
            shutil.copy2(s, d)
            files_copied += 1

    if not os.path.exists(dest_build_dir):
        os.mkdir(dest_build_dir)
    for item in os.listdir(src_build_dir):
        # copy over shared library to dest build dir
        if item.endswith(lib_ext):
            s = os.path.join(src_build_dir, item)

            # Need to copy .dll right next to Cython extension for Windows
            if system == "Windows":
                d = os.path.join(HOME_DIR, item)
                shutil.copy2(s, d)
            else:
                d = os.path.join(dest_build_dir, item)
            
            shutil.copy2(s, d)
            files_copied += 1
    
    return files_copied


# NOTE: To build Cython extension correctly, you must provide correct path to
# the prebuilt llmodel C library. Specifically, the llmodel.h and C shared library are needed.
copy_prebuilt_C_lib(SRC_CLIB_DIRECtORY,
                    SRC_CLIB_BUILD_DIRECTORY,
                    DEST_CLIB_DIRECTORY,
                    DEST_CLIB_BUILD_DIRECTORY)

def get_extra_link_args():
    if system != "Windows":
        return [f'-Wl,-rpath,{DEST_CLIB_BUILD_DIRECTORY}', f'-Wl,-rpath,{LIB_BUILD_DIR}']
    else:
        # no rpath option for Windows
        return []

llmodel_extension = Extension(
    name="gpt4all.pyllmodel",
    sources=["gpt4all/pyllmodel.pyx"],
    libraries=["llmodel"],
    library_dirs=[DEST_CLIB_BUILD_DIRECTORY, LIB_BUILD_DIR, HOME_DIR],
    include_dirs=[DEST_CLIB_DIRECTORY],
    extra_link_args=get_extra_link_args()
)

ext_modules = cythonize([llmodel_extension])

setup(
    name=package_name,
    version="0.1.5",
    description="Python bindings for GPT4All",
    author="Richard Guo",
    author_email="richard@nomic.ai",
    url="https://pypi.org/project/gpt4all/",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=[
        "Cython==0.29.34",
        "pytest==7.3.1"],
    ext_modules=ext_modules,
    package_data={'llmodel': [f"{DEST_CLIB_DIRECTORY}/*", f"{HOME_DIR}/*.dll"]},
    include_package_data=True
)