# Import Dependencies
import streamlit as st
import joblib
import pandas as pd

# Import Saved Models & Data
Symptoms = joblib.load("Symptoms.pkl")
Input_DF = joblib.load("input_transformer.pkl")
Scaler = joblib.load("Scaler.pkl")
Model = joblib.load("Model.pkl")
sol = pd.read_csv('solution.csv')

# Create Streamlit web-page

col1, col2 = st.columns([1, 3])

with col1:
   st.image(
       "https://static.vecteezy.com/system/resources/previews/005/097/848/non_2x/a-female-doctor-cartoon-character-on-white-background-free-vector.jpg")

with col2:
    st.header("Hi! How are you feeling today? ")
    st.subheader("What health concerns are you having?")
    # Create a MultiSelect Dropdown Button
    Selected_Symptoms = st.multiselect(
        'Please do not select more then 17 Symptoms',
        Symptoms)


# Transform input from Dropdown
add = []
for opt in Selected_Symptoms:
    for i in range(len(Input_DF)):
        if opt == Input_DF['Symptom'][i]:
            add += str(Input_DF['weight'][i])

input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in add:
    for i in range(len(add)):
        input[i] = int(add[i])

# Scale the Data
scaled_input = Scaler.transform([input])

# Predict the Disease
Output = Model.predict(scaled_input)
Model_Output = ' '.join(Output).replace('_', ' ')


# Providing Description for the Disease
def description(Model_Output):
    for i in range(0, 41):
        if sol['Disease'][i] == Model_Output:
            return sol['Description'][i]


# Providing Treatment for the Disease
def p1(Model_Output):
    for i in range(0, 41):
        if sol['Disease'][i] == Model_Output:
            return sol['Precaution_1'][i]

def p2(Model_Output):
    for i in range(0, 41):
        if sol['Disease'][i] == Model_Output:
            return sol['Precaution_2'][i]

def p3(Model_Output):
    for i in range(0, 41):
        if sol['Disease'][i] == Model_Output:
            return sol['Precaution_3'][i]

def p4(Model_Output):
    for i in range(0, 41):
        if sol['Disease'][i] == Model_Output:
            return sol['Precaution_4'][i]

# Create a Submit Button
if st.button('Submit'):
    st.write(Model_Output)
    st.write(description(Model_Output))
    st.write('Treatment options for', Model_Output, 'are:-')
    st.write('1.', p1(Model_Output))
    st.write('2.', p2(Model_Output))
    st.write('3.', p3(Model_Output))
    st.write('4.', p4(Model_Output))
