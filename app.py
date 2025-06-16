
# python script for Disease Prediction Web App

## import Libraries
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
import pickle


## load the saved model
diabetic_model = pickle.load(open('diabetes_model.sav', 'rb'))
cancer_model = pickle.load( open('cancer_model.sav', 'rb'))
parkinson_model = pickle.load( open('parkinson_model.sav', 'rb'))
heart_model = pickle.load( open('heart_model.sav', 'rb'))


with st.sidebar:

	st.image("logo.png", width=120)
	selected = option_menu('Multiple Disease Prediction System',

		['Diabetes Prediction', 'Breast Cancer Prediction', 'Parkinson Disease Prediction', 'Heart Disease Prediction', 'About the developer'],

		icons = ['person-arms-up', 'lungs', 'headset-vr', 'heart-pulse', 'person-gear'],

		default_index = 0)


if (selected == 'Diabetes Prediction'):

	# give title 
	st.title("Diabetes Prediction Using Machine Learning 🩺")

	# give subheader
	st.header("Introduction")

	st.markdown("---")

	st.markdown("Diabetes is a chronic metabolic disorder characterized by elevated levels of blood glucose, which can lead to serious damage to the heart, blood vessels, eyes, kidneys, and nerves over time. Early detection and management of diabetes play a crucial role in preventing long-term health complications.")
	st.markdown("This Diabetes Prediction System utilizes a machine learning model trained on medical and diagnostic data to assess whether an individual is likely to be diabetic based on key health indicators. The system provides a quick, accessible, and reliable prediction to assist healthcare decisions and personal awareness.")
	st.markdown("---")
	
	st.subheader("Feature Used in Prediction")

	st.markdown("""
		- Pregnancies — Number of times pregnant

		- Glucose — Plasma glucose concentration

		- Blood Pressure — Diastolic blood pressure (mm Hg)

		- Skin Thickness — Triceps skinfold thickness (mm)

		- Insulin — Serum insulin (mu U/ml)

		- BMI — Body Mass Index (kg/m²)

		- Diabetes Pedigree Function — Genetic risk score for diabetes

		- Age — Patient’s age (years)


		""")

	st.divider()

	st.caption("⚠️ Disclaimer: This prediction is based on statistical models and should not replace professional medical advice. Consult healthcare professionals for official diagnosis and treatment.")

	# create columns
	col1, col2, col3 = st.columns(3)

	with col1:
		pregnancies = st.text_input("Number of Pregnancies")
	with col2:
		glucose = st.text_input("Blood Glucose Level")
	with col3:
		bloodpressure = st.text_input("Blood Pressure Level")
	with col1:	
		skinthickness = st.text_input("Skin Thickness")
	with col2:	
		insulin = st.text_input("Insulin Level")
	with col3:
		bmi = st.text_input("Body Mass Index (BMI)")
	with col1:	
		diabetespedigreefunction = st.text_input("Diabetes Pedigree Function (DPF)")
	with col2:
		age = st.text_input("Enter Age")

	diabetes = ''
	
	if st.button("Predict Diabetes"):
		prediction = diabetic_model.predict([[pregnancies,glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])

		if (prediction[0] == 0):
			diabetes = "The Person is Diagnosized as Non-Diabetic"
		else:
			diabetes = "The Person is Diagnosized as Diabetic"

	st.success(diabetes)

	st.divider()
	st.caption("🔗 Learn more about diabetes: [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/diabetes)")



if (selected == 'Breast Cancer Prediction'):

	# give title 
	st.title("Breast Cancer Prediction Using Machine Learning 🩺")

	# give contents
	st.header("Introduction")

	st.divider()

	st.markdown("Breast cancer is one of the most common cancers affecting women globally. Early diagnosis significantly increases the chances of successful treatment and survival. However, distinguishing between benign (non-cancerous) and malignant (cancerous) tumors based solely on physical examination or imaging can be challenging.")

	st.markdown("This Breast Cancer Prediction System leverages machine learning algorithms trained on clinical diagnostic data to predict whether a tumor is likely to be benign or malignant. By analyzing tumor characteristics, the model provides a fast and reliable assessment to assist in early diagnosis and treatment decisions.")
	st.divider()

	
	st.subheader("Feature used in Prediction")
	
	st.markdown("These features describe cell nuclei characteristics derived from digitized images of fine needle aspirate (FNA) of a breast mass.")

	st.markdown("""

				| **Feature**                        | **Description**                                                         |
		| ---------------------------------- | ----------------------------------------------------------------------- |
		| **Radius (mean/worst)**            | Mean of distances from center to points on the perimeter of the nucleus |
		| **Texture (mean/worst)**           | Variation in gray-scale intensity (image texture)                       |
		| **Perimeter (mean/worst)**         | Perimeter length of the cell nucleus                                    |
		| **Area (mean/worst)**              | Area size of the nucleus                                                |
		| **Smoothness (mean/worst)**        | Local variation in radius lengths (smooth vs. rough)                    |
		| **Compactness (mean/worst)**       | Perimeter² / Area - 1.0 (compactness of shape)                          |
		| **Concavity (mean/worst)**         | Severity of concave portions of the contour                             |
		| **Concave Points (mean/worst)**    | Number of concave portions of the contour                               |
		| **Symmetry (mean/worst)**          | Symmetry of the cell nucleus shape                                      |
		| **Fractal Dimension (mean/worst)** | Complexity of the nucleus boundary curve                                |



		""")

	st.divider()
	st.caption("⚠️ Disclaimer: This prediction is for educational purposes and should not be used as a substitute for professional medical diagnosis.")

	# create columns
	col1 , col2, col3 = st.columns(3)

	
	with col1:
		radius_mean = st.text_input("Radius Mean value")
	with col2:
		texture_mean = st.text_input("Texture Mean value")
	with col3:
		perimeter_mean = st.text_input("Perimeter Mean value")
	with col1:	
		area_mean = st.text_input("Area Mean value")
	with col2:	
		smoothness_mean = st.text_input("Smoothness Mean value")
	with col3:
		compactness_mean = st.text_input("Compactness Mean value")
	with col1:	
		concavity_mean = st.text_input("Concavity Mean value")
	with col2:
		concave_points_mean = st.text_input("Concave Points Mean value")
	with col3:
		symmetry_mean = st.text_input("Symmetry Mean value")
	with col1:
		fractal_dimension_mean = st.text_input("Fractal Dimension Mean value")
	
	with col2:
		radius_worst = st.text_input("Radius worst value")
	with col3:
		texture_worst = st.text_input("Texture Worst value")
	with col1:
		perimeter_worst = st.text_input("Perimeter Worst value")
	with col2:	
		area_worst = st.text_input("Area Worst value")
	with col3:	
		smoothness_worst = st.text_input("Smoothness Worst value")
	with col1:
		compactness_worst = st.text_input("Compactness Worst value")
	with col2:	
		concavity_worst = st.text_input("Concavity Worst value")
	with col3:
		concave_points_worst = st.text_input("Concave Points Worst value")
	with col1:
		symmetry_worst = st.text_input("Symmetry Worst value")
	with col2:
		fractal_dimension_worst = st.text_input("Fractal Dimension Worst value")
	
	# create a predictive system

	cancer = ''

	if st.button("Predict Breast Cancer"):
		prediction = cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])

		if prediction[0]=="B":
			cancer = "Diagnosized as Benign Cancer"
		else:
			cancer = "Diagnosized as Malignant Cancer"

	st.success(cancer)
	
	st.caption("🔗 Learn more: [Breast Cancer - WHO](https://www.who.int/news-room/fact-sheets/detail/breast-cancer)")


