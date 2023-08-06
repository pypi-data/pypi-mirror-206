import click

import requests
from .ChatGPT import Chatbot
import os
import sys
from rich.live import Live
from rich.markdown import Markdown

sys.stdin.reconfigure(encoding='utf-8')

@click.command()
def hello():
    """Say hello"""
    click.echo('Hello, world!')

@click.group()
def dxr():
    """Figlu command line tool"""
    # 默认调用bash函数
    pass

def get_bash_scripts():
    url = 'http://39.101.69.111:4000/bash'
    r = requests.get(url)
    scripts = r.json()
    return scripts

def get_bash_script_dir(script):
    url = f'http://39.101.69.111:4000/bash/{script}'
    r = requests.get(url)
    scripts = r.json()
    return scripts

def get_bash_script(script, sub_script):
    url = f'http://39.101.69.111:4000/bash/{script}/{sub_script}'
    r = requests.get(url)
    script = r.text
    return script

def choose_script(scripts, step=1):
    script_index = 0
    while True:
        click.clear()
        click.echo('Select a script:')
        for i, script in enumerate(scripts):
            if i == script_index:
                click.echo(f'> {script}')
            else:
                click.echo(f'  {script}')
        key = click.getchar()
        # 上下键选择，左键返回，右键进入
        if key == '\r':
            return scripts[script_index], step + 1
        elif key == '\x1b[A':
            script_index = (script_index - 1) % len(scripts)
        elif key == '\x1b[B':
            script_index = (script_index + 1) % len(scripts)
        elif key == '\x1b[D':
            return None, step - 1
        elif key == '\x1b[C':
            return scripts[script_index], step + 1
            

@dxr.command()
def bash():
    """Bash scripts"""
    import os
    # scripts = get_bash_scripts()
    # script = choose_script(scripts)
    # sub_scripts = get_bash_script_dir(script)
    # sub_script = choose_script(sub_scripts)
    # bash_script = get_bash_script(script, sub_script)
    # print("=" * 80)
    # click.echo(bash_script)
    # print("=" * 80)
    # click.echo('Run this script?')
    # if click.confirm('Continue?'):
    #     os.system(bash_script)
    step = 1
    while True:
        if step == 0:
            break
        if step == 1:
            scripts = get_bash_scripts()
            script, step = choose_script(scripts, step)
        elif step == 2:
            sub_scripts = get_bash_script_dir(script)
            sub_script, step = choose_script(sub_scripts, step)
        elif step == 3:
            bash_script = get_bash_script(script, sub_script)
            print("=" * 80)
            click.echo(bash_script)
            print("=" * 80)
            click.echo('Run this script?')
            if click.confirm('Continue?'):
                os.system(bash_script)
                break
            step = 2
    
def get_api_key():
    api_key = os.environ.get("OPENAI_API_KEY", '')
    if api_key == '':
        url = f'http://39.101.69.111:4000/chat/get_api_key'
        r = requests.get(url)
        base_url_and_api_key = r.text
        base_url, api_key = base_url_and_api_key.split(',')
    return base_url, api_key  

@click.command()
@click.option("--model", default="gpt-3.5-turbo", help="Specify which GPT model to use")
@click.option("--maxtoken", default=4096, help="Maximum number of tokens in a single prompt")
def chat(model, maxtoken):
    """Chat with GPT-3 or GPT-4"""
    base_url, api_key = get_api_key()
    bot = Chatbot(api_key=api_key, base_url=base_url, engine=model, max_tokens=maxtoken)
    while True:
        text = input("You: ")
        if text.strip() == "exit":
            break
        response = bot.ask_stream(text)
        md = Markdown("")
        with Live(md, auto_refresh=False) as live:
            tmp = ""
            for r in response:
                tmp += r
                md = Markdown(tmp)
                live.update(md, refresh=True)
                

@click.command()
@click.option("--model", default="gpt-3.5-turbo", help="Specify which GPT model to use")
@click.option("--maxtoken", default=4096, help="Maximum number of tokens in a single prompt")
def git(model, maxtoken):
    """Git scripts"""
    print("这是一个git命令行助手,你可以通过这个助手来学习git命令")
    # use openai to generate git scripts
    base_url, api_key = get_api_key()
    bot = Chatbot(api_key=api_key, base_url=base_url, system_prompt="""
    你是一个很好的git命令行助手，你可以帮助我更好的使用git, 
    根据我的问题,你可以给我提供一些git命令
    """, engine=model, max_tokens=maxtoken)
    while True:
        text = input("请输入你的问题: ")
        if text.strip() == "exit":
            break
        response = bot.ask_stream(text)
        print("=" * 80)
        tmp = ""
        for r in response:
            tmp += r
            print(r, end='', flush=True)
        print()
        print("=" * 80)
    
    
   
    


def main():
    print("Hello world!")

dxr.add_command(hello)
dxr.add_command(bash)
dxr.add_command(chat)
dxr.add_command(git)

if __name__ == '__main__':
    dxr()
