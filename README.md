# Finding the Best Family Hiking Trail - Columbia River Gorge Area

# Team Members
Anya Bocharova,
Eduardo Camacho,
Riley Hutchinson,
Katrina Rodriguez

# Project Overview and Questions
This project is an analysis of Hiking Trails near the Columbia River Gorge Region in the Pacific Northwest based on location, family-friendly rating, number of hazards, distance and elevation. These are the questions we used to create our data analysis and visualizations:

    • What trails in the Columbia River Gorge region are the best suited for families and pets?
        ○ Where are the different trails located? 
        ○ What types of trail hazards are found each trail?
        ○ What is relationship between the distance and elevation for each trail?

On our dashboard you will find the following:

# Columbia River Gorge Trail Map
This is a detailed map of the Columbia River Gorge area with visual markers of the geocode locations for the start of each trail in our dataset of hiking trails. The markers are colored based on the diffuclty rating for each trail with red for Diffcult, orange for Moderate, and green for Easy. The map also includes a filter box for multiple Trail Filters that users can use to narrow dowm trails based on trail name, difficulty, distance, and family friendly rating. This map was created using data from the file under the folders resources>cleaned data>all_trails_cleaned_df and the leaflet library for JS. Javascript, HTML, and CSS coding for this map can be found in the index.html file. 

![image](https://github.com/user-attachments/assets/39fa4ba9-5c73-4c34-8db7-1d6587738af9)

# Nature Bites Back: Ranking Common Hiking Hazards
Four common hazards found amongst most trails (Rattlesnakes, Ticks, Poison Ivy, and Falling) are included in the data details for the list of trails for the Columbia River Gorge region. This data was cleaned and used to create a bar chart that details the number of trails for each type of hazard. A lable with the trail count displays when the user hovers each column. A filter was added to the chart for allowing users to select a specific trail name and update the number of hazards based on the trail data. With this data we found Poison Ivy to be the most common trail hazard with 44 trails and Falling the least common trail hazard at 0. The code for this visualization was created using two new libraries Papaparse.min.js and Chart.js, to read and chart the data found in resources>cleaned_data>hazards_data_clean_df.csv.

![image](https://github.com/user-attachments/assets/d60a637c-849f-484c-bfe5-96170151c5ea)

# Climbing the Data: The Relationship Between Elevation and Distance
In this visualization, a scatterplot was used to chart the relationship between the distance and elevation of each trail. This data can be used in relation to the hazard and map visualization to narrow down the best suited trail based on the user's distance and elevation needs. The majority of trails from our dataset were found to fall under the  miles mark for distance and under 1500 feet of elevation. A lable with the trail name for each plot generates when a user hovers over a specific plot point. A colored heatmap was also used to display the gradual change as plot points increased in elevation. The code for this viuslization was created using mostly Javascript and a new library Papaparse.min.js to create the visualization and read the data found in resources>cleaned_data>Family_data_ElevationVsDistance.csv.

![image](https://github.com/user-attachments/assets/bb9ef5fd-0e53-4643-934e-31e8e71aa777)

# Tech Stack
	• Python
	• Jupyter Notebook
	• MongoDB
	• HTML
	• CSS
	• JavaScript
	• Pandas
 	• Plotly
	• Leaflet.js
	• PapaParse.js
	• Chart.js
   	• trailsData.js
       
# Resources

    • Website Resources
        ○ Outdoor Recreation/Hiking Trails: https://www.kaggle.com/datasets/chuckh193333/hiking-trails-columbia-river-gorge 
		○ HTML/CSS coding help: https://developer.mozilla.org/en-US/
        ○ Leaflet Library: https://unpkg.com/leaflet@1.7.1/dist/leaflet.js
		○ PapaParse Library: https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js
 		○ Plotly Library: https://cdn.plot.ly/plotly-latest.min.js
        ○ Chart Library: https://cdn.jsdelivr.net/npm/chart.js
	
• Additional Support from our tutors, teacher, teaching assistants, Copilot and Claude (for coding corrections and error guidance).

# Considerations


Our team acknowledges several important data ethics considerations for this project:

1. Data Collection Bias: The trail data was sourced from user-contributed information and we have found inaccuracies in the data provided. We did our best to manually correct the geo data to more accurately reflect the correct location of trails.

2. Accessibility Representation: Our "family-friendly" classification is subjective and may not adequately represent the needs of all families, particularly those with members who have different mobility requirements or accessibility needs. While we include elevation and distance metrics, other important accessibility factors might not be captured in our dataset.

3. Hazard Reporting Limitations: The hazard data (rattlesnakes, ticks, poison ivy, falling) relies on reported incidents and may not reflect the actual risk levels. Some hazards might be underreported in less frequented trails or overreported in more popular ones. Additionally, the binary nature of our hazard indicators (present/not present) doesn't capture the severity or seasonality of these risks.

4. Geographic and Temporal Limitations: Our dataset focuses specifically on the Columbia River Gorge region and may not be representative of other hiking areas. Additionally, trail conditions can change seasonally and over time, so the accuracy of the data may vary depending on when it was last updated.

5. Cultural Considerations: Some trails in our dataset may have cultural or historical significance to local Indigenous communities. While we provide location data and trail descriptions, we acknowledge that this information should be used respectfully and in accordance with any local guidelines or restrictions.

These considerations should be kept in mind when using our dashboard for trail selection and planning purposes.

# Instructions
