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
A `distilroberta-base` model sourced from HuggingFace Transformers was used. This model was finetuned using Fastai and blurr. <br/>
The accuracy score of the model is:<br/>
F1 Score (Micro) = 0.5965437022266534<br/>
F1 Score (Macro) = 0.26071636343696014

## Model Compression with ONNX:
To deploy the model, the model's size needed to be compressed. The initial model was 313.8 MB in size and through onnx quantization method the final size came down to 78.7 MB and a bit faster at the same time.<br/>

## Model deployment
The model was deployed on Hugging Face, and the model API was connected to a website that was set up on Render using Flask.

## Deployment of API on Render:
The deployed model API has been integrated into this [render]([https://naosher98.github.io/Ball-Recognizer/),](https://song-genre-classifier.onrender.com) allowing users to easily access and test the model's capabilities. .<br/>
Here is the website:.<br/>
<a href="https://song-genre-classifier.onrender.com">
<img src = "data\Capture.PNG" width = "900" height = "450">
</a><br/>
Here is the output result:<br/>
<a href="https://song-genre-classifier.onrender.com">
<img src = "data\Capture1.PNG" width = "450" height = "450">
</a>
