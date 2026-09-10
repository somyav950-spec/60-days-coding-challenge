# Day 6 – Image Classification using Teachable Machine

## Objective
To create and test an image classification model using Google Teachable Machine.

## Classes
- Class 1: Pen
- Class 2: Bottle

## Dataset
I used image samples of pens and bottles to train the model.

## Training
The model was trained using the uploaded image samples for both classes.

## Testing Results

| Test Image | Prediction |
|------------|------------|
| Clear Pen Image | Pen – 77% |
| Clear Bottle Image | Bottle – 100% |
| Blurred/Noisy Pen Image | Pen – 53%, Bottle – 47% |

## Observations
1. The model identified the clear pen image as Pen with 77% confidence.
2. The model identified the clear bottle image as Bottle with 100% confidence.
3. When a blurred pen image with a busy background was tested, the model became confused and gave Pen 53% and Bottle 47%.

## Conclusion
The model performed well on clear images but became less confident when the input image was blurred and had a complex background. This shows that image quality and background can affect classification accuracy.
