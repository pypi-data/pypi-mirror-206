from setuptools import setup

long_description = None
with open('README.md', encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = "CustomTkinterTitlebar",
	version = "1.0.7.8",
	author = "littlewhitecloud",
	author_email = "q1141926647@163.com",
	description = "This is a project can help you to have a custom titlebar!",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	keywords = 'python c windows cplusplus dll cpp custom pillow blur ctypes tk titlebar tkinter window windows10 doc msvc details user32 darkdetect',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
	],
	url = "http://github.com/littlewhitecloud/CustomTkinterTitlebar", 

	packages = ["CustomTkinterTitlebar"],
	package_data = {'': ["*.dll"]},
	include_package_data = True,
	install_requires = ["Pillow>=9.0.0", "darkdetect>=0.8.0", "BlurWindow>=1.2.1"],
	python_requires='>=3.8',
)

