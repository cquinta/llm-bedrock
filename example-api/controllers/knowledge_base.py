from .vector_store import Vector_Store
from .request_data import PromptBody
from .vector_index import Vector_Index
import time

class Knowledge_Base(object):
    def create(knowledge_base_name:str):
        vector_store_reply = Vector_Store.create(name=knowledge_base_name)
        time.sleep(60)
        #vector_index_reply = Vector_Index.create(store_name=vector_store_reply)
        return (
            [vector_store_reply,"teste"]
        )
