<div align="left" style="margin-bottom: 40px; display: flex; align-items: center; gap: 10px;">
  <img src="images/UM_Logo.png" alt="Unified Mentors Private Limited" height="40px">
  <span style="font-size: 15px; font-weight: 500; color: #7e7e7eff;">Unified Mentors Private Limited</span>
</div>


<!-- Image Logo -->
<div align="center">
    <img src="images/FCP_Banner.png" alt="" width="400" height="235" style="border-radius: 18px;">
</div>
<br>

<!-- project and ML title -->
<h1 align='center' style="margin-bottom: 0px;">
<!-- <a href="https://git.io/typing-svg"> -->
  <img src="https://readme-typing-svg.herokuapp.com?font=Playfair+Display&weight=500&size=25&duration=5500&pause=1000&color=00FFFF&center=true&random=false&width=600&lines=Forest+Cover+Prediction" alt="Typing SVG" />
</a></h1>

<!-- ML name -->
<h4 align='center' style="margin-top: 0; margin-bottom: 10px;">
<!-- <a href="https://git.io/typing-svg"> -->
  <img src="https://readme-typing-svg.herokuapp.com?font=Playfair+Display&weight=100&size=15&duration=5500&pause=1000&color=0FFFFF&center=true&random=false&width=600&lines=Machine+Learning+Project" alt="Typing SVG" />
</a></h4>



---
<br>
<!-- Table of content -->
## Table of Contant

* <p style="font-size:14px;">About this Project.</p>
* <p style="font-size:14px;">Problem Statment.</p>
* <p style="font-size:14px;">What DataSet cointains?</p>
* <p style="font-size:14px;">Main library to be used.</p>
* <p style="font-size:14px;">Visualizations/Chart.</p>
* <p style="font-size:14px;">Conclusion.</p>
* <p style="font-size:14px;">Acknowledgment.</p>
<br>

---
<!-- About this Project -->
<br><br>
## About this Project:
<p style="font-size:15px;">
    This project, completed under Unified Mentors Private Limited, focuses on predicting forest cover types using environmental and geographical data to support land management and conservation. Using a dataset of 15,120 records with 56 features such as Elevation, Slope, Aspect, and Hillshade, the study built and compared multiple machine learning models. After analysis and feature evaluation, Random Forest emerged as the best performer, accurately classifying seven forest types and highlighting key environmental predictors that influence forest distribution.
    <br><br>
</p>

---
<br><br>
## Problem Statement:

- Can we accurately predict the type of forest cover in a given area solely based on its geographical and environmental characteristics?<br>
- Which specific environmental factors (like elevation, slope, or proximity to water and roads) are the most influential in determining the dominant forest type?<br>
- How can we leverage machine learning to build a robust model that distinguishes between seven distinct forest cover classes?<br>
- What are the implications of accurate forest cover prediction for sustainable land management, conservation efforts, and understanding ecological patterns?<br>
- Can a predictive model help in identifying areas vulnerable to changes in forest composition due to environmental shifts or human activity?<br>
<br><br>
---
<br><br>
<!-- What Data set Containes -->
<!-- columns and their descriptions -->
<details open>
    <summary style="font-size: 20px; text-align: center;">
    What Data Set Contains?
</summary>
<br>
<p style="font-size:16px; test-align: left;">
1. Elevation - Elevation in meters.<br><br>
2. Aspect - Aspect in degrees azimuth.<br><br>
3. Slope - Slope in degrees.<br><br>
4. Horizontal_Distance_to_Hydrology - Horz Dist to nearest surface water features.<br><br>
5. Vertical_Distance_to_Hydrology: FroVert Dist to nearest surface water features.<br><br>
6. Horizontal_Distance_To_Roadways - Horz Dist to nearest roadway.<br><br>
7. Hillshade_9am (0 to 255 index) - Hillshade index at 9am, summer solstice.<br><br>
8. Hillshade_Noon (0 to 255 index) - Hillshade index at noon, summer solstice.<br><br>
9. Hillshade_3pm (0 to 255 index) - Hillshade index at 3pm, summer solstice.<br><br>
10. Horizontal_Distance_To_Fire_Points - Horz Dist to nearest wildfire ignition points.<br><br>
11. Wilderness_Area (4 binary columns, 0 = absence or 1 = presence) - Wilderness area designation.<br><br>
12. Soil_Type (40 binary columns, 0 = absence or 1 = presence) - Soil Type designation.<br><br>
13. Cover_Type - Forest Cover Type designation.<br><br>
=> Integer Classification of the forest cover types:<br>
|- 1 - Spruce/Fir..<br>
|- 2 - Lodgepole Pine.<br>
|- 3 - Ponderosa Pine.<br>
|- 4 - Cottonwood/Willow..<br>
|- 5 - Aspen.<br>
|- 6 - Douglas-fir.<br>
|- 7 - Krummholz.<br>
</p>
</details>
<br><br>

