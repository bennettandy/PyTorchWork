from IPython.display import display, HTML

def make_scrollable(output, height="100px"):
    return HTML(f'<div style="height:{height}; overflow:auto;">{output}</div>')

# # Example usage
# scrollable_output = scrollable(output, height="200px")
# display(scrollable_output)