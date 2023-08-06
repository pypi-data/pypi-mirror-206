import setuptools

setuptools.setup(
	name="buildington",
	version="1.6",
	author="RixTheTyrunt",
	author_email="rixthetyrunt@gmail.com",
	description="Building websites like React, and hosting 'em like Flask!",
	packages=["buildington"],
	classifiers=[
		"Environment :: Console",
		"Framework :: Flask",
		"Operating System :: OS Independent",
		"Topic :: Internet :: WWW/HTTP :: HTTP Servers",
		"Topic :: Internet :: WWW/HTTP :: Site Management",
		"Topic :: Internet :: WWW/HTTP :: WSGI :: Server"
	],
	install_requires=["flask"],
	long_description=open("README.txt").read(),
	long_description_content_type="text/plain"
)
