#Находим по регулярному выражению слова начинающиеся с буквы т или Т 
import re
text = 'Microsoft SQL Server is a proprietary relational Database management system developed by Microsoft'
match = re.findall(r'\b[dD]\w+',text)
print(match)