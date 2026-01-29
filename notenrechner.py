import streamlit as st

st.set_page_config(page_title="Notendurchschnitt Rechner", page_icon="📚", layout="centered")

# ---------- Header ----------
st.markdown("# 📚 Notendurchschnitt Rechner")
st.markdown("Berechne deinen Zeugnis-Durchschnitt übersichtlich und strukturiert.")

# ---------- Anzahl Fächer ----------
anzahl_faecher = st.number_input("Wie viele Fächer hast du?", min_value=1, max_value=20, step=1)

# ---------- Standard-Fächer ----------
standard_faecher = ["Deutsch", "Mathe", "Englisch", "Biologie", "Chemie", "Physik", "Geschichte", "Geographie", "Kunst", "Musik"]

fach_namen = []
noten = []

st.markdown("---")
st.markdown("### Fächer & Noten")
for i in range(int(anzahl_faecher)):
    col1, col2 = st.columns([2,1])
    with col1:
        if i < len(standard_faecher):
            fach = st.text_input(f"Fach {i+1}", value=standard_faecher[i], key=f"f_{i}")
        else:
            fach = st.text_input(f"Fach {i+1}", value=f"Fach {i+1}", key=f"f_{i}")
    with col2:
        note = st.number_input(f"Note", min_value=1.0, max_value=6.0, step=0.1, key=f"n_{i}")
    fach_namen.append(fach)
    noten.append(note)

st.markdown("---")

# ---------- Durchschnitt ----------
if st.button("📊 Durchschnitt berechnen"):
    if len(noten) > 0:
        durchschnitt = sum(noten) / len(noten)
        st.markdown(f"## 🎯 Dein Notendurchschnitt: **{durchschnitt:.2f}**")

        # Bewertung
        if durchschnitt <= 1.5:
            st.success("🌟 Sehr stark! Top Leistung!")
        elif durchschnitt <= 2.5:
            st.info("👍 Gut gemacht!")
        elif durchschnitt <= 3.5:
            st.warning("🙂 Solide Leistung")
        else:
            st.error("💪 Da geht noch was – du schaffst das!")

        # Diagramm
        st.markdown("### 📈 Notenübersicht")
        chart_data = {fach_namen[i]: noten[i] for i in range(len(fach_namen))}
        st.bar_chart(chart_data)

        st.info(f"📌 Durchschnitt: {durchschnitt:.2f}")
    else:
        st.error("Bitte Noten eingeben")
 
