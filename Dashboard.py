import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_bypayment_df(df):
    bypayment_df = df.groupby(by="payment_type").order_id.nunique().reset_index()
    bypayment_df.rename(columns ={
    "order_id": "order_count"
}, inplace=True)
    return bypayment_df

def create_bystate_df(df):
    bystate_df = df.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={
    "customer_id": "order_count"
}, inplace=True)
    return bystate_df


all_df = pd.read_csv("all_data.csv")
all_customer_with_order_df = pd.read_csv("all_customer_join_orders.csv")


bypayment_df = create_bypayment_df(all_df)
bystate_df = create_bystate_df(all_customer_with_order_df)




with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")

st.header('Dicoding Collection Dashboard :sparkles:')

st.subheader("Customer Demographics")
col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))
 
    sns.barplot(
        y="order_count", 
        x="payment_type",
        data=bypayment_df.sort_values(by="order_count", ascending=False),
        ax=ax
    )
    ax.set_title("Number of Customer by Payment", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

with col2: 
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        y="order_count",
        x="customer_state",
        data=bystate_df.sort_values(by="order_count", ascending=False)
    )
    ax.set_title("Number of Customer by State", loc="center", fontsize=30)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    st.pyplot(fig)

st.caption('Copyright (c) Dicoding 2023')