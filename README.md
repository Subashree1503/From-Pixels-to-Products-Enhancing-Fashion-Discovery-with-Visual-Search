# From Pixels to Products: Enhancing Fashion Discovery with Visual Search

The modern fashion landscape presents many clothing and accessories, many with intricate designs and unique features that challenge verbal description. Fortunately, the internet offers a vast repository of images displaying these diverse items. This research addresses the difficulty of verbally articulating specific fashion desires by exploring a deep learning-based approach to image similarity search. This innovative system empowers users to locate desired products and accessories simply by providing an image as a reference. By leveraging deep learning techniques, the proposed system can identify visually similar items within the online fashion domain. This not only simplifies the user experience by eliminating the need for precise verbal descriptions but also enhances the discoverability of products and accessories. Consequently, the system creates a mutually beneficial scenario for both users and retailers. To demonstrate the practical application of the proposed approach, a trained deep learning model is deployed on a server. This allows users to experience the ease and effectiveness of image-based fashion search firsthand. This real-world implementation serves as a valuable proof-of-concept and underscores the potential of deep learning to revolutionize the way people interact with the fashion world.


## Dataset

The project utilizes the Farfetch dataset, a comprehensive collection of fashion images curated by Farfetch, a global luxury fashion online platform. The Farfetch dataset comprises a diverse range of fashion items, including clothing, accessories, and footwear, from various luxury brands and designers. The dataset encompasses a wide array of styles, trends, and categories, enabling the development of robust and versatile fashion-related applications and systems. In this project, the Farfetch dataset is leveraged to train and evaluate deep learning models for feature extraction and image similarity comparison. 


## Model Used

The project utilizes pre-trained deep learning models, specifically VGG-16 and ResNet-50, for feature extraction. These models come pre-trained on the ImageNet dataset, a large-scale dataset with millions of labeled images spanning thousands of categories. By leveraging the knowledge learned from ImageNet, VGG-16 and ResNet-50 are adept at extracting high-level features from images, making them well-suited for a variety of computer vision tasks.

In this project, the pre-trained VGG-16 and ResNet-50 models are used to extract features from images in the Farfetch dataset. Despite being pre-trained on ImageNet, these models generalize well to other datasets and domains, including the Farfetch dataset, due to their ability to capture generic visual representations. This enables the project to leverage the rich feature representations learned by VGG-16 and ResNet-50 to facilitate accurate and effective image similarity comparisons within the Farfetch dataset.

By combining the power of pre-trained deep learning models with the Farfetch dataset, the project aims to provide a robust and efficient fashion image search engine tailored to the needs of users, offering accurate and relevant search results for fashion-related queries.



## Usage Instructions

1. Run the following command to start the web-based interface for the image search engine:

```bash
python generator.py
```

2. Access the interface through your web browser.
3. Enter the URL of the image you want to search for in the provided text input field.
4. Click the "Search" button to initiate the search.
5. The system will display the query image and the top similar images found in the dataset.

## File Descriptions

- `config.py`: Configuration file containing paths to dataset files.
- `feature_extractor.py`: Module implementing a feature extraction class using various pre-trained deep learning models.
- `generator.py`: Script for generating the web-based interface of the image search engine.
- `predictions.py`: Module implementing the prediction logic to find similar images based on a query.
- `train.py`: Script for training the deep learning models and extracting features from the dataset.
- `listing_data_with_path.csv`: CSV file containing listing data with image paths.


## Code Flow

- **Data Preparation**: The `train.py` script preprocesses the dataset, extracts image paths, and prepares the data for feature extraction.

- **Feature Extraction**: The `feature_extractor.py` module implements classes to extract features from images using pre-trained models like VGG-16 and ResNet-50.

- **Prediction**: The `predictions.py` module contains the logic to predict similar images based on a query image. It computes the similarity between the query image and images in the dataset using extracted features.

- **Interface Generation**: The `generator.py` script generates a web-based interface for the image search engine using Streamlit. It allows users to input an image URL and displays the query image along with top similar images.