---
<br><br>
<!-- Library used in projects and their description -->
<details open> 
  <summary style="font-size: 20px; text-align:center;"> Main Libraries Used </summary> 
  <br> 
  <p style="font-size:16px;">
  🔢 <b>NumPy</b> – For numerical computations and efficient array manipulation.<br>
  📊 <b>Pandas</b> – To load, clean, and analyze structured datasets.<br>
  📈 <b>Matplotlib & Seaborn</b> – For creating visualizations that explore data distributions, correlations, and feature relationships.<br>
  🧪 <b>SciPy</b> – Used for statistical analysis and hypothesis testing.<br>
  ⚙️ <b>scikit-learn (sklearn)</b> – Core machine learning framework used for:
  <ul> 
    <li>Data preprocessing (<code>StandardScaler</code>, <code>LabelEncoder</code>)</li> 
    <li>Model training and evaluation (<code>DecisionTreeClassifier</code>, <code>RandomForestClassifier</code>, <code>GradientBoostingClassifier</code>)</li> 
    <li>Performance metrics (<code>accuracy_score</code>, <code>precision_score</code>, <code>recall_score</code>, <code>f1_score</code>, <code>confusion_matrix</code>, <code>classification_report</code>)</li> 
    <li>Model validation (<code>train_test_split</code>, <code>cross_val_score</code>)</li>
  </ul>
  🚀 <b>XGBoost & LightGBM</b> – Advanced gradient boosting frameworks used for improving model accuracy and speed.<br>
  🚫 <b>Warnings</b> – To suppress unnecessary warning messages for cleaner notebook outputs.<br>
  </p> 
</details>
<br><br>


---
<br><br>
<details open>
<summary style="font-size: 20px; text-align:center;"> Visualizations/Chart. </summary>
<p align="center">
    <img src="images/Chart1.png" alt="Insights Visualization 1" width="400" style="border-radius: 20px; margin: 10px;">
    <img src="images/Chart4.png" alt="Insights Visualization 2" width="400" style="border-radius: 20px; margin: 10px;">
    <img src="images/Chart9.png" alt="Insights Visualization 3" width="400" style="border-radius: 20px; margin: 10px;">
    <img src="images/Chart10-1.png" alt="Insights Visualization 3" width="400" style="border-radius: 20px; margin: 10px;">
    <img src="images/Chart10-2.png" alt="Insights Visualization 3" width="400" height="160" style="border-radius: 20px; margin: 10px;">
    <img src="images/ML_Comparision.png" alt="Insights Visualization 3" width="400" style="border-radius: 20px; margin: 10px;">
    <img src="images/BestModel.png" alt="Insights Visualization 3" width="400" style="border-radius: 20px; margin: 10px;">
    <img src="images/ConfusionMatric.png" alt="Insights Visualization 3" width="400" style="border-radius: 20px; margin: 10px;">
    
</p>

---
<br><br>
## Conclusion:
<p style="font-size:16px;">
The analysis of the forest cover prediction dataset revealed that the data was clean and well-structured, though slightly imbalanced across cover types. Exploratory analysis showed **Elevation** as the strongest predictor, with features like Slope, Aspect, Hillshade, and distances to hydrology and roads also influencing forest types. Correlation and visualization plots highlighted meaningful feature relationships. Several models were tested, and among them, **Random Forest** achieved the best accuracy, outperforming Decision Tree and performing competitively with Gradient Boosting, XGBoost, and LightGBM. The model was saved, reloaded, and validated successfully, proving reliable for prediction. Overall, the project identified key environmental factors affecting forest cover and demonstrated the effectiveness of machine learning—especially Random Forest—for ecological analysis and land management insights.
</p>
<br><br>

---
<br><br>
### Acknowledgments:
<p style="font-size: 11px;">
This project is dedicated to applying machine learning techniques to understand and predict forest cover types, contributing to sustainable land and resource management. Sincere thanks to Unified Mentors Private Limited for providing the opportunity and platform to carry out this work. Appreciation is also extended to the open-source community for developing the powerful tools and libraries that made this project possible.
</p>
<p align="right" > Created with 🧠 by <a href="https://github.com/KushangShah">Kushang Shah</a></p>
<p align="right"> <img src="https://komarev.com/ghpvc/?username=kushang&label=Profile%20views&color=0e75b6&style=flat" alt="kushang" /> </p>