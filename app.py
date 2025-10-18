# app.py
import streamlit as st
from utils import predict_email  # your combined utils.py

# --- Title ---
st.title("📧 Heimdall - Email Classifier")
st.write("""
Classify emails into six categories:  
**Promotion, Spam, Social Media, Forum, Verify Code, Updates**
""")

# --- Single email input ---
st.subheader("Predict a single email")
email_text = st.text_area("Enter your email here:")

if st.button("Classify Email"):
    if email_text.strip() == "":
        st.warning("Please enter an email to classify.")
    else:
        # Run prediction using utils.py
        results = predict_email(email_text)
        
        # Display predictions and confidence
        st.subheader("Predictions:")
        for model_name, (pred, confidence) in results.items():
            if confidence is not None:
                st.write(f"**{model_name}**: {pred} ({confidence:.2f}% confident)")
            else:
                st.write(f"**{model_name}**: {pred}")

        # Optional: show confidence bar chart
        import pandas as pd
        conf_df = pd.DataFrame({k: [v[1]] for k, v in results.items()})
        st.bar_chart(conf_df.T)
