from bokeh.plotting import figure, output_notebook, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Span, Range1d
from bokeh.embed import components
from bokeh.io import reset_output

title_font = '14pt'
axis_font = '10pt'
days_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

A_color = '#1f77b4'
B_color = 'limegreen'
C_color = 'orange'

def plot_output(p, filename):
    script, div = components(p)
    with open('bokeh_source/{}.html'.format(filename),'w') as f:
        f.write(script)
        f.write(div)

    output_file('images/{}.html'.format(filename))
    show(p)
    reset_output()

def score_distribution_plot(score_distribution,title):
    reset_output()
    n = score_distribution.sum()

    score_distribution = score_distribution.to_frame(name='freq')
    score_distribution['half'] = score_distribution['freq']/2
    score_distribution['percent'] = score_distribution['freq']/n

    dt = score_distribution[score_distribution.index < 13.5] # A 
    A_source = ColumnDataSource(dt.to_dict('list'))
    A_source.add(dt.index,name='score')

    dt = score_distribution[(score_distribution.index > 13.5) & (score_distribution.index < 27.5)] # B 
    B_source = ColumnDataSource(dt.to_dict('list'))
    B_source.add(dt.index,name='score')

    dt = score_distribution[score_distribution.index > 27.5] # C 
    C_source = ColumnDataSource(dt.to_dict('list'))
    C_source.add(dt.index,name='score')

    wh = 450
    p = figure(title=title,
              x_axis_label='score',
              y_axis_label='count',
              plot_width = wh,
              plot_height = wh,
              x_range = Range1d(-3,120),
              y_range = Range1d(0,3000))
    hover = HoverTool(tooltips=[('score','@score'),
                                ('count','@freq'),
                                ('percent','@percent{0.0%}')])
    p.add_tools(hover)

    def histo(p,source,color,grade):
        tally = sum(source.data['freq'])
        p.rect('score','half',
               width=1,
               height='freq',
               fill_color=color,
               line_color=color,
               hover_fill_color=color,
               hover_line_color='#333333',
               legend='{}: {:>3.0f}%'.format(grade, tally*100/n),
               source=source)

    histo(p, A_source, A_color,'A')
    histo(p, B_source, B_color,'B')
    histo(p, C_source, C_color,'C')

    p.title_text_font_size = title_font
    p.xaxis.axis_label_text_font_size = axis_font
    p.yaxis.axis_label_text_font_size = axis_font

    plot_output(p,title.replace(' ','_'))
