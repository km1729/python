Plotly에서는 두가지 방법으로 plot을 생성 할 수 있다.   
# import plotly.graph_objects as go  
- low-level interface for creating highly customized visualization with full control over every aspect of the plot.  
- find-grained control over trace properties, layout, and annotations.  
- need to specify each trace and layout property explicitilym which can be more code-intensive  
- suitable for users who require precise customization and want to build complex, tailor-made visualizaton  

# import plotly.express as px 
- higer-level interface design for creating common types of visualization with LESS code.  
- Simplified syntax by using function like `px.scatter()`, `px.bar()` which automatically generate the necessary traces and layout.  
- great for simpler visualization
