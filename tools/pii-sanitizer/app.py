import streamlit as st
import pandas as pd
import hmac
import hashlib

def encrypt_column(df, columns, key):
    for column in columns:
        df[column] = df[column].apply(lambda x: hmac.new(key.encode(), str(x).encode(), hashlib.sha256).hexdigest())
    return df

st.title('CSV PII - Column Encryption App')

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
columns = []
secret_key = ""

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    columns = st.multiselect("Select columns to encrypt", df.columns.tolist())
    secret_key = st.text_input("Enter your shared secret key")

if st.button("Submit & Encrypt"):
    if uploaded_file is None:
        st.error("⚠️ Please upload a CSV file before submitting.")
    elif not columns:
        st.error("⚠️ Please select at least one column to encrypt.")
    elif not secret_key:
        st.error("⚠️ Please enter a secret key.")
    else:
        encrypted_df = encrypt_column(df, columns, secret_key)
        st.success("✅ Encryption completed successfully!")
        st.write("Encrypted Data Preview:", encrypted_df.head())

        encrypted_file = encrypted_df.to_csv(index=False).encode()
        st.download_button(
            label="Download Encrypted CSV",
            data=encrypted_file,
            file_name="encrypted_file.csv",
            mime="text/csv"
        )

