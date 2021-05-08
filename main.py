import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
    })
st.write('動的な表')
st.dataframe(df.style.highlight_max(axis=0),
             width=200,height=200)
st.write('静的な表')
st.table(df.style.highlight_max(axis=0))

st.write('Markdown')
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit超入門')
```

"""

