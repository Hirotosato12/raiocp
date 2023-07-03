import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from haversine import haversine, Unit
from interestingFunctions import createCards2

## C:\Users\hirot\Downloads\logo_cp.png



def main():
    st.sidebar.image('clubpetro_logo.png', use_column_width=True)
    analysis_type = st.sidebar.selectbox('Escolha o tipo de análise',
                                         ['Geral', 'Mapa de todos os Postos'])



    if analysis_type == 'Geral':

        st.image(r'clubpetro_logo.png', use_column_width=True)
        st.title("Estratégia Comercial")
        # definir o dataframe
        df = pd.read_csv(r'C:\Users\hirot\Downloads\anplat.csv.csv')

        # Converte as colunas 'Lat' e 'Lon' para números
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')
        # Criando a barra de pesquisa para o CNPJ
        cnpj = st.text_input('Digite o CNPJ do posto')

        # Definindo o raio

        # Quando o CNPJ é inserido
        if cnpj:
            # Encontrando o posto correspondente
            posto = df[df['CNPJ'] == cnpj]



            # Se o posto existe
            if not posto.empty:

                # Aqui você cria as colunas
                col1, col2, col3, col4 = st.columns(4)

                # E aqui você utiliza a função createCards para criar os cards dentro das colunas
                with col1:
                    createCards2('Razão Social', posto['Razão Social'].values[0])
                with col2:
                    createCards2('Endereço', posto['Endereço'].values[0])
                with col3:
                    createCards2('Bairro', posto['Bairro'].values[0])
                with col4:
                    createCards2('CEP', posto['CEP'].values[0])

                col5, col6, col7, col8 = st.columns(4)

                with col5:
                    createCards2('UF', posto['UF'].values[0])
                with col6:
                    createCards2('Município', posto['Município'].values[0])
                with col7:
                    createCards2('População', posto['População'].values[0])
                with col8:
                    createCards2('Vinculação a Distribuidor', posto['Vinculação a Distribuidor'].values[0])

                lat = posto['Lat'].values[0]
                lon = posto['Lon'].values[0]

                raio = st.slider('Selecione o raio (em km)', 0, 50, 10)

                # Limpa os dados que possuem 'nan' nas colunas de Lat e Lon
                df = df.dropna(subset=['Lat', 'Lon'])

                # Cria uma nova coluna com a distância do ponto de referência para cada ponto
                df['Distancia'] = df.apply(lambda row: haversine((lat, lon), (row['Lat'], row['Lon']), unit=Unit.KILOMETERS), axis=1)

                # Filtra os pontos que estão dentro do raio
                postos_proximos = df[df['Distancia'] <= raio]

                # Criar um mapa centrado nas coordenadas do posto
                m = folium.Map(location=[lat, lon], zoom_start=13)



                # Adicionar marcadores para os postos próximos
                for _, posto_proximo in postos_proximos.iterrows():
                    if posto_proximo['Cliente CP'] == 'Cliente Clubpetro':
                        cor = "orange"
                    else:
                        cor = "gray"

                    folium.Marker(
                        location=[posto_proximo['Lat'], posto_proximo['Lon']],
                        popup=f"CNPJ: {posto_proximo['CNPJ']}",
                        icon=folium.Icon(color=cor),
                    ).add_to(m)

                # Adicionar um marcador para o posto
                folium.Marker(
                    location=[lat, lon],
                    popup=f"CNPJ: {cnpj}",
                    icon=folium.Icon(color="blue", icon="info-sign"),  # Usando 'info-sign' em azul para o ícone
                ).add_to(m)




                # Exibir o mapa

                with st.expander("Mapa"):
                    folium_static(m)
                    st.write("""
                    **Legenda do Mapa**
                    - Ícone Azul: Posto Selecionado
                    - Ícone Laranja: Posto que é Cliente Clubpetro
                    - Ícone Cinza: Posto que não é Cliente Clubpetro
                    """)

                # Gerando as tabelas de postos próximos
                st.write('Clientes Clubpetro no raio selecionado:')
                clubpetro = postos_proximos[postos_proximos['Cliente CP'] == 'Cliente Clubpetro']
                clubpetro = clubpetro[['Distancia', 'Razão Social', 'Indice de Fidelidade']]
                st.dataframe(clubpetro)

                st.write('Não é Cliente Clubpetro no raio selecionado:')
                nao_clubpetro = postos_proximos[postos_proximos['Cliente CP'] == 'Não é Cliente Clubpetro']
                nao_clubpetro = nao_clubpetro[['Distancia', 'Razão Social']]
                st.dataframe(nao_clubpetro)

    if analysis_type == 'Mapa de todos os Postos':

        df = pd.read_csv(r'C:\Users\hirot\Downloads\anplat.csv.csv')

        # Limpa os dados que possuem 'nan' nas colunas de Lat e Lon
        df = df.dropna(subset=['Lat', 'Lon'])

        # Converte as colunas 'Lat' e 'Lon' para números
        df['Lat'] = pd.to_numeric(df['Lat'], errors='coerce')
        df['Lon'] = pd.to_numeric(df['Lon'], errors='coerce')


        st.image(r'clubpetro_logo.png', use_column_width=True)
        st.title("Mapa de todos os Postos")

        # # Cria um mapa centrado no Brasil
        # m = folium.Map(location=[-15.788497, -47.879873],
        #                zoom_start=4)  # Coordenadas de Brasília, aproximadamente o centro do Brasil
        #
        # # Adicionar marcadores para todos os postos
        # for _, posto in df.iterrows():
        #     if posto['Cliente CP'] == 'Cliente Clubpetro':
        #         cor = "orange"
        #     else:
        #         cor = "gray"
        #
        #     folium.Marker(
        #         location=[posto['Lat'], posto['Lon']],
        #         popup=f"CNPJ: {posto['CNPJ']}",
        #         icon=folium.Icon(color=cor),
        #     ).add_to(m)

        # Exibir o mapa
        # folium_static(m)



if __name__ == "__main__":
    main()
