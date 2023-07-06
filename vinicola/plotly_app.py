from exploratory_visualization import comercializacao
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


df_comercio = comercializacao()
df_comercio = df_comercio.loc[df_comercio["ANO"] >= 2006].query('QTD_LITRO != 0.0')
df_comercio_grouped = df_comercio.groupby('ANO').agg(QTD_PRODUTO_ANO=('PRODUTO', 'count'), MEDIA_LITROS=('QTD_LITRO', 'mean')).reset_index()

# Criar gráfico de barras com Plotly Express
comercio = px.bar(df_comercio_grouped, x='ANO', y='QTD_PRODUTO_ANO')

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

colors = {
    'background': '#000000',
    'text': '#FFFFFF'
}

# Definir o layout da página
app.layout = html.Div([
    # Título da página
    html.H1('Tech Challenge', style={'textAlign': 'center', 'color': '#16BA00'}),
    html.H2('Vitivinicultura, Embrapa Uva e Vinho', style={'textAlign': 'center', 'color': '#DCEDFF'}),
    # html.H3('Autores: Anna Karoliny e Victor Hugo', style={'color': '#DCEDFF'}),
    # Elemento Markdown
    dcc.Markdown('''

    Uma empresa desde 1970, que entrega qualidade no produto para clientes no mundo todo, sendo presente em 65 países.
    Invista agora no nosso negócio. Ainda tem dúvidas? Em 5 minutos com as informações abaixo e necessárias, vai te fazer pensar em fazer parte o quanto antes.

    '''),

    html.H2('Segurança nas Ações', style={'color': '#16BA00'}),
    dcc.Markdown('''

    **Nos ultimos 15 anos, mesmo em crises, sempre nos mantivemos e continuamos referência no mercado de vinhos e espumantes. 
    Se busca sofisticação, tempo de mercado, uma empresa presente nos principais países, e com entrega de qualidade, você está no lugar certo** 
    '''),

    html.H2('Tomada de Decições com Análise de Dados', style={'color': '#16BA00'}),
    dcc.Markdown('''

    **Um dos maiores motivos para investir conosco é que temos a tomada de decisão a partir do dados que nós obtemos. 
    É com toda a garantia que nossa empresa afirma, o investimento conosco é a certeza que só temos crescimento e retorno financeiro.**

    Saiba mais abaixo com nossas análises autorais.
    '''),

    html.H2('Comércio', style={'color': '#16BA00'}),
    html.H3('Temos constância e somos líderes em comercializar nossos produtos', style={'color': '#DCEDFF'}),

    dcc.Markdown('''
    
    Nos ultimos anos, continuamos comercializando todos os nossos produtos, entre eles vinhos, espumantes, sucos e entre outros, totalizando em 45 produtos.
    Podemos concluir com nossas análises, que 99% de todos os produtos estão sendo comercializados, desde 2006.
    '''),
    
    # Gráfico de barras
    dcc.Graph(figure=comercio)

])

# Executar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
