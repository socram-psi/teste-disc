import streamlit as st

# Configuração da página
st.title("Teste DISC Automatizado")
st.write("Selecione as características que mais combinam com você:")

# Características agrupadas por categoria
caracteristicas = {
    "Dominância (D)": ["Direto", "Decidido", "Ativo", "Ousado", "Autoconfiante"],
    "Influência (I)": ["Amigável", "Extrovertido", "Carismático", "Convincente", "Sociável"],
    "Estabilidade (S)": ["Paciente", "Tolerante", "Compreensivo", "Gentil", "Leal"],
    "Conformidade (C)": ["Perfeccionista", "Prudente", "Disciplinado", "Meticuloso", "Respeitoso"]
}

# Criar checkboxes para cada característica
respostas = {tipo: [] for tipo in caracteristicas}
for tipo, lista in caracteristicas.items():
    st.subheader(tipo)
    for item in lista:
        if st.checkbox(item, key=item):
            respostas[tipo].append(item)

# Botão para processar o resultado
if st.button("Ver meu perfil DISC"):
    perfil = {tipo: len(respostas[tipo]) for tipo in respostas}
    perfil_ordenado = sorted(perfil.items(), key=lambda x: x[1], reverse=True)
    resultado = f"Seu perfil predominante é: **{perfil_ordenado[0][0]}**"
    st.success(resultado)
