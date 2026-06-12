from src.agent.graph import (
    research_graph,
)

png_data = (
    research_graph
    .get_graph()
    .draw_mermaid_png()
)

with open(
    "langgraph_m3.png",
    "wb",
) as f:

    f.write(
        png_data
    )

print(
    "Saved: langgraph_m3.png"
)