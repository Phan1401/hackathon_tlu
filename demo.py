import json
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
api_key =  os.getenv('api_key')

with open('plan.json','r') as f:
    resource_changes = json.load(f)
    resource_changes = resource_changes['resource_changes']
    new_resource = resource_changes[1]['change']['after']
    old_resource = resource_changes[1]['change']['before']
    action = resource_changes[1]['change']['actions']


messages = [
    {'role':'system', 'content':f"""Bạn là một hệ thống giúp xác định nguyên nhân xảy ra sự sai lệch (drift) giữa resource cũ và resource mới.
                                    Cả hai resource đều có cấu trúc của một tệp JSON mà tôi sẽ cung cấp cho bạn.
                                    Loại sai lệch sẽ thuộc dạng {action}.
                                    Nhiệm vụ của bạn là tìm ra nguyên nhân, đề xuất một lý do có thể xảy ra, và gợi ý giải pháp.
                                    Vui lòng phản hồi bằng định dạng Markdown."""
    },
    {'role':'user', 'content':f""" Tôi sẽ cung cấp hai resource. Resource đầu tiên là resource cũ, và resource thứ hai là resource mới.

                                  Resource cũ: {old_resource}

                                  Resource mới: {new_resource}"""
    }
]

client = OpenAI(
  base_url= "https://openrouter.ai/api/v1",
  api_key= api_key,
)

completion = client.chat.completions.create(
  
  model="openai/gpt-4o-mini",
  messages=messages
)

print(completion.choices[0].message.content)