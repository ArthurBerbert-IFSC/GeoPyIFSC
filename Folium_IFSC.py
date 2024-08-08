import folium
import base64

class Mapa:
    """
    Uma classe que cria um mapa web.

    Atributos:
        bases (dict): Um dicionário que mapeia nomes de bases cartográficas e suas respectivas URLs.

    Métodos:
        Criar_Mapa(coordenadas, zoom_inicial, base=None, attr=None): Cria um novo mapa com a localização, zoom e base especificados.
    """
    
    # Exemplo de bases disponíveis
    bases = {
        'OpenStreetMap': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        'OpenTopoMap': 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
        'Esri WorldImagery': 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        'Esri NatGeoWorldMap': 'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
    }

    @staticmethod
    def Criar_Mapa(coordenadas, zoom_inicial, base=None, attr=None):
        """
        Cria um novo mapa com a localização, zoom e base especificados.

        Args:
            coordenadas (tuple): Um par de coordenadas (latitude, longitude) que especifica a localização inicial do mapa.
            zoom_inicial (int): O nível de zoom inicial do mapa.
            base (str, opcional): O nome ou URL da base do mapa. Se não for fornecido, será usado o mapa padrão do Folium.
            attr (str, opcional): O atributo a ser usado para a base do mapa. Se não for fornecido, será usado o atributo padrão do Folium.

        Returns:
            folium.Map: O mapa criado.
        """
        if base is not None:
            mapa = folium.Map(location=coordenadas, zoom_start=zoom_inicial, tiles=base, attr=attr)
        else:
            mapa = folium.Map(location=coordenadas, zoom_start=zoom_inicial)
        return mapa

