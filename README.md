# Multilabel Song Genre Classifier

## Project Info:
A song genre classifier is a machine learning model that can categorize songs into different genres based on song lyrics. The model can classify 137 different types of song genres. This model is trained on a large dataset of songs with known genre labels, and uses algorithms to identify patterns in the lyrics that are indicative of a specific genre. Once trained, the model can be used to automatically classify new songs into the appropriate genre, which can be useful for music recommendation systems or for organizing large music libraries. This is an alternative to classifying song genres based on audio data.

## Data Collection:
Dataset Collection is a crucial step in the development of any this model. Great care is taken to ensure the highest quality of data. 
The data used for this model is collected from 3 different websites and merged together to create the required dataset.
The dataset, as of now contains 9125 rows and 4 columns. This dataset will be updated and the updated version will contain about 37710 rows and 4 columns. The model will be trained on the updated version. <br/>
The 4 columns are: artist, song, spotify_genre and wiki_genre. The current model is trained only to classify spotify genre types. <br/>
The Websites that are used to collect data are: <br/>
1. [Rockarchive.](https://www.rockarchive.com/)<br/>
2. [AZLyrics.](https://www.azlyrics.com/)<br/>
3. [Chosic.](https://www.chosic.com/)<br/>

## Data Preprocessing:
Initially there were 1741 different genres in the dataset. Out of which, 1604 were rare genres. These rare genres were removed and only 137 were taken for consideration. After that song lyrics without any genres were removed, resulting in 7724 samples.

## Model Training:
A `distilrobera-base` model sourced from HuggingFace Transformers was used. This model was finetuned using Fastai and blurr. <br/>
The accuracy score of the model is:<br/>
F1 Score (Micro) = 0.5965437022266534<br/>
F1 Score (Macro) = 0.26071636343696014

