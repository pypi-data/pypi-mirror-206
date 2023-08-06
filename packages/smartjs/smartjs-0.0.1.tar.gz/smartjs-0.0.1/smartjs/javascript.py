__all__ = [
        'ScriptStatement', 'ScriptFunction', 'ScriptConstant',  'ScriptVariable', 'ScriptListLoop',
        'ScriptEventListener', 'Script', 'ScriptJoin', 'ScriptInterval', 'ScriptCondition',
        'ScriptElseCondition', 'ScriptIfCondition', 'ScriptElseIfCondition', 'ScriptTimeout', 'ScriptAnonymousFunction'
    ]

from collections import UserString
from typing import Union
from smartjs.functions import *


class BaseScript(UserString):
    pass


class ScriptStatement(BaseScript):
    def __init__(self, statement: str):
        self.statement = statement
        super().__init__(self.statement)


class ScriptJoin(BaseScript):
    def __init__(self, *args):
        self.args = args
        super().__init__(join(self.args, '; '))


class ScriptConstant(BaseScript):
    def __init__(self, name: str, statement: Union[str, ScriptStatement]):
        self.name = name
        self.statement = statement
        super().__init__(f'const {self.name} = {str(self.statement)}')
    
    @classmethod
    def create_by_id(cls, element_id: str):
        return cls(cls.make_name(element_id), f'document.getElementById("{element_id}")')
    
    @classmethod
    def make_name(cls, element_id: str):
        return camel_case(element_id)


class ScriptVariable(BaseScript):
    def __init__(self, name: str, statement: Union[str, ScriptStatement]):
        self.name = name
        self.statement = statement
        super().__init__(f'let {name} = {str(statement)}')


class ScriptIfCondition(BaseScript):
    def __init__(self, condition: str, statements: list[str]):
        self.condition = condition
        self.statements = statements
        super().__init__(f'if({self.condition}){{{join(self.statements, "; ")}}}')
        
        
class ScriptElseIfCondition(BaseScript):
    def __init__(self, condition: str, statements: list[str]):
        self.condition = condition
        self.statements = statements
        super().__init__(f'else if({self.condition}){{{join(self.statements, "; ")}}}')
        
        
class ScriptElseCondition(BaseScript):
    def __init__(self, statements: list[str]):
        self.statements = statements
        super().__init__(f'else {{{join(self.statements, "; ")}}}')
        
        
class ScriptCondition(BaseScript):
    def __init__(self, *args):
        self.args = args
        super().__init__(join(self.args))
        

class ScriptFunction(BaseScript):
    def __init__(self, name: str, arguments: str = '', statements: list[Union[str, ScriptStatement]] = None):
        self.name = name
        self.arguments = arguments
        self.statements = statements
        super().__init__(f'function {name} ({arguments}){{{join(self.statements, "; ")}}}')


class ScriptAnonymousFunction(BaseScript):
    def __init__(self, arguments: str = '', statements: list[Union[str, ScriptStatement]] = None):
        self.arguments = arguments
        self.statements = statements
        super().__init__(f'({arguments}) => {{{join(self.statements, "; ")}}}')


class ScriptListLoop(BaseScript):
    def __init__(self, list_name: str, statements: list[Union[str, ScriptStatement]]):
        self.list_name = list_name
        self.statements = statements
        super().__init__(f'for (let i = 0; i < {self.list_name}.length; i++) {{{ScriptJoin(self.statements)}}}')


class ScriptEventListener(BaseScript):
    def __init__(self, const_or_var: str, event_name: str, function: Union[str, ScriptFunction]):
        self.const_or_var = const_or_var
        self.event_name = event_name
        self.function = function
        super().__init__(f'{self.const_or_var}.addEventListener("{self.event_name}", {str(self.function)})')


class ScriptInterval(BaseScript):
    def __init__(self, call: str, interval: int = 1000):
        self.call = call
        self.interval = interval
        super().__init__(f'setInterval({self.call}, {self.interval})')


class ScriptTimeout(BaseScript):
    def __init__(self, call: str, interval: int = 1000):
        self.call = call
        self.interval = interval
        super().__init__(f'setTimeout({self.call}, {self.interval})')


