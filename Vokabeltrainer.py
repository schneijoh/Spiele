import streamlit as st
import pandas as pd
import os
import random
from fpdf import FPDF

# -----------------------------
# Seitentitel & Layout
# -----------------------------
st.set_page_config(page_title="Vokabeltrainer", page_icon="📚", layout="centered")
st.markdown("<h1 style='text-align: center; color: #0b3d91;'>📚 Vokabeltrainer</h1>", unsafe_allow_html=True)

# -----------------------------
# Datenmanagement
# -----------------------------
VOCAB_FILE = "vokabeln.csv"
if os.path.exists(VOCAB_FILE):
    df = pd.read_csv(VOCAB_FILE)
else:
    df = pd.DataFrame(columns=["Deutsch", "Fremdsprache", "Richtig", "Falsch"])

# -----------------------------
# Neue Vokabeln hinzufügen
# -----------------------------
st.subheader("Neue Vokabel hinzufügen")
with st.form("add_vocab"):
    deutsch = st.text_input("Deutsch")
    fremdsprache = st.text_input("Fremdsprache")
    submitted = st.form_submit_button("Hinzufügen")
    if submitted and deutsch and fremdsprache:
        df = pd.concat([df, pd.DataFrame([{"Deutsch": deutsch, "Fremdsprache": fremdsprache, "Richtig": 0, "Falsch": 0}])], ignore_index=True)
        df.to_csv(VOCAB_FILE, index=False)
        st.success(f"Vokabel '{deutsch} - {fremdsprache}' hinzugefügt!")

# -----------------------------
# Karteikarten-Übung
# -----------------------------
st.subheader("Karteikarten-Übung")
if not df.empty:
    vocab = df.sample(1).iloc[0]
    st.markdown(f"**Deutsch:** {vocab['Deutsch']}")
    answer = st.text_input("Fremdsprache eingeben:", key="karteikarte")
    if st.button("Antwort prüfen"):
        if answer.strip().lower() == vocab['Fremdsprache'].strip().lower():
            st.success("Richtig!")
            df.loc[df.index == vocab.name, "Richtig"] += 1
        else:
            st.error(f"Falsch! Richtige Antwort: {vocab['Fremdsprache']}")
            df.loc[df.index == vocab.name, "Falsch"] += 1
        df.to_csv(VOCAB_FILE, index=False)

# -----------------------------
# Statistiken & Diagramme
# -----------------------------
st.subheader("Statistiken")
if not df.empty:
    st.bar_chart(df.set_index("Deutsch")[["Richtig"]])

# -----------------------------
# PDF-Export
# -----------------------------
st.subheader("Vokabeln als PDF speichern")
if st.button("PDF exportieren"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for index, row in df.iterrows():
        pdf.cell(200, 10, txt=f"{row['Deutsch']} - {row['Fremdsprache']}", ln=True)
    pdf.output("vokabeln.pdf")
    st.success("Vokabeln als PDF gespeichert!")

# -----------------------------
# Gamification: Punkte & Level
# -----------------------------
st.subheader("Gamification")
if not df.empty:
    df['Punkte'] = df['Richtig'] * 10 - df['Falsch'] * 5
    level = df['Punkte'].sum() // 50
    st.markdown(f"**Gesamtpunkte:** {df['Punkte'].sum()} | **Level:** {level}")

# -----------------------------
# Designhinweis
# -----------------------------
st.markdown("""
<style>
body {background-color: #e6f0ff;}
</style>
""", unsafe_allow_html=True)

st.info("💡 Tipp: Die App speichert Vokabeln in `vokabeln.csv`. Du kannst diese Datei sichern oder bearbeiten.")

    

