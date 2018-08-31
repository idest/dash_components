import idest_dash_components
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    idest_dash_components.ExampleComponent(
        id='input',
        value='my-value',
        label='my-label'
    ),
    idest_dash_components.Slider(
        id='input-slider',
        min=0,
        max=10,
        step=1,
        value=5,
    ),
    html.Div(id='output', style={'margin-top': 40}),
    html.Div(id='output-slider')
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)
@app.callback(Output('output-slider', 'children'), [Input('input-slider', 'value')])
def display_slider_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
