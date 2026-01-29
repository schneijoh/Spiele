import streamlit as st

st.set_page_config(page_title="Notendurchschnitt Rechner", page_icon="📚")

st.title("📚 Notendurchschnitt Rechner")
st.write("Einfache Streamlit WebApp zur Berechnung deines Zeugnis-Durchschnitts")

# Eingabe Anzahl Fächer
anzahl_faecher = st.number_input("Wie viele Fächer hast du?", min_value=1, max_value=20, step=1)

fach_namen = []
noten = []

# Dynamische Felder
for i in range(int(anzahl_faecher)):
    fach = st.text_input(f"Fach {i+1}", value=f"Fach {i+1}", key=f"f_{i}")
    note = st.number_input(f"Note für {fach}", min_value=1.0, max_value=6.0, step=0.1, key=f"n_{i}")
    fach_namen.append(fach)
    noten.append(note)

# Button
if st.button("Durchschnitt berechnen"):
    if len(noten) > 0:
        durchschnitt = sum(noten) / len(noten)
        st.success(f"Dein Notendurchschnitt: {durchschnitt:.2f}")

        # Diagramm (ohne matplotlib)
        st.markdown("### 📊 Notenübersicht")
        chart_data = {fach_namen[i]: noten[i] for i in range(len(fach_namen))}
        st.bar_chart(chart_data)

        st.info(f"📈 Durchschnitt: {durchschnitt:.2f}")
    else:
        st.error("Bitte Noten eingeben")
