from asyncio import coroutines
from typing import List, Optional
import langchain
from langchain.llms.base import LLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import pathlib
import os, json
import asyncio
from termcolor import colored
import torch, gc
from transformers import AutoTokenizer, AutoModel
import datetime
from hashlib import md5
import time
from .callbacks import AsyncWebsocketHandler, AsyncWebSocksetCallbackManager


from aiowebsocket.converses import AioWebSocket
from websocket import create_connection
import websockets
from websockets.server import serve
## LLM for chatglm
# only load from local's path
# default path is in ~/.cache/chatglm, if not exists, will download from huggingface'url :https://huggingface.co/THUDM/chatglm-6b
# 
"""Common utility functions for working with LLM APIs."""
import re
from typing import List
TODAY = datetime.datetime.now()
PASSWORD = "ADSFADSGADSHDAFHDSG@#%!@#T%DSAGADSHDFAGSY@#%@!#^%@#$Y^#$TYDGVDFSGDS!@$!@$" + f"{TODAY.year}-{TODAY.month}-{TODAY.day}"


def enforce_stop_tokens(text: str, stop: List[str]) -> str:
    """Cut off the text as soon as any stop words occur."""
    return re.split("|".join(stop), text)[0]

def auto_gc():
    if torch.cuda.is_available():
        # for all cuda device:
        for i in range(0,torch.cuda.device_count()):
            CUDA_DEVICE = f"cuda:{i}"
            with torch.cuda.device(CUDA_DEVICE):
                torch.cuda.empty_cache()
                torch.cuda.ipc_collect()
    else:
        gc.collect()

