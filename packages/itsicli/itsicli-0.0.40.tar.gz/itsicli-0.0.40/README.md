# The ITSI Command Line Interface (CLI)

## Setup Virtualenv


```
python3 -m venv /path/to/new/virtual/environment

source /path/to/new/virtual/environment/bin/activate
```
For more info about venv, click [here](https://docs.python.org/3/library/venv.html).

## ```itsi-content-pack``` overview

The `itsi-content-pack` command assists in creating and managing ITSI Content Packs. The main functionality is to convert an itsi backup zip file into Splunk App for Content Packs supported format for itsi objects. Supported backup version is 4.9.0

The general end-to-end workflow is as follows with example provided in each step:

## Dependencies
The `itsi-content-pack` command depends on the ```itsimodels``` python module to convert an itsi backup to itsi object jsons used by Splunk App for Content Packs. Here's [source link](https://github.com/splunk/itsi-models) to ```itsimodels```. The packaged ```itsimodule``` is published [here](https://pypi.org/project/itsimodels/) on PyPI, and can be installed via pip (see below).

## Steps to create content pack

- [Clone the repos](#clone-the-repos)
- [Prep your environment](#prep-your-environment)
- [Initialize content pack](#initialize-content-pack)
- [Import itsi backup](#import-itsi-backup)

### Clone the repos
Clone the following repos on your local box. It is recommended that you do this on a linux box.

- [itsi-cli](https://github.com/splunk/itsi-cli) (current repo)
- [itsi-models](https://github.com/splunk/itsi-models)
- [itsi-content](https://github.com/splunk/itsi-content)


### Prep your environment
- Install the latest dependent python packages
    ```
    pip install --upgrade itsicli
    pip install --upgrade itsimodels
    ```


- Update PATH to include `itsi-cli/bin` so we can invoke `itsi-content-pack` command from anywhere:

    ```export PATH=$PATH:<path to itsi-cli/bin>```
    
    >Example:
    >
    >export PATH=$PATH:/my/git/itsi-cli/bin


:bulb: If you are a developer working on fixing itsicli or itsimodels and would like to test with unpublished changes in your own environment, then set your PYTHONPATH to include `itsi-models` and `itsi-cli` top level folders to utilize your local changes:
```
export PYTHONPATH=<path to itsi-cli>:<path to itsi-models>
```
>Example:
>
>export PYTHONPATH=/my/git/itsi-cli:/my/git/itsi-models

### Initialize content pack
This step only needs to be done once if you are starting fresh content pack. You can always remove the directory created below and start over if needed. Steps below shows how to create a new content pack in your local clone of ```itsi-content``` repo. You can always create the content pack in some other folder on your system and then copy into [src]((https://github.com/splunk/itsi-content/tree/main/src)) of your ```itsi-content``` folder when you are ready to test/build/push changes.

- Create a new git branch for your changes in your local clone of ```itsi-content```

- Create an empty folder under [src]((https://github.com/splunk/itsi-content/tree/main/src)) of your local clone of itsi-content repo

    ```mkdir DA-ITSI-CP-<your-cp-name>```
    
    This will be the main folder of your content pack, see other content pack folders [here](https://github.com/splunk/itsi-content/tree/main/src). 
      
- Go into the folder you just created

    ```cd DA-ITSI-CP-<your-cp-name>```
    
- Create skeleton files/folders

    ```itsi-content-pack init```
    
    Follow the prompt to provide a content pack id and title. Please prefix id with `DA-ITSI-CP-`. Once completed, you should see the following folders and files created                                                                                 
    
    ```
    ├── appserver
    │   └── static
    │       └── screenshots
    ├── default
    │   └── app.conf
    └── itsi
        ├── README.md
        ├── config.json
        └── manifest.json
    ```
    You should update README.md to explain what your content pack is for. See other content packs for inspirations. You should also add thumbnails and screenshots for your content pack.
     


### Import itsi backup
Once the content pack is initialized, you can create content pack ITSI objects by importing your itsi backup zip file. Perform the command from within your ```DA-ITSI-CP-<your-cp-name>``` directory.
```
itsi-content-pack importbackup <path-to-backup-zip-file>
```

>Example:
>
>itsi-content-pack importbackup /full/path/to/my_cp_itsi_partial_backup490.zip


You will see logging messages and maybe some warnings as well. Take a look at the warnings to see if there are any real issues.

You can rerun this step many times. You may want to first backup your previous ```DA-ITSI-CP-<your-cp-name>\itsi``` folder for comparison/backup before you run ```importbackup``` again. 

### Continue to add, remove, or edit content from the Content Pack
You can add or remove objects inside each object type directory, make sure to update manifest.json as part of your changes.


### Add any supporting Splunk knowledge objects
This DA-ITSI-CP-* is a Splunk app, so feel free to add lookups, transforms, props, etc that are Splunk compatible.


### Validate the Content Pack through the `validate` command
Inside DA-ITSI-CP-*, run following command to validate if this content pack is compatible with ITSI.

```
itsi-content-pack validate
```

# Submit content pack

Please follow README in itsi-content repo
### Build content pack app
### Install content pack app
### Install your content pack
### Submit content pack via PR
Submit the Content Pack to either:
    - Splunkbase (must first run the `build` command)
    - The ITSI Splunk App for Content Packs via a pull request on Github repo: itsi-content


# Build the itsicli distribution archive and upload it to PyPi
For releasing the packages you must have Maintainer access on PyPi
 
There are two ways:
- [Build and release itsicli packages manually](#build-and-release-itsicli-packages-manually)
- [Build and release itsicli packages automatically](#build-and-release-itsicli-packages-automatically)
## Build and release itsicli packages manually

:exclamation: __Please build the package on linux box__

Install the build dependencies:
```
pip install --upgrade setuptools wheel
```

### Generate the Python package
Clean up distribution:
```
make clean
```

Generate the Python distribution archive:
```
make
```

### Upload to the Python Package Index

Install the dependencies required for uploading to the index:

```
pip install --upgrade twine
```

Upload to PyPI:

```
make upload
```
## Build and release itsicli packages automatically
- On the left sidebar, select CI/CD > Pipelines. 
- Select Run Pipeline.
- In the Run for branch name select the branch to run the pipeline for.
- Select Run pipeline.
- base_stage job will run automatically
- sast and whitesource_python are manual jobs that do not need to be triggered if you are trying to release the packages on PyPi.
- After successfully completion of previous job you have to click on the Settings icon of `build` job to fill variables for providing username and password
- Fill the data as follows
    ```text
    Key: username
    Value: <username of PYPI> 
    ```
    ```text
    Key: password
    Value: <password of PYPI> 
    ```
- Click on `Trigger this manual action` to start the pipeline
- Please wait for the `build` job to complete

## Troubleshooting

Log file name:
```
itsi_contentpacks_itsicli.log
itsi_contentpacks_itsimodels.log
```

If you have $SPLUNK_HOME environment set, then you can find the log file in:
```
$SPLUNK_HOME/var/log/splunk/
```
Otherwise, you will find the log file in ```~/```

