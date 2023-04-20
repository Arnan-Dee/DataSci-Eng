# DataSci-Eng

To install all the dependencies use

```shell
py -m venv spark
.\spark\Scripts\activate
py -m pip install pyspark==3.3.2 request pandas
```

More information regarding venv can be found in https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment.

Then run cells in demo.ipynb(located in spark/execution_scripts/demo.ipynb). Demo.ipynb is the file that
produce the same result as Spark but it processes data in sequential manner. The analytic script using Spark is still worked on. Nevertheless, as a demo, it serves the same result.

This command above will produce jpg files in folder resources/photos and processed.csv in the same
folder. Those data file is ready to be use in ML pipeline. However, prior data cleaning also need to be done.
