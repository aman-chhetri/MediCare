import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('/Users/Nitro/Desktop/MediCare/model/diabetes_model.pkl', 'rb'))

heart_disease_model = pickle.load(open('/Users/Nitro/Desktop/MediCare/model/heart_disease_model.pkl','rb'))

parkinsons_model = pickle.load(open('/Users/Nitro/Desktop/MediCare/model/parkinsons_model.pkl', 'rb'))


# sidebar for navigation2
with st.sidebar:
    
    selected = option_menu('MediCare⚕️ - Multiple Disease Prediction System 🔍',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

st.sidebar.caption(
    '**This is a machine learning web application built using Streamlit that predicts whether or `not` a patient has `diabetes, heart disease or parkinsons` considering multiple health parameters.**')
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    # st.title('Diabetes Prediction')
    st.markdown("<h1 style='text-align: center; color: violet;'> Diabetes Prediction 🧑‍⚕️</h1>", unsafe_allow_html=True)

    st.write('The Diabetes Prediction App is a tool that predicts the probability of a patient having diabetes based on diagnostic measurements. This tool is intended for females above the age of 21 years, of Pima Indian Heritage, and uses a dataset from the National Institute of Diabetes and Digestive and Kidney Diseases.')

    with st.expander('Click on the dropdown to see - How it works?'):
        st.subheader('Steps to Predict:')
        st.markdown(
            '1. Enter the required information in the input fields.')
        st.markdown(
            '2. Click the `Diabetes Test Result` button to generate the prediction.')
        st.markdown('')
        
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies','6')
        
    with col2:
        Glucose = st.text_input('Glucose Level','148')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value','72')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value','35')
    
    with col2:
        Insulin = st.text_input('Insulin Level','0')
    
    with col3:
        BMI = st.text_input('BMI value','33.6')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value','0.627')
    
    with col2:
        Age = st.text_input('Age of the Person','50')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result 🔍'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = 'Ooppss! 😲 The Patient is highly likely to have Diabetes.'
            st.error(diab_diagnosis)

        else:
            diab_diagnosis = 'Relaaxxx! 😊 The Patient is likely Diabetes-Free.'
            st.success(diab_diagnosis)



# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    # st.title('Heart Disease Prediction using ML')
    st.markdown("<h1 style='text-align: center; color: red;'> Heart Disease Prediction 💝</h1>", unsafe_allow_html=True)

    st.write('The Heart Disease Prediction App is a tool that predicts the probability of a patient having heart disease based on diagnostic measurements.')

    with st.expander('Click on the dropdown to see - How it works?'):
        st.subheader('Steps to Predict:')
        st.markdown(
            '1. Enter the required information in the input fields.')
        st.markdown(
            '2. Click the `Heart Disease Test Result` button to generate the prediction.')
        st.markdown('')
        
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', '63')
        
    with col2:
        sex = st.text_input('Sex', '1')
        
    with col3:
        cp = st.text_input('Chest Pain types', '3')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', '145')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', '233')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', '1')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', '0')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', '150')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina', '0')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', '2.3')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', '0')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy', '0')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', '1')

    # Convert inputs to appropriate numeric types
    try:
        age = float(age)
        sex = int(sex)
        cp = int(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = int(fbs)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = int(exang)
        oldpeak = float(oldpeak)
        slope = int(slope)
        ca = int(ca)
        thal = int(thal)
        
        # Assuming heart_disease_model is your trained model
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
    except ValueError as e:
        st.error(f"Input error: {e}")
        

     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result 🔍'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'Ooppss! 😲 The Patient is highly likely to have Heart Disease.'
            st.error(heart_diagnosis)
        else:
            heart_diagnosis = 'Relaaxxx! 😊 The Patient is likely Heart Disease Free.'
            st.success(heart_diagnosis)        
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    # st.title("Parkinson's Disease Prediction using ML")
    st.markdown("<h1 style='text-align: center; color: yellow;'> Parkinsons Prediction 🧑‍⚕️</h1>", unsafe_allow_html=True)

    st.write('The Parkinsons Prediction App is a tool that predicts the probability of a patient having parkinsons based on diagnostic measurements.')

    with st.expander('Click on the dropdown to see - How it works?'):
        st.subheader('Steps to Predict:')
        st.markdown(
            '1. Enter the required information in the input fields.')
        st.markdown(
            '2. Click the `Parkinsons Test Result` button to generate the prediction.')
        st.markdown('')
        
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', '119')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', '157')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', '74')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', '0.00784')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', '0.00007')
        
    with col1:
        RAP = st.text_input('MDVP:RAP', '0.00370')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ', '0.00554')
        
    with col3:
        DDP = st.text_input('Jitter:DDP', '0.01109')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', '0.04374')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', '0.426')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', '0.02182')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', '0.03130')
        
    with col3:
        APQ = st.text_input('MDVP:APQ', '0.02971')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA', '0.06545')
        
    with col5:
        NHR = st.text_input('NHR', '0.02211')
        
    with col1:
        HNR = st.text_input('HNR', '21.033')
        
    with col2:
        RPDE = st.text_input('RPDE', '0.414783')
        
    with col3:
        DFA = st.text_input('DFA', '0.815285')
        
    with col4:
        spread1 = st.text_input('spread1', '0.218')
        
    with col5:
        spread2 = st.text_input('spread2', '2.279')
        
    with col1:
        D2 = st.text_input('D2', '2.361')
        
    with col2:
        PPE = st.text_input('PPE', '0.160')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result 🔍"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "Ooppss! 😲 The Patient is highly likely to have Parkinsons Disease."
            st.error(parkinsons_diagnosis)

        else:
            parkinsons_diagnosis = "Relaaxxx! 😊 The Patient is likely Parkinsons Disease Free."
            st.success(parkinsons_diagnosis)

st.markdown(
    "<footer style='text-align: center; position: fixed; bottom: 0; width: 45%; padding: 10px;'>Made with ❤️ by Aman</footer>",
    unsafe_allow_html=True
)
