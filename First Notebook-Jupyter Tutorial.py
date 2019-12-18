#!/usr/bin/env python
# coding: utf-8

# ##Simple Plotting, example
# This is a plot of the $sin$ function
# $$
# f(x)=\frac{\sin(x)}{x}
# $$

# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format= 'svg'")

import numpy as np
import matplotlib.pyplot as plt
pi=np.pi
x=np.linspace(-4*pi, 4*pi, 1000)
plt.rcParams['figure.figsize']=(11, 4)
plt.rcParams.update({'font.size': 17})
plt.xticks([-4*pi, -2*pi, 0, 2*pi, 4*pi],
                  ['$-4*pi$', '$-2*pi$', '$0$' , '$2*pi$, ''$4*pi$'] )
plt.yticks([0,1], ['$0$', '$1$'])
plt.title('$The Sin(x) Function$')
plt.axhline(0, color='black', lw=1)
plt.plot(x, np.sin(x)/x, label=r'$f(x)=\frac{\sin(x)}{x}$')
plt.legend(loc='best', fontsize=20)
plt.show()


# In[15]:


get_ipython().run_line_magic('lsmagic', '')


# In[16]:


get_ipython().run_line_magic('timeit', '3+1')


# In[17]:


def add2nums(a, b):
    return a+b


# In[18]:


get_ipython().run_line_magic('timeit', 'add2nums(3, 1)')


# In[25]:


get_ipython().run_cell_magic('timeit', '', '\na=[]\nfor i in range(1000):\n    a.append(4+i)')


# In[ ]:




