import streamlit as st
import joblib
import os
import numpy as np

# --- 1. Page Configuration ---
st.set_page_config(page_title="Salary Predictor", layout="centered")

@st.cache_resource
def load_assets():
    base_path = os.path.dirname(__file__)
    model_path = os.path.join(base_path, 'salary_model.pkl')
    encoding_path = os.path.join(base_path, 'encoding_maps.pkl')
    
    try:
        model_obj = joblib.load(model_path)
        maps_obj = joblib.load(encoding_path)
        
        # Verify the model is not a string
        if isinstance(model_obj, str):
            return None, None
            
        return model_obj, maps_obj
    except Exception:
        return None, None

model, encoding_maps = load_assets()

# --- 2. Interface ---
if model is not None and encoding_maps is not None:
    st.title("Software Developer Salary Predictor (Egypt) 🇪🇬")
    st.write("Predict monthly salaries using a refined XGBoost model.")

    # Dropdown Options
    titles = list(encoding_maps['title'].keys())
    cities = list(encoding_maps['city of company site'].keys())
    work_types = list(encoding_maps['work type'].keys())
    work_hours = list(encoding_maps['work hour'].keys())

    col1, col2 = st.columns(2)
    
    with col1:
        selected_title = st.selectbox("Job Title:", titles)
        selected_city = st.selectbox("City:", cities)
        selected_work_type = st.selectbox("Work Type:", work_types)
    
    with col2:
        selected_work_hour = st.selectbox("Work Hour:", work_hours)
        experience = st.number_input("Years of Experience:", min_value=0.0, max_value=40.0, value=2.0)

    # --- 3. Prediction ---
    if st.button("Predict Salary"):
        try:
            # IMPORTANT: Convert categories to their MEAN salaries (Target Encoding)
            title_val = encoding_maps['title'].get(selected_title, encoding_maps['global_mean'])
            city_val = encoding_maps['city of company site'].get(selected_city, encoding_maps['global_mean'])
            type_val = encoding_maps['work type'].get(selected_work_type, encoding_maps['global_mean'])
            hour_val = encoding_maps['work hour'].get(selected_work_hour, encoding_maps['global_mean'])

            # Features MUST be in this exact order: 
            # [title, years of experiences, work hour, work type, city of company site]
            features = np.array([[title_val, experience, hour_val, type_val, city_val]])
            
            prediction = model.predict(features)[0]
            
            st.success(f"Estimated Salary: {round(prediction, 2):,} EGP")
            
        except Exception as e:
            st.error(f"Prediction error: {e}")
else:
    st.error("Error: Assets (model or maps) could not be loaded as objects. Please re-run the export in your Notebook.")