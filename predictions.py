# Import libraries
import numpy as np
import pandas as pd
import requests

from PIL import Image
from io import BytesIO

from feature_extractor import FeatureExtractor


class GenerateSimilarImages:

    # Constructor
    def __init__(self, image_url):
        self.image_url = image_url
        self.feature_extractor = FeatureExtractor(arch='VGG')

    # Method to generate predictions
    def generate_similar_images(self):

        # load the numpy weights
        saved_features = np.load("trained_weights/vgg_trained_features.npy")
        saved_index = np.load("trained_weights/vgg_trained_index.npy")

        # Load the data
        listing_data = pd.read_csv('listing_data_with_path.csv')

        '''
        Read the image URL
        '''
        response = requests.get(self.image_url)
        queryImage = Image.open(BytesIO(response.content))

        # Extracting the Features from the queryImage
        queryImage_features = self.feature_extractor.extract_features(queryImage)

        # Compute the distance (similarity) bw the query image and the images in the dataset
        similarity_index = {}
        for i, feat in zip(saved_index, saved_features):

            # Compute the euclidean distance bw the 2 extracted features
            distance = np.sum((queryImage_features - feat) ** 2) ** 0.5
            # print(i )
            similarity_index[i] = distance
            # print(distance)

        # Sort the distances in ascending order and extract the top 10 indexes
        # print(type(similarity_index))
        # print(similarity_index)
        similarity_index_sorted = sorted(similarity_index.items(), key = lambda x : x[1])
        # print(similarity_index_sorted)
        top_8_indexes = [idx for idx, _ in similarity_index_sorted][ : 8]
        scores = [score for _, score in similarity_index_sorted][ : 8]
        # print(scores)
        # Extract the top 10 images
        top_8_images_path = listing_data.iloc[top_8_indexes]['modelImages_path'].values
        top_8_images_desc = listing_data.iloc[top_8_indexes]['shortDescription'].values

        return queryImage, top_8_images_path, top_8_images_desc , scores