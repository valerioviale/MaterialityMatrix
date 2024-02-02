# MaterialityMatrix

A Python program to create a Materiality Matrix based on user input for impact ratings, in a 1 to 9 scale.

## Overview

This Python script utilizes Matplotlib and NumPy to generate a Materiality Matrix, visualizing the impact ratings on both society/environment and business. Users can input their ratings for various topics, and the program creates a scatter plot with bubble sizes and colors representing the total impact.

## Requirements

Make sure you have the following installed:

- Python 3.x
- Matplotlib
- NumPy
- adjustText

You can install the required packages using the following command:

```bash
pip install matplotlib numpy adjustText


git clone https://github.com/valerioviale/MaterialityMatrix.git
cd MaterialityMatrix
```


<img width="1317" alt="MaterialityMatrix" src="https://github.com/valerioviale/MaterialityMatrix/assets/34212301/7c7ab101-71d8-465c-ae26-dc2d75c37176">


Label positioning in a scatter plot like the Materiality Matrix is crucial for clarity and readability. Different techniques can be employed to position labels effectively:

    Random Angle Distribution:
        Randomly distribute labels around each bubble to avoid overlap.
        Use a random angle for each label to make the distribution more even.
        Adjust the angle to evenly space labels around the bubbles.

    Displacement Offset:
        Displace labels horizontally and vertically from the center of each bubble.
        Adjust the offset values to control the positioning of labels.
        This ensures labels do not overlap with the bubbles or each other.

    Adjustment Based on Distance:
        Consider the distance of each label from the origin (0, 0).
        Adjust the position of labels based on their distance to provide a cleaner appearance.
        Labels closer to the center may need more significant adjustments.

    Checking for Overlap:
        Check if labels are too close to any bubble or other labels.
        Adjust the vertical position of labels if they are too close to ensure readability.
        Use a minimum distance threshold to determine if adjustment is needed.

    Line Connection:
        Connect labels to their corresponding bubbles with lines for visual clarity.
        Use dashed lines to differentiate connections from the actual data points.
        This provides a clear link between labels and the data they represent.

    Font Size and Boldness:
        Adjust the font size and boldness of labels for emphasis and readability.
        Larger fonts may be necessary for smaller bubbles or labels that are farther from the origin.
        Bold labels stand out more and can be easier to read.

    Text Adjustment Based on Total Impact:
        Add an offset to the label position based on the total impact of the corresponding data point.
        Larger bubbles might need more significant adjustments to avoid overlap.

    Angle and Rotation:
        Experiment with the angle and rotation of labels for better visual appeal.
        Ensure that labels are easily readable, even when positioned at different angles.
        Rotate labels based on the anchor point to maintain alignment.

These techniques combined help strike a balance between preventing overlap and providing a clear representation of data in the Materiality Matrix. Fine-tuning parameters such as offsets, font sizes, and minimum distances allows for customization based on the specific characteristics of the dataset and visualization requirements.
Actual iteration would benefit from further improvements. A big step has been using adjustText library which works very well when the labels are small.
