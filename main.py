import click
import datetime
from enum import Enum
import random
from typing import Optional

@click.group()
def cli():
    pass

@click.command()
def toy():
    class Toys(Enum):
        RED = "Red Ball"
        PURPLE = "Purple Angel"
    
    click.echo(print(f'Купите елочную игрушку: {random.choice(list(Toys)).value}'))
    

@click.command()
@click.option('--hours', is_flag=True) 
def newyear(hours): 
    date_n= datetime.datetime.now()
    date_ny=datetime.datetime(2022,1,1)
    delta=date_ny-date_n
    hours_1 = delta.total_seconds()// 3600
    if hours: 
        click.echo(print(f'До Нового года осталось {int(hours_1//24)} дней и {int(hours_1%24)} часов'))
    else:
        click.echo(print(f'До Нового года осталось {int(hours_1//24)} дней'))
        
 
cli.add_command(toy)
cli.add_command(newyear)
if __name__ == '__main__':
    cli()