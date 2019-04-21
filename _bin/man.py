#!/usr/bin/env python
import click
import calendar
import os
from datetime import datetime, date
from jinja2 import Environment, FileSystemLoader, BaseLoader

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def date_format(date, fmt=None):
    fmt = fmt or "%m/%d"
    return date.strftime(fmt)

def get_template(template_name=None, template_string=None, base=None):
    env = None
    filters = {'date': date_format}

    if template_name:
        base = base or os.path.join(BASE, '_templates') 
        env = Environment(
            loader=FileSystemLoader(base, encoding='utf8'))
        env.filters = filters
        return env.get_template(template_name)

    if template_string:
        env = Environment(loader=BaseLoader)
        env.filters = filters
        return env.from_string(template_string)



def render(ctx, **vars):
    template = get_template(**ctx.obj)
    if template:
        click.echo(template.render(**vars))
        return 

    for key, val in vars.items():
        click.echo(f"{key}: {val}")


@click.group()
@click.option('--base', '-b', default=None)
@click.option('--template', '-t', default=None)
@click.pass_context
def diary(ctx, base, template):
    ctx.obj['base'] = base
    ctx.obj['template_name'] = template


def main():
    diary(obj={})


@diary.command()
@click.option('--year', '-y', default=None)
@click.option('--month', '-m', default=None)
@click.option('--reverse', '-r', is_flag=True)
@click.pass_context
def month_index(ctx, year, month, reverse):
    ctx.obj['template_name'] = ctx.obj['template_name'] \
        or 'month_index.md'
    today = datetime.now().date()
    y = int(year) if year else today.year
    m = int(month) if month else today.month
    dates = [
        date(y, m, d) 
        for d in calendar.Calendar().itermonthdays(y, m) 
        if d > 0
    ]
    if reverse:
        dates.reverse()
    render(ctx, dates=dates)


if __name__ == '__main__':
    main()