class Script(BaseScript):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        super().__init__(f'<script {self.render_kwargs()}> {self.render_args()} </script>')
    
    def render_kwargs(self):
        return repr_dict(dict_filtered(self.kwargs), sep=" ")
    
    def render_args(self):
        return join(self.args, '; ')
    
    @staticmethod
    def name(value: str) -> str:
        return slug(value)
    
    @staticmethod
    def name_to_js_name(value: str) -> str:
        return join([item.title() for item in normalize(value).split()])
    
    @classmethod
    def create_input(cls, input_id, input_type, *args, label: str = None, **kwargs) -> ScriptJoin:
        return ScriptJoin(
                ScriptConstant(f'{cls.name(input_id)}Field', f'document.createElement("input")'),
                ScriptStatement(f'{cls.name(input_id)}Field.id = "{input_id}"'),
                ScriptStatement(f'{cls.name(input_id)}Field.type = "{input_type}"'),
                ScriptStatement(f'{cls.name(input_id)}Field.className = "{"form-check-input" if input_type == "checkbox" else "form-control"}"'),
                *[ScriptStatement(f'{cls.name(input_id)}Field.{item} = true') for item in list_filtered(args)],
                *[ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("{k}", "{v}")') for k, v in kwargs.items()],
                ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("placeholder", "{input_id}")'),
                ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("name", "{input_id}")'),
                ScriptConstant(f'{cls.name(input_id)}Label', f'document.createElement("label")')  if label and input_type != "hidden" else "",
                ScriptStatement(f'{cls.name(input_id)}Label.id = "{input_id}__label"') if label and input_type != "hidden" else "",
                ScriptStatement(f'{cls.name(input_id)}Label.setAttribute("for", "{input_id}")' if label and input_type != "hidden"  else ""),
                ScriptStatement(f'{cls.name(input_id)}Label.innerText = "{label}"'  if label and input_type != "hidden"  else ""),
                ScriptStatement(f'{cls.name(input_id)}Label.className = "{"form-check-label" if input_type == "checkbox" else "form-label"}"' if label and input_type != "hidden"  else ""),
                ScriptConstant(cls.name(input_id), f'document.createElement("div")'),
                ScriptStatement(f'{cls.name(input_id)}.id = "{input_id}__container"'),
                ScriptStatement(f'{cls.name(input_id)}.className = "form-floating"'),
                ScriptStatement(f'{cls.name(input_id)}.append({cls.name(input_id)}Field)'),
                ScriptStatement(f'{cls.name(input_id)}.append({cls.name(input_id)}Label' if label and input_type != "hidden"  else ""),
        )
    
    @classmethod
    def create_select(cls, input_id, *args, label: str = None, **kwargs) -> ScriptJoin:
        label = label or input_id
        return ScriptJoin(
                ScriptConstant(f'{cls.name(input_id)}Field', f'document.createElement("select")'),
                ScriptStatement(f'{cls.name(input_id)}Field.id = "{input_id}"'),
                ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("hx-trigger", "load")'),
                ScriptStatement(f'{cls.name(input_id)}Field.className = "form-select"'),
                *[ScriptStatement(f'{cls.name(input_id)}Field.{item} = true') for item in list_filtered(args)],
                *[ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("{k}", "{v}")') for k, v in kwargs.items()],
                ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("name", "{input_id}")'),
                ScriptConstant(f'{cls.name(input_id)}Label', f'document.createElement("label")'),
                ScriptStatement(f'{cls.name(input_id)}Label.id = "{input_id}__label"'),
                ScriptStatement(f'{cls.name(input_id)}Label.setAttribute("for", "{input_id}")'),
                ScriptStatement(f'{cls.name(input_id)}Label.innerText = "{label}"'),
                ScriptStatement(f'{cls.name(input_id)}Label.className = "form-label"'),
                ScriptConstant(cls.name(input_id), f'document.createElement("div")'),
                ScriptStatement(f'{cls.name(input_id)}.id = "{input_id}__container"'),
                ScriptStatement(f'{cls.name(input_id)}.className = "form-floating"'),
                ScriptStatement(f'{cls.name(input_id)}.append({cls.name(input_id)}Field, {cls.name(input_id)}Label)'),
        )
    
    @classmethod
    def create_textarea(cls, input_id, *args, label: str = None, height: str = "150px", **kwargs) -> ScriptJoin:
        label = label or input_id
        return ScriptJoin(
                ScriptConstant(f'{cls.name(input_id)}Field', f'document.createElement("textarea")'),
                ScriptStatement(f'{cls.name(input_id)}Field.id = "{input_id}"'),
                ScriptStatement(f'{cls.name(input_id)}Field.className = "form-control"'),
                ScriptStatement(f'{cls.name(input_id)}Field.style.height = "{height}"'),
                *[ScriptStatement(f'{cls.name(input_id)}Field.{item} = true') for item in list_filtered(args)],
                *[ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("{k}", "{v}")') for k, v in kwargs.items()],
                ScriptStatement(f'{cls.name(input_id)}Field.setAttribute("name", "{input_id}")'),
                ScriptConstant(f'{cls.name(input_id)}Label', f'document.createElement("label")'),
                ScriptStatement(f'{cls.name(input_id)}Label.id = "{input_id}__label"'),
                ScriptStatement(f'{cls.name(input_id)}Label.setAttribute("for", "{input_id}")'),
                ScriptStatement(f'{cls.name(input_id)}Label.innerText = "{label}"'),
                ScriptStatement(f'{cls.name(input_id)}Label.className = "form-label"'),
                ScriptConstant(cls.name(input_id), f'document.createElement("div")'),
                ScriptStatement(f'{cls.name(input_id)}.id = "{input_id}__container"'),
                ScriptStatement(f'{cls.name(input_id)}.className = "form-floating"'),
                ScriptStatement(f'{cls.name(input_id)}.append({cls.name(input_id)}Field, {cls.name(input_id)}Label)'),
        )
    

