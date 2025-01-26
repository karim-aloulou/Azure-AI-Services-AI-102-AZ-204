import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    load_dotenv()
    endpoint = os.environ["AI_SERVICE_ENDPOINT"]
    key = os.environ["AI_SERVICE_KEY"]
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

# Create an Image Analysis client
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Get a caption for the image. This will be a synchronously (blocking) call.
result = client.analyze_from_url(
    image_url="https://media.gettyimages.com/id/1500448395/fr/photo/cat-taking-a-selfie.jpg?s=612x612&w=gi&k=20&c=v2qzfXZ1HGfdWt0mOG-QqV-5MSEoULSTm1pTmiZtWj8=",
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ,VisualFeatures.TAGS],
    gender_neutral_caption=True,  # Optional (default is False)
)
""" We can use all these features
VisualFeatures.TAGS: Identifies tags about the image, including objects, scenery, setting, and actions
VisualFeatures.OBJECTS: Returns the bounding box for each detected object
VisualFeatures.CAPTION: Generates a caption of the image in natural language
VisualFeatures.DENSE_CAPTIONS: Generates more detailed captions for the objects detected
VisualFeatures.PEOPLE: Returns the bounding box for detected people
VisualFeatures.SMART_CROPS: Returns the bounding box of the specified aspect ratio for the area of interest
VisualFeatures.READ: Extracts readable text"""

print("Image analysis results:")
# Print caption results to the console
print(" Caption:")
if result.caption is not None:
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")
print(" Tags:")
if result.tags is not None:
    print(f"   '{result.tags}'")
# Print text (OCR) analysis results to the console
print(" Read:")
if result.read is not None:
    for line in result.read.blocks[0].lines:
        print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
        for word in line.words:
            print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")