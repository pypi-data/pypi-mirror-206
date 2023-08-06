from setuptools import setup

setup(
    name='IrisChatBot',
    version='0.0.9',
    packages=['mx', 'mx.com', 'mx.com.bancoazteca', 'mx.com.bancoazteca.cloud', 'mx.com.bancoazteca.cloud.core',
              'mx.com.bancoazteca.cloud.core.utilerias', 'mx.com.bancoazteca.cloud.core.seguridad', 'mx.com.bancoazteca.cloud.abonos'],
    url='http://devops:8181/cloud/irischatbot',
    license='License :: OSI Approved :: MIT License',
    author='Chapter Cloud and DevOps',
    author_email='clouddevops@elektra.com.mx',
    description='',
    dependencies = [ # Optional
      "requests","pycryptodome"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords = ["BAZ", "Cobranza", "Cloud","Iris","Bot","ChatBot","Core"]  # Optional
)
