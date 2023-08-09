import click


@click.group()
def main():
    click.echo(f"main...")
    pass

@main.command()
@click.option('-s', '--script', help="The file that contains the algorithm to run.")
def run(script):
    click.echo('run command call')
    print(f"script : {script}")

if __name__ == '__main__':
	main()