class ChatGLMLLM(LLM):
    """
            Load a model from local or remote
        if want to use stream mode:
            'streaming=True'
        if want to use langchain's Callback:
            examples: 'callbacks=[StreamingStdOutCallbackHandler(), AsyncWebsocketHandler()]'

        if want use cpu: # default will try to use gpu
            'cpu=True'
        
        if want to use remote's model:
            'remote_host="xx.xxx.xx.xx"'  , if set this , will auto call by ws://xx.xxx.xxx.xx:15000"
            optional:
                remote_callback: a callback function, will call when receive a new token like  'callback(new_token, history, response)'
                if not set, will print to stdout

    """
    max_token: int = 10000
    temperature: float = 0.01
    top_p = 0.9
    history = []
    history_id = "default"
    tokenizer: object = None
    model: object = None
    history_len: int = 10
    model: object = None
    tokenizer: object = None
    model_path: str = pathlib.Path.home() / ".cache" / "chatglm"
    cpu: bool = False
    streaming: bool = False
    verbose: bool = False
    callbacks  = [StreamingStdOutCallbackHandler(), AsyncWebsocketHandler()]
    callback_manager: langchain.callbacks.base.BaseCallbackManager = None
    remote_host: str = None


    @classmethod
    def load(cls, *args, model_path: str = None, **kargs):
        """
        Load a model from local or remote
        if want to use stream mode:
            'streaming=True'
        if want to use langchain's Callback:
            examples: 'callbacks=[StreamingStdOutCallbackHandler(), AsyncWebsocketHandler()]'

        if want use cpu: # default will try to use gpu
            'cpu=True'
        
        if want to use remote's model:
            'remote_host="xx.xxx.xx.xx"'  , if set this , will auto call by ws://xx.xxx.xxx.xx:15000"
            optional:
                remote_callback: a callback function, will call when receive a new token like  'callback(new_token, history, response)'
                if not set, will print to stdout


        """
        mo = cls(*args, **kargs)
        if "cpu" in kargs and kargs["cpu"]:
            mo.cpu = True
        if model_path is not None:
            mo.model_path = pathlib.Path(model_path)
        # load from local
        if mo.model_path.exists() and mo.remote_host is None:
            mo.model = AutoModel.from_pretrained(mo.model_path, trust_remote_code=True)
            mo.tokenizer = AutoTokenizer.from_pretrained(mo.model_path, trust_remote_code=True)
        else:
            # load from huggingface
            # use os.system to call git lfs download model
            # then load from local
            # TODO: use git lfs to download model
            pass
        if mo.remote_host is not None:
            return mo
        if mo.cpu:
            mo.model = mo.model.float()
        else:
            mo.model = mo.model.half().cuda()
        mo.model = mo.model.eval()
        return mo
    
    def set_history(self, hist:List[str]):
        self.history = hist
    
    
    @property
    def _llm_type(self) -> str:
        return "ChatGLM"

    async def _acall(self, prompt: str, stop: List[str] = None):
        if self.streaming:
            # print("async ing ", self.callbacks)
            if not "(history_id:" in prompt:
                prompt = f"(history_id:{self.history_id})" + prompt

            if not isinstance(self.callback_manager, AsyncWebSocksetCallbackManager):
                self.callback_manager = AsyncWebSocksetCallbackManager([i for i in self.callbacks if isinstance(i, AsyncWebsocketHandler)])
            current_completion = ""
            # if self.callback_manager.is_async:
            prompt,history_id, history = await self.callback_manager.on_llm_start(
                prompt,
                None,
                verbose=self.verbose
            )
            if history_id is not None and history is not None:
                self.history_id = history_id
                self.history = history
            for response, history in self.model.stream_chat(self.tokenizer, prompt, self.history, max_length=self.max_token, top_p=self.top_p,
                                               temperature=self.temperature):
                
                delta = response[len(current_completion) :]
                current_completion = response
                data = {"response": response, "history": history,"query": prompt, "verbose":self.verbose}
                if self.callback_manager.is_async:
                    # print(".", end="", flush=True)
                    await self.callback_manager.on_llm_new_token(
                        delta, verbose=self.verbose, **data
                    )
                else:
                    # print("+", end="", flush=True)
                    self.callback_manager.on_llm_new_token(
                        delta, verbose=self.verbose, **data
                    )
            auto_gc()
            self.history = self.history+[[None, current_completion]]
            await self.callback_manager.on_llm_end(
                {
                    "id": self.history_id,
                    "history": self.history,
                },
                verbose=self.verbose
            )
            return current_completion
        elif self.remote_host is not None :
            uri = f"ws://{self.remote_host}:15000"
            result = ''
            # self.callback_manager =  langchain.callbacks.base.BaseCallbackManager(self.callbacks)
            self.callback_manager.set_handlers(self.callbacks)
            async with AioWebSocket(uri) as aws:
                converse = aws.manipulator
                
                user_id = md5(time.asctime().encode()).hexdigest()
                await converse.send(json.dumps({"user_id":user_id, "password":PASSWORD}).encode())
                res = await converse.receive()
                res = res.decode()
                if res != "ok":
                    raise Exception("password error:"+res)
                
                await converse.send(json.dumps({"prompt":prompt, "history":self.history}).encode())
                self.callback_manager.on_llm_start(prompt, None, verbose=self.verbose)
                while 1:
                    res = await converse.receive()
                    msg = json.loads(res.decode())
                    # { "new":delta,"response": response, "history": history,"query": prompt}
                    if "stop" in msg:
                        break
                    new_token = msg["new"]
                    response = msg["response"]
                    history = msg["history"]
                    self.callback_manager.on_llm_new_token(new_token, response=response, history=history, query=prompt, verbose=self.verbose)
                    result = response
            self.history = self.history+[[None, result]]
            self.callback_manager.on_llm_end(result, verbose=self.verbose)
            return result


                
        else:
            response, _ = self.model.chat(
                self.tokenizer,
                prompt,
                history=self.history[-self.history_len:] if self.history_len > 0 else None,
                max_length=self.max_token,
                top_p=self.top_p,
                temperature=self.temperature,
            )
            response = enforce_stop_tokens(response, stop or [])
            self.history = self.history+[[prompt, response]]
            return response

    
    def _call(self, prompt: str, stop: List[str]  = None) -> str:
        if self.streaming:
            current_completion = ""
            if self.verbose:
                print("streaming")
            
            for response, history in self.model.stream_chat(self.tokenizer, prompt, self.history, max_length=self.max_token, top_p=self.top_p,
                                               temperature=self.temperature):
                delta = response[len(current_completion) :]
                current_completion = response
                data = {"response": response, "history": history,"query": prompt}
                if self.verbose:
                    print(delta, end='', flush=True)
                self.callback_manager.on_llm_new_token(
                    delta, verbose=self.verbose, **data
                )
            auto_gc()
            self.history = self.history+[[None, current_completion]]
            return current_completion
        elif self.remote_host is not None :
            ws = create_connection(f"ws://{self.remote_host}:15000")
            # self.callback_manager =  langchain.callbacks.base.BaseCallbackManager(self.callbacks)
            self.callback_manager.set_handlers(self.callbacks)
            user_id = md5(time.asctime().encode()).hexdigest()
            ws.send(json.dumps({"user_id":user_id, "password":PASSWORD}).encode())
            res = ws.recv()
            if res != "ok":
                raise Exception("password error")
            result = ''
            ws.send(json.dumps({"prompt":prompt, "history":self.history}))
            self.callback_manager.on_llm_start(
                prompt,
                None,
                verbose=self.verbose
            )
            while 1:
                res = ws.recv()
                msg = json.loads(res)
                # { "new":delta,"response": response, "history": history,"query": prompt}
                if "stop" in msg:
                    break
                new_token = msg["new"]
                response = msg["response"]
                history = msg["history"]
                msg["verbose"] = self.verbose
                # self.remote_callback(new_token, history, response)
                
                self.callback_manager.on_llm_new_token(new_token, **msg)
                result = response
            self.callback_manager.on_llm_end(result, verbose=self.verbose)
            self.history = self.history+[[None, result]]
            return result
        else:
            response, _ = self.model.chat(
                self.tokenizer,
                prompt,
                history=self.history[-self.history_len:] if self.history_len>0 else [],
                max_length=self.max_token,
                temperature=self.temperature,
            )
            auto_gc()
            if stop is not None:
                response = enforce_stop_tokens(response, stop)
            self.history = self.history+[[None, response]]
            return response



