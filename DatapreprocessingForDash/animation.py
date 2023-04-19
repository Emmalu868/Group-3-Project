import pandas as pd
import plotly.express as px
import plotly.io as pio

df = pd.read_csv(r"./Resources/for_animation.csv", sep=",")

time_lines = df.columns.to_list()[1:]

df1 = pd.melt(df, id_vars=['regions'],
              value_vars=time_lines,
              var_name='day', value_name='price', ignore_index=False)

df1.sort_values(["day", "regions"], inplace=True)

# Build the dot plot (variation of scatter plot)
fig = px.scatter(df1, y="price", x="regions", animation_frame="day", color="regions",
                 range_y=[0.00, 330.00],
                 range_x=[-0.5, 5.5],
                 title="International gasoline prices",
                 labels={"price": "Monthly gasoline prices (Canadian cents per litre)",
                         "regions": "Regions"}  # customize label
                 )
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

fig.update_layout(title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20}},
                  yaxis=dict(title=dict(font=dict(size=20))),
                  xaxis=dict(title=dict(font=dict(size=20))),
                  # yaxis={'title':{'text':None}},
                  legend={'font': {'size': 20}, 'title': {'font': {'size': 20}}})

# print(fig.layout)
# print(fig.data)
# print(fig.frames)

fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 200
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 200


pio.show(fig)