class Marcador:
    """
    Classe para criação de marcadores personalizados em mapas interativos com Folium.
    """

    # Exemplos de cores disponíveis para os ícones
    Cores = [
        'lightblue', 'darkblue', 'green', 'darkred', 'cadetblue', 'gray',
        'darkpurple', 'orange', 'purple', 'black', 'blue', 'lightgreen',
        'red', 'white', 'beige', 'darkgreen', 'pink', 'lightgray', 'lightred'
    ]

    # Exemplos de ícones disponíveis
    font_awesome = [
        'bicycle', 'location-crosshairs', 'map', 'bug', 'cloud', 'remove',
        'question', 'info', 'exclamation', 'plus', 'minus', 'asterisk', 'euro',
        'map-marker', 'home', 'building', 'arrow-up', 'arrow-down', 'arrow-left',
        'arrow-right', 'traffic-light', 'flag', 'star'
    ]  
    glyphicon = [
        'ok-sign', 'remove-sign', 'question-sign', 'info-sign', 'exclamation-sign',
        'plus-sign', 'minus-sign', 'asterisk', 'euro', 'cloud', 'heart'
    ]

    @staticmethod
    def criar_icone(prefixo, simbolo, cor_simbolo, cor_fundo, rotação=0):
        """
        Cria um ícone personalizado para um marcador.

        Args:
            prefixo (str): O prefixo do ícone ('fa' para FontAwesome, 'glyphicon' para Glyphicon).
            simbolo (str): O símbolo do ícone.
            cor_simbolo (str): A cor do símbolo.
            cor_fundo (str): A cor de fundo do ícone.
            rotação (int, opcional): O ângulo de rotação do ícone. O padrão é 0.

        Returns:
            folium.Icon: Um objeto de ícone personalizado.
        """
        return folium.Icon(prefix=prefixo, icon=simbolo, icon_color=cor_simbolo, color=cor_fundo, angle=rotação)

    class Popup:
        """
        Classe para criação de popups em mapas interativos.

        Métodos:
            HTML(titulo, texto, link, texto_link='Clique aqui'): Gera código HTML para um popup com texto e um link.
            HTML_Imagem_embutida(titulo, texto, caminho, link, link_texto, largura=150, altura=150): Gera código HTML para um popup com uma imagem, texto e um link.
            HTML_Imagem_URL(titulo, texto, imagem, link, link_texto, largura=None, altura=None): Gera código HTML para um popup com uma imagem, texto e um link.
            decode_image(imagem): Decodifica um arquivo de imagem para o formato base64.
        """

        @staticmethod
        def HTML(titulo, texto, link, texto_link='Clique aqui'):
            """
            Gera código HTML para um popup com texto e um link.

            Args:
                titulo (str): O título do popup.
                texto (str): O conteúdo de texto do popup.
                link (str): A URL do link.
                texto_link (str, opcional): O texto a ser exibido para o link. O padrão é 'Clique aqui'.

            Returns:
                str: O código HTML gerado para o popup.
            """
            html = f'''<h3>{titulo}</h3>
                      <p>{texto}</p>
                      <a href="{link}" target="_blank">{texto_link}</a>
                      '''
            return html

        @staticmethod
        def decode_image(imagem):
            """
            Decodifica um arquivo de imagem para o formato base64.

            Args:
                imagem (str): O caminho para o arquivo de imagem. Se estiver na mesma pasta do arquivo que o script, 
                basta passar o nome do arquivo.

            Returns:
                str: A string codificada em base64 da imagem.
            """
            with open(imagem, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()
            return encoded_image

        @staticmethod
        def HTML_Imagem_embutida(titulo, texto, caminho, link, link_texto, largura=150, altura=150):
            """
            Gera código HTML para um popup com uma imagem, texto e um link.

            Args:
                titulo (str): O título do popup.
                texto (str): O conteúdo de texto do popup.
                caminho (str): O caminho para o arquivo de imagem.
                link (str): A URL do link.
                link_texto (str): O texto a ser exibido para o link.
                largura (int, opcional): A largura da imagem em pixels. O padrão é 150.
                altura (int, opcional): A altura da imagem em pixels. O padrão é 150.

            Returns:
                str: O código HTML gerado para o popup.
            """
            # Decodifica a imagem para base64
            encoded_image = Marcador.Popup.decode_image(caminho)

            # Gera o código HTML para o popup
            html = f'''<h3>{titulo}</h3>
                      <img src="data:image/jpeg;base64,{encoded_image}" alt="Imagem Exemplo" style="width:{largura}px; height:{altura}px;"><br>
                      <p>{texto}</p>
                      <a href="{link}" target="_blank">{link_texto}</a>
                      '''
            return html

        @staticmethod
        def HTML_Imagem_URL(titulo, texto, imagem, link, link_texto, largura=None, altura=None):
            """
            Gera código HTML para um popup com uma imagem, texto e um link.

            Args:
                titulo (str): O título do popup.
                texto (str): O conteúdo de texto do popup.
                imagem (str): A URL da imagem.
                link (str): A URL do link.
                link_texto (str): O texto a ser exibido para o link.
                largura (int, opcional): A largura da imagem em pixels. O padrão é 150.
                altura (int, opcional): A altura da imagem em pixels. O padrão é 150.

            Returns:
                str: O código HTML gerado para o popup.
            """
            html = f'''<h3>{titulo}</h3>
                      <img src="{imagem}" alt="Imagem Exemplo" style="width:{largura}px; height:{altura}px;"><br>
                      <p>{texto}</p>
                      <a href="{link}" target="_blank">{link_texto}</a>
                      '''
            return html

    @staticmethod
    def Criar_Marcador(coordenadas, icone, popup=None, tooltip=None):
        """
        Cria um marcador em um mapa interativo.

        Args:
            coordenadas (list): Lista de coordenadas [latitude, longitude] para o marcador.
            icone (folium.Icon): Objeto de ícone personalizado para o marcador.
            popup (folium.Popup, opcional): Objeto de popup personalizado para o marcador. O padrão é None.
            tooltip (str, opcional): Texto que aparece ao passar o mouse sobre o marcador. O padrão é None.

        Returns:
            folium.Marker: Um objeto de marcador criado.
        """
        return folium.Marker(location=coordenadas, icon=icone, popup=popup, tooltip=tooltip)