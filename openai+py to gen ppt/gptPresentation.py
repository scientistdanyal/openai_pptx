import openai, json
from pptx import Presentation
import apikey

openai.api_key = apikey.key   #apikey 


presentation_title = input('Write title of your presentation?? ')

query_json = """{
       "input_text" : "[[QUERY]]",
       "output_format":"json",
       "json_structure":{
       "slides":"{{presentation_slides}}"
       }
}"""

question = "Make 10 slide presention on " + presentation_title + " Each slide should have {{headar}}, {{content}}. Return as JSON."
prompt = query_json.replace("[[QUERY]]",question)
print(prompt)

completion = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages = [{'role':'user','content':prompt}])

response = completion.choices[0].message.content
