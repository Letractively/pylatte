'''
Created on 2012. 8. 4.

@author: HwanSeung Lee(rucifer1217@gmail.com)
'''
from distutils.core import setup, Extension

classifierList=['Development Status :: 4 - Beta',
                'Environment :: Console',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.2',
                'Topic :: Internet :: WWW/HTTP']

longDescription = """
=======
Pylatte 
=======
Pylatte : A Web Framework Based on Python 3 Pylatte is a web framework created specifically for Python 3. Developers can now generate websites with Pylatte in Python 3, just as they might for Python 2x-based frameworks such as Django, Flask, or Bottle.

Visit to http://www.pylatte.org/

mail : pylatte@pylatte.org

Facebook Page : https://www.facebook.com/pylatte

Sample code
-----------
The following code is a example pyl file.

<p>Pylatte</p>
<$
pyl = "HTML" + " + " + "python"
$>
<p>
<$=pyl$>
</p>
The pyl code is translated by Pylatte to HTML in the browser.
 
<p>Pylatte</p>
<p>
HTML + python
</p>

Functions
---------
Translation Engine Pylatte uses pyl file format. pyl consists of HTML and Python. pyl is fully translated by the Pylatte engine into HTML. It is unique feature of Pylatte.

Database
--------
To use the database, external library must be installed: the MySQLdb(for mysql) module or pymongo3(for MonogoDB) module for Python 3.

Simple and advanced SQL via specific functions that are similar to iBATIS are provided.

Session
-------
A session is needed to distinguish each client.

Filter
------
If a filter is set, select pages pass through the filter.

Form File
---------
It is possible to upload a file to server via POST.

URL Mapping
-----------
For security purposes, URL mapping transfers virtual URLs accessed by clients to web pages.
"""


setup(name='Pylatte',
      author='HwanSeung lee',
      author_email='rucifer1217@gmail.com',
      description='Web Framework - Insert Python code in HTML(called PYL) and execute webserver',
      long_description=longDescription,
      license = "GPL",
      keywords = "webserver Framework",
      url='http://pylatte.org',
      version='0.9.7',
      classifiers = classifierList,
      packages=['Pylatte','Pylatte.Database','Pylatte.WebServer']
)