class WebsocketWrap:
    def __init__(self, llm, websocket):
        self.websocket = websocket
        self.llm = llm
    
    async def __call__(self, prompt=None, history=None):
        assert prompt is not None 
        assert isinstance(prompt, str)
        llm = self.llm
        current_completion = ""
        if history is not None and isinstance(history, list):
            llm.history = history
        for response, history in llm.model.stream_chat(llm.tokenizer, prompt, llm.history, max_length=llm.max_token, top_p=llm.top_p,
                                               temperature=llm.temperature):
            delta = response[len(current_completion) :]
            current_completion = response
            data = { "new":delta,"response": response, "history": history,"query": prompt}
            await self.websocket.send(json.dumps(data))
        data = { "new":delta,"response": response, "history": history,"query": prompt, "stop":True}
        await self.websocket.send(json.dumps(data))




class AsyncServer:
    __users = {}
    _callbacks = {"hello": lambda x: colored("[hello]","green") + time.asctime()}
    llm = None
    @classmethod
    async def echo(cls,websocket):
        try:
            print(colored("[connected]","green"),":",websocket)
            no = 0
            async for message in websocket:
                if no == 0:
                    if await cls.user(message, websocket):
                        no += 1
                        continue
                    else:
                        await websocket.close()
                        break
                print(colored("[recv]","green") ,":",message)
                if len(message) == 0:
                    await cls.del_user(websocket)
                    break
                    
                oneChat = WebsocketWrap(cls.llm, websocket)
                
                await oneChat(**json.loads(message))

                no += 1
        except websockets.exceptions.ConnectionClosedOK:
            print(colored("[closed]","yellow"),":",websocket)
            await cls.del_user(websocket)
        except websockets.exceptions.ConnectionClosedError:
            print(colored("[closed]","red"),":",websocket)
            await cls.del_user(websocket)

        except Exception as e:
            
            print(colored("[error]","red"),":",e)
            raise e
    
    @classmethod
    def add_callback(cls, name, callback):
        cls._callbacks[name] = callback

    @classmethod
    async def call(cls, message, websocket):
        try:
            msgs = json.loads(message)
            if "user_id" not in msgs :
                await websocket.send("error")
                await websocket.close()
                await cls.del_user(websocket)
                return
            user_id = msgs["user_id"]
            if user_id not in cls.__users.values():
                await websocket.send("not login")
                await websocket.close()
                await cls.del_user(websocket)
                return
            if "callback" in msgs:
                callback = cls._callbacks[msgs["callback"]]
                args = msgs.get("args",[])
                kwargs = msgs.get("kwargs",{})

                res = await callback(*args, **kwargs)
                await websocket.send(json.dumps({
                    "result":res,
                    "user_id":user_id,
                    "callback":msgs["callback"],
                }))
            
        except Exception as e:
            print(colored("[error]","red"),":",e)
            await websocket.close()
            await cls.del_user(websocket)

    @classmethod
    async def main(cls, port):
        async with serve(cls.echo, "0.0.0.0", port):
            await asyncio.Future()  # run forever
    
    @classmethod
    async def user(cls, first_msg, websocket) -> bool:
        try:
            d = json.loads(first_msg)
            user_id = d["user_id"]
            password = d["password"]
            if password != PASSWORD:
                return False
            print(colored("[user-login]","green"),":",user_id)
            cls.__users[websocket] =  user_id
            await websocket.send("ok")
            return True
        except Exception as e:
            print(colored("[error]","red"),":",websocket, e)
    
    @classmethod
    async def del_user(cls,websocket):
        if websocket in cls.__users:
            del cls.__users[websocket]

    @classmethod
    def start(cls,port=15000, model_path=None):
        cpu = False
        if not torch.cuda.is_available():
            cpu = True
        print(colored(f"[cpu:{cpu} ]","green"),":",f"listen:0.0.0.0:{port}")
        cls.llm = ChatGLMLLM.load(model_path=model_path, cpu=cpu, streaming=True)
        print(colored(f"[ starting ]","green"),":",f"listen:0.0.0.0:{port}")
        asyncio.run(cls.main(port))