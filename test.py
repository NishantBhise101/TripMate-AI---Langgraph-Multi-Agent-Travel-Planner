from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# res = tavily_search("Best tourist attractions in India")
# print(res)

res = search_flights("Plan trip from Delhi")
print(res)
