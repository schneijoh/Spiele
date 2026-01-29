import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Notendurchschnitt Rechner", page_icon="📚", layout="centered")

# Custom CSS für schöneres Design
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
h1 {
    color: #2c3e50;
    text-align: center;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Zeugnis-Notendurchschnitt Rechner")
st.write("Berechne einfach deinen Zeugnis-Durchschnitt und sieh deine Noten im Diagramm 📊")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    anzahl_faecher = st.number_input("📘 Wie viele Fächer hast du?", min_value=1, max_value=50, step=1)

    fach_namen = []
    noten = []

    for i in range(int(anzahl_faecher)):
        col1, col2 = st.columns(2)
        with col1:
            fach = st.text_input(f"Fachname {i+1}", value=f"Fach {i+1}")
        with col2:
            note = st.number_input(f"Note {i+1}", min_value=1.0, max_value=6.0, step=0.1, format="%.1f")

        fach_namen.append(fach)
        noten.append(note)

    if st.button("📊 Durchschnitt berechnen"):
        durchschnitt = sum(noten) / len(noten)

        st.success(f"🎯 Dein Notendurchschnitt ist: **{durchschnitt:.2f}**")

        # Bewertung
        if durchschnitt <= 1.5:
            st.balloons()
            st.write("🌟 Sehr stark! Top Leistung!")
        elif durchschnitt <= 2.5:
            st.write("👍 Gut gemacht!")
        elif durchschnitt <= 3.5:
            st.write("🙂 Solide Leistung")
        else:
            st.write("💪 Da geht noch was – du schaffst das!")

        # Diagramm
        st.markdown("### 📈 Noten-Diagramm")

        fig = plt.figure()
        plt.bar(fach_namen, noten)
        plt.axhline(y=durchschnitt, linestyle='--', label=f'Durchschnitt: {durchschnitt:.2f}')
        plt.xlabel("Fächer")
        plt.ylabel("Noten")
        plt.title("Notenübersicht")
        plt.legend()
        plt.xticks(rotation=45)

        st.pyplot(fig)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("✨ Moderne Streamlit WebApp | Notenrechner mit Diagramm")
