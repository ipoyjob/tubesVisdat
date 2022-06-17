# -*- coding: utf-8 -*-
# import modules
import numpy as np
import pandas as pd
from bokeh.io import output_file, save, curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import CDSView, ColumnDataSource, GroupFilter, Div, HoverTool
from bokeh.models.tools import RangeTool
from datetime import date
from bokeh.io import show
from bokeh.models import CustomJS, DateRangeSlider

# read data
country_list = ['Germany', 'France', 'Finland', 'Italy', 'Ireland', 'Russia']

df = pd.read_csv("./full_grouped.csv", parse_dates=['Date'])
data = df[df.Country.isin(country_list)] 
# data.head()

# output to file
# output_file('covid19.html',
#             title = 'Visualisasi Data Interaktif Statistik COVID-19')

# Create and configure the figure
con_fig = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=1000,
                  title='Click Legend to HIDE Data',
                  x_axis_label='Date', y_axis_label='Confirmed',
                 )

dea_fig = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=1000,
                  title='Click Legend to HIDE Data',
                  x_axis_label='Date', y_axis_label='Deaths')

rec_fig = figure(x_axis_type='datetime',
                  plot_height=400, plot_width=1000,
                  title='Click Legend to HIDE Data',
                  x_axis_label='Date', y_axis_label='Recovered')

# create a ColumnDataSource
covid_cds = ColumnDataSource(data)

# create views for 5 Country
ger_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Country', group='Germany')])

fra_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Country', group='France')])

fin_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Country', group='Finland')])

ita_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Country', group='Italy')])

ire_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Country', group='Ireland')])

rus_view = CDSView(source=covid_cds,
                  filters=[GroupFilter(column_name='Country', group='Russia')])

# format the tooltip
con_tooltips = [
            ('Country', '@Country'),
            ('Confirmed', '@Confirmed')
            ]

dea_tooltips = [
            ('Country', '@Country'),
            ('Death', '@Deaths')
            ]

rec_tooltips = [
            ('Country', '@Country'),
            ('Recovered', '@recovered')
            ]

# format hover glyph
con_hover_glyph = con_fig.circle(x='Date', y='Confirmed', source=covid_cds,
                                 size=7, alpha=0,
                                 hover_fill_color='white', hover_alpha=0.5)

dea_hover_glyph = dea_fig.circle(x='Date', y='Deaths', source=covid_cds,
                                 size=7, alpha=0,
                                 hover_fill_color='white', hover_alpha=0.5)

rec_hover_glyph = rec_fig.circle(x='Date', y='Recovered', source=covid_cds,
                                 size=7, alpha=0,
                                 hover_fill_color='white', hover_alpha=0.5)

# add the HoverTool to the figure
con_fig.add_tools(HoverTool(tooltips=con_tooltips, renderers=[con_hover_glyph]))
dea_fig.add_tools(HoverTool(tooltips=dea_tooltips, renderers=[dea_hover_glyph]))
rec_fig.add_tools(HoverTool(tooltips=rec_tooltips, renderers=[rec_hover_glyph]))

# consolidate the common keyword arguments in dicts
common_circle = {
    'source': covid_cds,
    'size': 5,
    'alpha': 1,
    'muted_alpha': 0
}
common_germany = {
    'view': ger_view,
    'color': '#FC6E51',
    'legend_label': 'Germany'
}
common_france = {
    'view': fra_view,
    'color': '#370665',
    'legend_label': 'France'
}
common_finland = {
    'view': fin_view,
    'color': '#35589A',
    'legend_label': 'Finland'
}
common_italy = {
    'view': ita_view,
    'color': '#F14A16',
    'legend_label': 'Italy'
}
common_ireland = {
    'view': ire_view,
    'color': '#FC9918',
    'legend_label': 'Ireland'
}
common_russia = {
    'view': rus_view,
    'color': '#32a842',
    'legend_label': 'Russia'
}

# create the figures and draw the data
con_fig.circle(x='Date', y='Confirmed', **common_circle, **common_germany)
con_fig.circle(x='Date', y='Confirmed', **common_circle, **common_france)
con_fig.circle(x='Date', y='Confirmed', **common_circle, **common_finland)
con_fig.circle(x='Date', y='Confirmed', **common_circle, **common_italy)
con_fig.circle(x='Date', y='Confirmed', **common_circle, **common_ireland)
con_fig.circle(x='Date', y='Confirmed', **common_circle, **common_russia)

dea_fig.circle(x='Date', y='Deaths', **common_circle, **common_germany)
dea_fig.circle(x='Date', y='Deaths', **common_circle, **common_france)
dea_fig.circle(x='Date', y='Deaths', **common_circle, **common_finland)
dea_fig.circle(x='Date', y='Deaths', **common_circle, **common_italy)
dea_fig.circle(x='Date', y='Deaths', **common_circle, **common_ireland)
dea_fig.circle(x='Date', y='Deaths', **common_circle, **common_russia)

rec_fig.circle(x='Date', y='Recovered', **common_circle, **common_germany)
rec_fig.circle(x='Date', y='Recovered', **common_circle, **common_france)
rec_fig.circle(x='Date', y='Recovered', **common_circle, **common_finland)
rec_fig.circle(x='Date', y='Recovered', **common_circle, **common_italy)
rec_fig.circle(x='Date', y='Recovered', **common_circle, **common_ireland)
rec_fig.circle(x='Date', y='Recovered', **common_circle, **common_russia)

# add interactivity to the legend
con_fig.legend.click_policy = 'mute'
dea_fig.legend.click_policy = 'mute'
rec_fig.legend.click_policy = 'mute'

# Date Range Slider
date_range_slider = DateRangeSlider(value=(date(2020, 1, 22), date(2020, 5, 13)),
                                    start=date(2020, 1, 22), end=date(2020, 5, 13))

#fungsi date_range_slider
date_range_slider.js_link("value", con_fig.x_range, "start", attr_selector=0)
date_range_slider.js_link("value", con_fig.x_range, "end", attr_selector=1)
date_range_slider.js_link("value", dea_fig.x_range, "start", attr_selector=0)
date_range_slider.js_link("value", dea_fig.x_range, "end", attr_selector=1)
date_range_slider.js_link("value", rec_fig.x_range, "start", attr_selector=0)
date_range_slider.js_link("value", rec_fig.x_range, "end", attr_selector=1)

# add a tittle for the entire visualization using Div
html = """<h3>Visualisasi Data Interaktif Statistik COVID-19</h3>
Kelompok: 9 <br>
Kelas: IF-42-GAB02 <br>"""
sup_title = Div(text=html)

# Create three panels
con_panel = Panel(child=con_fig, title='Confirmed')
dea_panel = Panel(child=dea_fig, title='Deaths')
rec_panel = Panel(child=rec_fig, title='Recovered')

# Assign the panels to Tabs
tabs = Tabs(tabs=[con_panel, dea_panel, rec_panel])

# Visualize
layout = row(sup_title, column(tabs, date_range_slider))
curdoc().add_root(layout)

# save to file
# show(layout)
