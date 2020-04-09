# Google Cloud Translation API with Python

This small tutorial shows how to quickly connect to Google Cloud API to make a string translation.

## Requirements for this tutorial

* Google Cloud Account
* Ubuntu

## Install Google SDK

Tutorial here: <https://cloud.google.com/sdk/docs/downloads-apt-get>

First we add the Cloud SDK distribution URI with:


`echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list`

`sudo apt-get install apt-transport-https ca-certificates gnupg`

We import the Google Cloud public key

`curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -`

Update and install the Cloud SDK.

`sudo apt-get update && sudo apt-get install google-cloud-sdk`

You should now have it installed. To start using it you should now connect to the account you are going to use.

`gcloud init`

You will be asked about which project you will want to connect to. In this case you should create a new one which will enseforth be identified as '[PROJECT]'

## Activate a Google Cloud Translate API

1. Go to the Google Cloud Platform.
2. Select your project on the top-left corner.
2. Search for "Cloud Translation API" and enable it.

## Install Google Cloud Translate through PIP

`pip install google-cloud-translate`

## Make a service account

Henceforth, `[NAME]` will be the name of the service account.
First start by creating it with `gcloud iam service-accounts create [NAME]`.

We can then grant permissions to this service-account, for now it is owner, though it should be carefully considered if that is the case.
`gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"`

## Generate the JSON key file

`gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com`

## Authenticate with JSON file.

Simply export it as GOOGLE_APPLICATION_CREDENTIALS.

`export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"`

## Creating the Python Script

To keep in mind:

1. Should have an encoding at the start like `# -*- coding: utf-8 -*-`.
2. Import the Translate model.
3. Apply the model by puttin in the string and the target language.


