#from main import df 
from bokeh.plotting import figure, show
import pandas
from bokeh.models import HoverTool, ColumnDataSource

df=pandas.read_csv("./times.csv", parse_dates=["Start", "End"])

df["Start_str"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_str"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

f=figure(x_axis_type="datetime", height=300, width=1000, title="Motion Graph")
f.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[("Start","@Start_str"), ("End","@End_str")])

f.add_tools(hover)
q=f.quad(left="Start", right="End", bottom=0, top=1, color="Red", source=cds)

show(f)