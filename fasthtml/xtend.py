# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_xtend.ipynb.

# %% auto 0
__all__ = ['picocss', 'picolink', 'picocondcss', 'picocondlink', 'set_pico_cls', 'Html', 'A', 'AX', 'Checkbox', 'Card', 'Group',
           'Search', 'Grid', 'DialogX', 'Hidden']

# %% ../nbs/02_xtend.ipynb 2
from html.parser import HTMLParser
from dataclasses import dataclass, asdict

from fastcore.utils import *
from fastcore.xml import *
from fastcore.meta import use_kwargs, delegates
from .components import *

try: from IPython import display
except ImportError: display=None

# %% ../nbs/02_xtend.ipynb 3
picocss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css"
picolink = Link(rel="stylesheet", href=picocss)
picocondcss = "https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.conditional.min.css"
picocondlink = Link(rel="stylesheet", href=picocondcss)

# %% ../nbs/02_xtend.ipynb 6
def set_pico_cls():
    js = """var sel = '.cell-output, .output_area';
document.querySelectorAll(sel).forEach(e => e.classList.add('pico'));

new MutationObserver(ms => {
  ms.forEach(m => {
    m.addedNodes.forEach(n => {
      if (n.nodeType === 1) {
        var nc = n.classList;
        if (nc && (nc.contains('cell-output') || nc.contains('output_area'))) nc.add('pico');
        n.querySelectorAll(sel).forEach(e => e.classList.add('pico'));
      }
    });
  });
}).observe(document.body, { childList: true, subtree: true });"""
    return display.Javascript(js)

# %% ../nbs/02_xtend.ipynb 9
def Html(*c, doctype=True, **kwargs):
    res = xt('html', *c, **kwargs)
    if not doctype: return res
    return (xt('!DOCTYPE', html=True), res)

# %% ../nbs/02_xtend.ipynb 10
@delegates(xt_hx, keep=True)
def A(*c, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs):
    return xt_hx('a', *c, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../nbs/02_xtend.ipynb 12
@delegates(xt_hx, keep=True)
def AX(txt, hx_get=None, target_id=None, hx_swap=None, href='#', **kwargs):
    return xt_hx('a', txt, href=href, hx_get=hx_get, target_id=target_id, hx_swap=hx_swap, **kwargs)

# %% ../nbs/02_xtend.ipynb 14
@delegates(xt_hx, keep=True)
def Checkbox(checked:bool=False, label=None, value="1", **kwargs):
    if not checked: checked=None
    res = Input(type="checkbox", checked=checked, value=value, **kwargs)
    if label: res = Label(res, label)
    return res

# %% ../nbs/02_xtend.ipynb 16
@delegates(xt_hx, keep=True)
def Card(*c, header=None, footer=None, **kwargs):
    if header: c = (Header(header),) + c
    if footer: c += (Footer(footer),)
    return Article(*c, **kwargs)

# %% ../nbs/02_xtend.ipynb 18
@delegates(xt_hx, keep=True)
def Group(*c, **kwargs):
    return Fieldset(*c, role="group", **kwargs)

# %% ../nbs/02_xtend.ipynb 20
@delegates(xt_hx, keep=True)
def Search(*c, **kwargs):
    return Form(*c, role="search", **kwargs)

# %% ../nbs/02_xtend.ipynb 22
@delegates(xt_hx, keep=True)
def Grid(*c, cls='grid', **kwargs):
    c = tuple(o if isinstance(o,list) else Div(o) for o in c)
    return xt_hx('div', *c, cls=cls, **kwargs)

# %% ../nbs/02_xtend.ipynb 24
@delegates(xt_hx, keep=True)
def DialogX(*c, open=None, header=None, footer=None, id=None, **kwargs):
    card = Card(*c, header=header, footer=footer, **kwargs)
    return Dialog(card, open=open, id=id)

# %% ../nbs/02_xtend.ipynb 26
@delegates(xt_hx, keep=True)
def Hidden(value:str="", **kwargs):
    return Input(type="hidden", value=value, **kwargs)
