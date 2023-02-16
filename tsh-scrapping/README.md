# Really learning python

to activate the python virtual enviroment in Windows you have to run the flowwing command
```
.\<env-name>\Scripts\activate
```

In linux
```
source <env-name>/bin/activate
```

to create an enviroment run:
```
python -m venv venvName
```

We put all our dependecies in the requirements.txt file, so everyone can know what packages the projects need
And when you want to install all the dependencies you go to terminal, activate the python enviroment and run the following:
```
pip install -r requirements.txt
```
And pip will install all the packages in the enviroment, you should also track the version of each package

To check the version installed of a package you can run

```
pip show package_name
```