import streamlit as st
def createCards(text, value, container_style=0, value_style=0):
    # Definir cores personalizadas
    color_white = '#ffffff'
    gradient_color1 = '#9c27b0'
    gradient_color2 = '#673ab7'

    if (container_style == 0):
        # Estilo CSS inline
        container_style = f"""
    background: linear-gradient(135deg, {gradient_color1}, {gradient_color2});
    padding: 2rem;
    border-radius: 1rem;
    color: {color_white};
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    """
    if (value_style == 0):
        value_style = f"""
    color: {color_white};
    font-weight: bold;
    """
    with st.container():
        st.markdown(f'<div style="{container_style}">{text} <span style="{value_style}">{value}</span></div>',
                    unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)


def createCards2(text, value, container_style=0, value_style=0):
    # Definir cores personalizadas
    color_white = '#ffffff'
    gradient_color1 = '#FF7F50'  # Cores de laranja
    gradient_color2 = '#FF6347'

    # Definindo altura e largura fixas
    fixed_height = '150px'
    fixed_width = '200px'

    if (container_style == 0):
        # Estilo CSS inline
        container_style = f"""
        background: linear-gradient(135deg, {gradient_color1}, {gradient_color2});
        padding: 2rem;
        border-radius: 1rem;
        color: {color_white};
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        height: {fixed_height};
        width: {fixed_width};
        margin: 10px;
        """

    if (value_style == 0):
        value_style = f"""
      color: {color_white};
      font-weight: bold;
      """

    with st.container():
        st.markdown(f'<div style="{container_style}">{text} <span style="{value_style}">{value}</span></div>',
                    unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)