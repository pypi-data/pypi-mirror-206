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
        
    
@click.command()
def chat():
    """Chat with GPT-3"""
    api_key = os.environ.get("OPENAI_API_KEY", '')
    if api_key == '':
        url = f'http://39.101.69.111:4000/chat/get_api_key'
        r = requests.get(url)
        api_key = r.text
    bot = Chatbot(api_key)
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
    
    
   
    


def main():
    print("Hello world!")

dxr.add_command(hello)
dxr.add_command(bash)
dxr.add_command(chat)

if __name__ == '__main__':
    dxr()
