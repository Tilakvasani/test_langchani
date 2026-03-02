[1mdiff --git a/messages.py b/messages.py[m
[1mindex 235072c..e767640 100644[m
[1m--- a/messages.py[m
[1m+++ b/messages.py[m
[36m@@ -9,7 +9,7 @@[m [mmessages=[[m
     SystemMessage(content='you are a helpful assistant'),[m
     HumanMessage(content='Tell me about Langchain')[m
 ][m
[31m-result=model.invoke(messages)[m
[32m+[m[32mresult=model.invoke(messages).content[m
 [m
 messages.append(AIMessage(content=result))[m
 [m
