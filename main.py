from graph import build_graph
from graph_state import Total
from logging_config import logger

player=input("Enter The Player :")

pipeline=build_graph()

result=pipeline.invoke({"Name":player})

# print(result["Name"])
# print(result["Summary"])
# print(result["ODI"])
# print(result["T20"])
# print(result["TEST"])

for i in result:
    print(result[i])


with open("graph2.png", "wb") as f:
    f.write(pipeline.get_graph().draw_mermaid_png())

import subprocess
subprocess.run(["start", "graph2.png"], shell=True)