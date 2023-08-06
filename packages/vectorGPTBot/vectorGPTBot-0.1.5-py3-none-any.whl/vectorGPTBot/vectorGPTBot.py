import chromadb
from transformers import AutoTokenizer, AutoModel
from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from chromadb.config import Settings


class mainClass():
    def __init__(self,file_pah,model_path="THUDM/chatglm-6b"):
        model_id = "damo/nlp_corom_sentence-embedding_chinese-base"
        self.pipeline_se = pipeline(Tasks.sentence_embedding,
                       model=model_id)
            
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            anonymized_telemetry=False,
            persist_directory=file_pah # Optional, defaults to .chromadb/ in the current directory
        ))
        self.db = self.client.get_or_create_collection('miandb') 
        pass

    def chatsss(self,text):
        response, history = self.model.chat(self.tokenizer,
                                    text,
                                    history=[],
                                    max_length= 2048,
                                    top_p= 0.999,
                                    temperature= 0.001)
        return response

    def vetor_db(self,db,input_text,ids):
        inputs = {
                "source_sentence": input_text
            }

        result = self.pipeline_se(input=inputs)
        self.db.add(
            embeddings=result['text_embedding'].tolist(),
            documents=input_text,
            ids=ids
        ) 

    def put_data(self,text_list):
        db = self.db
        input_text = [] 
        ids = []
        for ttt_i in range(len(text_list)):
            input_text.append(text_list[ttt_i])
            if self.db.count():
                ids.append(str(self.db.count()))
            else:
                ids.append(str('0'))
            if len(input_text) > 1000:
                self.vetor_db(db,input_text,ids)
                input_text = [] 
                ids = []
                #print(ttt_i)
        # 当输入包含“soure_sentence”与“sentences_to_compare”时，会输出source_sentence中首个句子与sentences_to_compare中每个句子的向量表示，以及source_sentence中首个句子与sentences_to_compare中每个句子的相似度。
        if len(ids) > 0:
            self.vetor_db(db,input_text,ids)

    def query_data(self,qa):
        src_qa =qa
        results = self.__query_data(qa)
        #print( results['distances'])
        contentext ='。\n'.join( results['documents'][0])+"。"
        qa = """请根据上下文来回答问题，如果根据上下文的内容无法回答问题，请回答"我不知道"。不需要编造信息。

    上下文：
    ```
    """+contentext+"""
    ```

    问题：```"""+qa+"""？```

    """
        #print(qa)
        result = self.chatsss(qa)
        #print('接入知识库后回答：',result)
        #print('==============')
        #print('接入知识库前回答：',chatsss(src_qa))
        return result

    def __query_data(self,text):
        db= self.db
        input_text = [ text ]
        inputs = {
                "source_sentence": input_text
            }
        result = self.pipeline_se(input=inputs)
        
        result = db.query(
            query_embeddings=result['text_embedding'].tolist()
            ,n_results=5
        )
        return result

    def run(self):
        print('hello')