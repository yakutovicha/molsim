import ipywidgets as ipw

def get_start_widget(appbase, jupbase):
    #http://fontawesome.io/icons/
    template = """
    <table>
    <td valign="top"><ul>
    <li><a href="{appbase}/dc_group.ipynb" target="_blank"> Deliverable capacities (Quick and Simple) </a>
    <li><a href="{appbase}/dc_wf.ipynb" target="_blank"> Deliverable capacities (Elegant and Robust) </a>
    </ul></td>
    
"""
    
    html = template.format(appbase=appbase, jupbase=jupbase)
    return ipw.HTML(html)
    
#EOF
