# Seeds Labeler

## Installation

Install the last version of SeedsLabeler with `pip install SeedsLabeler --upgrade`.

More details in [INSTALL.md](INSTALL.md).

## Run SeedsLabeler

In a terminal, simply run `SeedsLabeler`.

## Guidelines

For any modification request, open an issue.

Once the issue is solved, commit your changes with the message "Fixes #<issue_number>". The issue will be automatically closes at the next push/merge/deployement.

## Updates

`conda activate SeedsLabeler`

`python SeedsLabeler.py`
`python SeedsLabeler.py --project /Users/giancos/Desktop/SeedsLabeler/project.annt`

### Modify UI

To update the user interface, modify `src/gui/mainwindow.ui` and recompile the equivalent python file with 

`pyuic5 src/gui/mainwindow.ui -o src/gui/ui_mainwindow.py`

## [Dev] Update pip pacakge (requires admin rights for pip project and github repo)

Update [version.py](src/libs/version.py) with the new version number.

Make wure twin is installed: `pip install twine`

Run `python setup.py upload`.


# OLD SERVER
curl -H "Content-Type: image/jpeg" -H "project_id: Striga_Strat2" -H "api_token: bc470cc3459349b4bcbb685a217e83a0" -X POST --data-binary @sample.jpg http://cloudlabeling.org:4000/api/predict

# SERVER ON THYA TECH
curl -X POST 'https://api-infer.thya-technology.com/api/v1/inference' -H 'x-api-key: 0cda174e183667abd12e061e9ced3c0ecb008c52bd4830e7d293bd6847c211a4' -F 'projectId=4' -F 'images=@sample.jpg;type=image/jpeg'