if (selected == 'Parkinson Disease Prediction'):

	# give title 
	st.title("Parkinson Disease Prediction Using Machine Learning 🩺")

	# give header
	st.header("Introduction")
	st.divider()

	st.markdown("Parkinson’s disease is a progressive neurological disorder that primarily affects movement, balance, and coordination. One of the earliest and most common symptoms of Parkinson’s is a change in voice quality, including tremors, reduced volume, and hoarseness. Detecting Parkinson’s early allows for timely interventions, slowing progression and improving the quality of life.")
	st.markdown("This Parkinson Disease Prediction System uses machine learning models trained on acoustic voice measurements to predict whether an individual may be affected by Parkinson’s. By analyzing subtle changes in voice parameters, this tool provides an accessible, non-invasive assessment to assist in early detection.")
	st.divider()

	st.subheader("Feature Used in the Prediction")
	st.markdown("""

		- 🎙️ MDVP:Fo(Hz) → Average fundamental frequency of the voice (pitch)

		- 🎙️ MDVP:Fhi(Hz) → Maximum fundamental frequency during speech

		- 🎙️ MDVP:Flo(Hz) → Minimum fundamental frequency during speech

		- 🎙️ MDVP:Jitter(%) & Jitter(Abs) → Variability in frequency (voice instability)

		- 🎙️ MDVP:RAP, PPQ, DDP → Refined and relative measures of pitch variation	

		- 🎙️ MDVP:Shimmer & Shimmer(dB) → Variability in amplitude (loudness instability)

		- 🎙️ Shimmer:APQ3, APQ5, APQ, DDA → Additional detailed measures of amplitude variation

		- 🎙️ NHR (Noise-to-Harmonics Ratio) → Ratio of noise to tonal components in voice

		- 🎙️ HNR (Harmonics-to-Noise Ratio) → Ratio of tonal sound to noise (higher = healthier voice)

		- 🌀 RPDE (Recurrence Period Density Entropy) → Complexity measure of the vocal fold signal

		- 📈 DFA (Detrended Fluctuation Analysis) → Indicates the presence of long-term correlation in voice

		- 📉 Spread1 & Spread2 → Nonlinear signal dynamics features

		- 🎛️ D2 (Correlation Dimension) → Complexity measure of the voice signal

		- 🎚️ PPE (Pitch Period Entropy) → Irregularity of pitch periods



		""")

	st.divider()

	st.caption("⚠️ Disclaimer: This prediction is for educational purposes and should not be used as a substitute for professional medical diagnosis.")

	# create columns
	col1, col2, col3 = st.columns(3)

	with col1:
		fo = st.text_input("MDVP Fo(Hz) value")
	with col2:
		fhi = st.text_input("MDVP Fhi(Hz) value")
	with col3:
		flo = st.text_input("MDVP Flo(Hz) value")
	with col1:	
		jitter_perc = st.text_input("MDVP Jitter(%) value")
	with col2:	
		jitter_abs = st.text_input("MDVP Jitter(Abs) value")
	with col3:
		rap = st.text_input("MDVP RAP value")
	with col1:	
		ppq = st.text_input("MDVP PPQ value")
	with col2:
		ddp = st.text_input("Jitter DDP value")
	with col3:
		shimmer = st.text_input("MDVP Shimmer value")
	with col1:
		shimmer_db = st.text_input("MDVP shimmer(dB) value")
	with col2:
		apq3 = st.text_input("Shimmer APQ3")
	with col3:
		apq5 = st.text_input("Shimmer APQ5")
	with col1:
		apq = st.text_input("MDVP APQ")
	with col2:	
		dda = st.text_input("Shimmer DDA")
	with col3:	
		nhr = st.text_input("NHR value")
	with col1:
		hnr = st.text_input("HNR value")
	with col2:	
		rpde = st.text_input("RPDE value")
	with col3:
		dfa = st.text_input("DFA value")
	with col1:
		spread1 = st.text_input("Spread1 value")
	with col2:
		spread2 = st.text_input("Spread2 value")
	with col3:
		d2 = st.text_input("D2 value")
	with col1:
		ppe = st.text_input("PPE value")

	# create predictive system
	parkinson = ''

	if st.button("Predict Parkinson Disease"):
		prediction = parkinson_model.predict([[fo, fhi, flo, jitter_perc, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])

		if prediction[0] == 0:
			parkinson = "The person does not have Parkinson disease"
		else:
			parkinson = "The person has Parkinson Disease"

		st.success(parkinson)

	st.caption("🔗 Learn more: [Breast Cancer - WHO](https://www.who.int/news-room/fact-sheets/detail/breast-cancer)")



if (selected == 'Heart Disease Prediction'):

	# give title 
	st.title("Heart Disease Prediction Using Machine Learning 🩺")

	# give header
	st.header("Introduction")
	st.divider()

	st.markdown("Heart disease remains one of the leading causes of death worldwide. Early detection is crucial for preventing life-threatening events such as heart attacks or strokes. Several clinical indicators, including blood pressure, cholesterol levels, and chest pain types, are used to assess an individual’s risk of developing heart disease.")
	st.markdown("This Heart Disease Prediction System utilizes a machine learning model trained on comprehensive cardiovascular health data to predict the likelihood of heart disease. By analyzing key health metrics, this tool provides a quick, accessible, and supportive assessment to assist individuals and healthcare professionals in making informed health decisions.")
	st.divider()

	st.subheader("Feature Used in the Prediction")
	st.markdown("""
		- Age → Patient’s age in years

		- Sex → 1 = Male, 0 = Female

		- cp (Chest Pain Type)

			- 0 = Typical Angina (heart-related)

			- 1 = Atypical Angina

			- 2= Non-anginal Pain

			- 3 = Asymptomatic (most serious)

		- trestbps (Resting Blood Pressure) → Measured in mm Hg

		- chol (Serum Cholesterol) → Total cholesterol in mg/dL

		- fbs (Fasting Blood Sugar > 120 mg/dL) → 1 = True, 0 = False

		- restecg (Resting Electrocardiogram Results)

			- 0 = Normal

			- 1 = ST-T wave abnormality (possible ischemia)

			- 2 = Left Ventricular Hypertrophy

		- thalach (Maximum Heart Rate Achieved) → Beats per minute

		- exang (Exercise-Induced Angina) → 1 = Yes, 0 = No

		- oldpeak (ST Depression) → Depression induced by exercise relative to rest

		- slope (Slope of the Peak Exercise ST Segment)

			- 0 = Upsloping

			- 1 = Flat

			- 2 = Downsloping

		- ca (Number of Major Vessels Colored by Fluoroscopy) → 0 to 3

		- thal (Thalassemia Test Result)

			- 1 = Normal

			- 2 = Fixed Defect

			- 3 = Reversible Defect




		""")
	st.divider()

	st.caption("⚠️ Disclaimer: This prediction is for educational purposes and should not be used as a substitute for professional medical diagnosis.")
	

	# create columns
	col1, col2, col3 = st.columns(3)

	

	with col1:
		age = st.text_input("Enter Age")
	with col2:
		cp = st.text_input("Enter Chest Pain type")
	with col3:
		trestbps = st.text_input("Resting Blood Pressure value")
	with col1:	
		chol = st.text_input("Serum Cholestrol Level")
	with col2:	
		fbs = st.text_input("Fasting Blood Sugar level")
	with col3:
		restecg = st.text_input("Resting ECG value")
	with col1:	
		thalach = st.text_input("Maximum Heart Rate achieved value")
	with col2:
		exang = st.text_input("Exercise Induced Angina Value")
	with col3:
		oldpeak = st.text_input("Old Peak Value")
	with col1:
		slope = st.text_input("Slope Value")
	with col2:
		ca = st.text_input("No. of Major Vessels Coloured (ca)")
	with col3:
		thal = st.text_input("Thalassemia type")

	# create predictive system
	heart_disease = ''

	if st.button("Predict Heart Disease"):
		prediction = heart_model.predict([[float(age), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]])

		if prediction[0] == 0:
			heart_disease = "The Heart is in Healthier Condition"
		else :
			heart_disease = "Propable chance of Heart Disease is confirmed"

	st.success(heart_disease)

	st.caption("🔗 Learn more about heart disease: [World Heart Federation](https://world-heart-federation.org/)")


if (selected=="About the developer"):
	# give title
	st.title("About the Developer👨🏽‍💻")
	st.divider()

	st.markdown("I am **Karthik**, a passionate biotechnology graduate from SRM University. With a strong foundation in life sciences, I have developed a deep interest in integrating biological research with computational tools. My key areas of interest include bioinformatics, data analysis, and machine learning applications in healthcare. Over the past year, I have been working on projects involving gene expression analysis, disease prediction systems, and data-driven biological research. I am skilled in Python, R programming, and data visualization, and I am committed to using computational approaches to solve complex biological challenges. My goal is to contribute meaningfully to the field of bio-IT by developing innovative solutions that bridge the gap between biology and technology.")
	st.divider()

	st.header("Contact")
	st.markdown("""
		- [📧Mail id : karthikyoganantham@gmail.com](karthikyoganantham@gmail.com)
		- 📞**Mobile** : +91 93841 42469
		- [Connect with me on Linkedin](https://www.linkedin.com/in/karthik-yoganantham/) 
		- [Github page](https://github.com/KARTHIK-YOGANANTHAM)

		""")

	st.subheader("For more details:👇🏻")
	st.markdown("**[visit my Portfolio👇🏻](https://karthikyoganantham.framer.website/)**")












