from itertools import cycle

import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from mdata.core import machine_data_def as mdd


def create_overview_plot(md: mdd.MachineData, downsample_to=10_000, use_gl=True):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.1)

    def create_hovertemplate(fs):
        return '<b>time: %{x:%X}</b>' \
            + '<br>' \
            + '<br>'.join([f'<i>{f}: %{{customdata[{i}]}}</i>' for i, f in enumerate(fs)]) + '<extra></extra>'

    def derive_colors(series, colorscale=plotly.colors.qualitative.Plotly):
        codes, _ = pd.factorize(series)
        codes = codes % len(colorscale)
        return np.take(colorscale, codes)

    did_downsample = False
    colorscale = plotly.colors.qualitative.Plotly
    objs = md.index_frame[mdd.MDConcepts.Object.as_str()].cat.categories
    color_dict = {o: c for o, c in zip(objs, cycle(colorscale))}
    for o in objs:
        # dummy traces for legend
        fig.add_trace(
            go.Scatter(x=[None], y=[None], marker=dict(color=color_dict[o]), mode='markers', name=o,
                       line={'color': 'rgba(0, 0, 0, 0)'}, legendgroup=o, showlegend=True, hoverinfo='none'))

    for tsc in md.iter_all_timeseries():
        timeseries_type = tsc.timeseries_type
        typ = timeseries_type.type
        row = 1 if typ == mdd.MachineDataType.E else 2
        fs = timeseries_type.features

        for g, gidx in tsc.df.groupby(mdd.MDConcepts.Object.as_str()).groups.items():
            obj = g
            df = tsc.df.loc[gidx]
            c = color_dict[g]

            length = len(df)
            if downsample_to and length > downsample_to:
                assert length > 0
                step = max(1, int(length / downsample_to))
                idx = np.arange(0, length, step)
                df = df.iloc[idx]
                did_downsample = True
            x, y = df[mdd.MDConcepts.Time.as_str()], df[mdd.MDConcepts.Label.as_str()]
            f_df = mdd.project_on_feature_columns(df)
            cls = go.Scattergl if use_gl else go.Scatter
            marker = dict(color=c)  # size=2
            n = f'{timeseries_type.type.as_str()}_{timeseries_type.label}_{obj}'
            g = cls(name=n, customdata=f_df, x=x, y=y, mode='markers',
                    hovertemplate=create_hovertemplate(fs), marker=marker, legendgroup=obj,
                    showlegend=False)
            fig.add_trace(g, row=row, col=1)

    fig.update_yaxes(categoryorder='category descending', side='left')
    fig.update_yaxes(title_text='Events', type='category', row=1, col=1)
    fig.update_yaxes(title_text='Measurements', type='category', row=2, col=1)
    # if not md.has_event_series():
    #    fig.update_yaxes()
    title_text = 'Overview'
    if did_downsample:
        title_text += '<br><sup>(sampled)</sup>'
    fig.update_layout(title=dict(text=title_text, xanchor='center', x=0.5, font_size=24),
                      legend=dict(title_text='Objects', x=0, y=1.2, orientation='h'))
    # fig.update_layout(title=dict(x=0), row=1, col=1)

    return fig
