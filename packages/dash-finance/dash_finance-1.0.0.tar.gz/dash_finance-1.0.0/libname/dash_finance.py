import yfinance as yf
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, html, dcc

app = Dash(__name__)
data = yf.download("AAPL", period="1d", interval="1m")


class DashFinance(go.Figure):
    def __init__(self):
        super().__init__()    
        # Set the layout
        self.update_xaxes(
            rangeslider_visible=True,
            rangebreaks=[
                # NOTE: Below values are bound (not single values), ie. hide x to y
                dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
                dict(bounds=[16, 9.5], pattern="hour"),  # hide hours outside of 9.30am-4pm
                # dict(values=["2020-12-25", "2021-01-01"])  # hide holidays (Christmas and New Year's, etc)
            ]
        )


        self.update_layout(
            title='Stock Analysis',
            yaxis_title=f'AAPL Stock',
            dragmode='pan',             # Enable chart dragging by clicking and holding left button of mouse
            plot_bgcolor='#E9EDF7',          # Set the background color of the plot
            paper_bgcolor='#E9EDF7' # 
        )

        self.update_xaxes(rangeslider_visible=True, showgrid=False)
        self.update_yaxes(showgrid=True)
        self.update_yaxes(showspikes=True, spikemode="across", spikesnap="cursor", showline=True, spikethickness=1,
                        spikedash="dot")
        self.update_xaxes(showspikes=True, spikemode="across", spikesnap="cursor", showline=True, spikethickness=1,
                        spikedash="dot")
        self.update_yaxes(fixedrange=False)
        self.update_layout(yaxis=dict(fixedrange=False), yaxis2=dict(fixedrange=False))
        self.update_yaxes(showticklabels=True)

        # ─── PLACING PRICE  IN RIGHT SIDE ────────────────────────────────────────────────────────────────────────
    

        # ─── PLACING PRICE  IN RIGHT SIDE ────────────────────────────────────────────────────────────────────────
        self.update_layout(
            yaxis=dict(title="Price", side="right", showgrid=False, zeroline=False, showline=True, ticks="", fixedrange=False),
            yaxis2=dict(title="Volume", side="left", showgrid=False, zeroline=False, showline=True, ticks="", fixedrange=True)
        )

        # ─── MOUSE DRAGGING LIKE IN TRADINGVIEW ────────────────────────────────────────────────────────────────────────
        self.update_layout(
            xaxis=dict(
                rangemode="tozero",  # Set the x-axis range mode
                rangeslider=dict(visible=False),  # Hide the range slider
                type="date",
                hoverformat="%Y-%m-%d %H:%M:%S"
            ),
            uirevision=True  # Add a revision number to the layout so that zoom and drag actions do not conflict with each other
        )

    def candlestick(self, data):
        candle = go.Candlestick(
            x = data.index,
            open = data["Open"],
            high = data["High"],
            low = data["Low"],
            close = data["Close"]
        )
        return self.add_trace(candle)
    
    def add_text(self, x1, y1, msg="Add text", color="black"):
        # x = list(x1)
        # y = list(y1)
        return self.add_trace(go.Scatter(
            x=[x1], y=[y1], mode='text', text=msg, textfont=dict(color=color)
        )
    )
    def add_line(self, x1=[], y1=[], mode='lines', color="blue", name="Line"):
        """
            x1 is the list of x-axis coordinates and y1 is the list of y-axis coordinates
            if x1 = [5, 7] and y1 = [12, 15] then the 1st point or start point will be (5, 12) and 
            end point will be (7, 15).
        """

        return self.add_trace(go.Scatter(
            x=x1, y=y1, line=dict(color=color), name=name
        ))
    
    def hide_legend(self):
        self.update_layout(showlegend=False)


fig = DashFinance()
app.layout = html.Div(children=[
    dcc.Graph(
        id="dash-figure-container",
        figure=fig,
        config={
            'scrollZoom': True,
            'displayModeBar': True,
            'modeBarButtonsToRemove': ['toggleSpikelines', 'zoomIn2d', 'zoomOut2d', 'autoScale2d']
        },
        style={
            'width': '1200px',
            'height': '700px'
        }
    )
])