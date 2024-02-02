import matplotlib.pyplot as plt
import numpy as np
from adjustText import adjust_text

# You should use *1* for production and 2 to test the plotting
# *1* main Function to get user input for impact ratings
# def get_user_ratings(topics):
#     ratings = {}

#     for topic in topics:
#         impact_on_society = int(input(f"Enter the impact on society rating (1-9) for '{topic}': "))
#         impact_on_business = int(input(f"Enter the impact on business rating (1-9) for '{topic}': "))

#         ratings[topic] = {
#             "impact_on_society": impact_on_society,
#             "impact_on_business": impact_on_business
#         }

#     return ratings

# *2* alternative Function to get random impact ratings for testing, comment when you activate *1*
def get_user_ratings(topics):
    ratings = {}

    for topic in topics:
        impact_on_society = np.random.randint(1, 10)
        impact_on_business = np.random.randint(1, 10)

        ratings[topic] = {
            "impact_on_society": impact_on_society,
            "impact_on_business": impact_on_business
        }

    return ratings

# Function to check if two points are too close
def is_too_close(x1, y1, x2, y2, min_distance):
    distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance < min_distance

# Mock data
topics = [
    "Economic Performance", "Market Presence", "Indirect Economic Impacts",
    "Anti-corruption", "Materials", "Energy", "Biodiversity", "Water",
    "Emissions", "Products & Services", "Waste", "Compliance",
    "Labor Practices", "Human Rights", "Society", "Product Responsibility",
    "Resp. Mineral Sourcing", "Governance Structure", "Remuneration",
    "Stakeholder Engagement", "Business Ethics"
]


# Set the font for the labels
font_properties = {'family': 'arial', 'weight': 'normal'}

# Get user ratings
user_ratings = get_user_ratings(topics) # change with get_user_ratings for production

# Extract user ratings into separate lists
impact_on_society = [user_ratings[topic]["impact_on_society"] for topic in topics]
impact_on_business = [user_ratings[topic]["impact_on_business"] for topic in topics]

# Calculate total impact and convert to a NumPy array
total_impact = [sum(pair) for pair in zip(impact_on_society, impact_on_business)]
total_impact_np = np.array(total_impact)

# Scale the size of bubbles based on Total Impact
scaled_size = total_impact_np * 10  # Adjusted scaling factor for larger bubbles

# Create a color map based on total impact values
color_map_name = plt.cm.get_cmap('viridis')
normalized_total_impact = (total_impact_np - np.min(total_impact_np)) / (np.max(total_impact_np) - np.min(total_impact_np))
bubble_colors = color_map_name(normalized_total_impact)

# Create a scatter plot with bubble size and colors
plt.figure(figsize=(10, 7))  # Adjusted figsize for more space
scatter = plt.scatter(impact_on_business, impact_on_society, s=scaled_size, c=bubble_colors, alpha=0.6, edgecolors='grey')

# Add a colorbar to show the scale of colors
cbar = plt.colorbar(scatter, ticks=[0, 0.5, 1],  cmap=color_map_name)
cbar.set_label('Total Impact= (Society*Environment)+Business')

# Add labels for each point above the bubbles
texts = []
min_distance = 3  # Adjust this value based on your preference
label_fontsize = 6  # Adjust this value based on your preference

# Calculate the distance of each point from the origin
distances = np.sqrt(np.square(impact_on_business) + np.square(impact_on_society))


# Adjust xytext based on random angles
for i, topic in enumerate(topics):
    # Adjust xytext to displace text horizontally and vertically
    text_offset = (0, 0)  # Adjust these values based on your preference
    
    # Random angle to distribute labels evenly around each bubble
    angle = np.random.uniform(0, 2*np.pi)
    
    # Adjust xytext based on the random angle
    text_x = impact_on_business[i] + text_offset[0] * np.cos(angle)
    text_y = impact_on_society[i] + text_offset[1] * np.sin(angle)
    
    text = plt.text(text_x, text_y, topic,
                    ha='center', va='center', fontsize=label_fontsize,
                    fontweight='bold',
                    rotation=0, rotation_mode='anchor',
                    transform=plt.gca().transData)  # Use data coordinates


    # Add an offset to the label based on the distance from the origin
    offset_x = 0.3  # Adjust this value based on your preference
    offset_y = 0.3
    text.set_position((text.get_position()[0] + offset_x, text.get_position()[1] + offset_y))

    # Check if the text is too close to any bubble, and if so, adjust its position
    for j in range(i):
        if is_too_close(impact_on_business[i], impact_on_society[i], impact_on_business[j], impact_on_society[j], min_distance):
            text.set_position((text.get_position()[0], text.get_position()[1] + 0.1))  # Adjust the vertical position

    texts.append(text)
    # Create lines connecting labels to bubbles
    plt.plot([impact_on_business[i], text.get_position()[0]], [impact_on_society[i], text.get_position()[1]], color='lightgreen', linestyle='--', linewidth=1.2)



    
# Add labels and title
plt.xlabel('Impact on Business')
plt.ylabel('Impact on Society/Environment')

# Increase y-axis limit to add space at the top
plt.ylim(0, max(impact_on_society) + 3)  # Adjusted ylim for more space

# Draw a blue cross in the exact middle of the chart
midpoint_x = (max(impact_on_business) + min(impact_on_business)) / 2
midpoint_y = (max(impact_on_society) + min(impact_on_society)) / 2
plt.axvline(x=midpoint_x, color='blue', linestyle='--', linewidth=0.7)
plt.axhline(y=midpoint_y, color='blue', linestyle='--', linewidth=0.7)

plt.title('Materiality Matrix')


# Show the plot
plt.grid(True)
plt.show()

