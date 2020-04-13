import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    df = pd.read_csv('data/Pokemon.csv')
    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    type = pd.concat([df['Type 1'],df['Type 2'].dropna()]).sort_values()
    graph_one = []    
    graph_one.append(
      go.Histogram(
      x = type
      )
    )

    layout_one = dict(title = 'Number of Pokemons by Type 1',
                xaxis = dict(title = ''),
                yaxis = dict(title = '# of Pokemons'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []
    graph_two.append(
      go.Histogram(
      x = df['Generation'],
      )
    )

    layout_two = dict(title = 'Number of Pokemons by Generation',
                xaxis = dict(title = 'Generation',),
                yaxis = dict(title = '# of Pokemons'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x=df.groupby(['Type 1']).mean().reset_index().sort_values(by='Type 1')['Type 1'],
      y=df.groupby(['Type 1']).mean().reset_index().sort_values(by='Type 1')['HP'],
      )
    )

    layout_three = dict(title = 'Pokemon Average HP vs. Type',
                xaxis = dict(title = ''),
                yaxis = dict(title = 'HP')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = df['Attack'],
      y = df['Defense'],
      text = df['Name'],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Pokemon Defense vs. Attack HP',
                xaxis = dict(title = 'Attack'),
                yaxis = dict(title = 'Defense'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures