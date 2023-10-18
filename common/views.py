import textwrap
from pathlib import Path

from django.shortcuts import redirect, render
from django.urls import reverse
import markdown
import yaml


def home(request):
    return render(request, 'common/home.html')


with Path(__file__).parent.joinpath('contents.yaml').open(encoding='utf8') as f:
    yaml_contents = yaml.safe_load(f)
    prompts = yaml_contents['prompts']
    guides = yaml_contents['guides']


def list_prompts(request):
    return render(request, 'common/list.html', {
        'title': '주제별 프롬프트 모음',
        'prompts': prompts.values()})


def view_prompt(request, prompt_id):
    prompt = prompts[prompt_id]
    content = markdown.markdown(textwrap.dedent(prompt['content']))
    return render(request, 'common/view_text.html', {
        'list_url': '/',
        'title': prompt['title'],
        'content': content,
    })


def list_guides(request):
    return render(request, 'common/list.html', {
        'title': '프롬프트 엔지니어링 가이드',
        'prompts': guides.values(),
        })


def view_guide(request, guide_id):
    guide = guides[guide_id]
    content = markdown.markdown(textwrap.dedent(guide['content']))
    return render(request, 'common/view_text.html', {
        'list_url': '/guide',
        'title': guide['title'],
        'content': content,
    })


