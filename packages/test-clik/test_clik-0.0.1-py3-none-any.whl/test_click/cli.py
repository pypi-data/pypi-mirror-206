import click
from pathlib import Path


@click.command()
def init():
    # creacion archivo main.py
    file_path_main = Path('./') / 'main.py'
    file_path_main.touch()

    source_path = Path(__file__).parent / 'struct/main.py'

    with open(source_path, 'r') as source_file:
        content = source_file.read()

    with open(file_path_main, 'w') as file:
        file.write(content)

    # creacion de las vistas/archivos.py
    Path('views').mkdir(exist_ok=True)
    # file_path_view = file_path_main = Path('./views') / 'main.py'
    file_list = ['__init__.py', 'index.py', '404.py']

    for file_name in file_list:
        file = Path('views') / file_name
        file.touch()

        with open(source_path, 'r') as source_file:
            content = source_file.read()

        with open(file, 'w') as file:
            file.write(content)

    print('Se ha creado correctamente!')

    click.echo()
    click.echo(
        f"Generado {len(file_list)} files in the 'view' directory y  el archivo main.py:")
    for files in file_list:
        click.echo(f"● {files}")
    click.echo()


@click.group()
def flet_template():
    pass


flet_template.add_command(init)

if __name__ == "__main__":
    flet_template()
