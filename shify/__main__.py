import click
from shify.utilities import run_algo


@click.group() 
def main(): 
    pass

@main.command()
@click.option('-s', '--script', help="The file that contains the algorithm to run.")
def run(script):
    print(f"loading script : {script}")

    with open(script, 'r') as f:
        script_code = f.read()

    script_globals = {}
    exec(script_code, script_globals)

    run_algo.run_algo(
        initialize  = script_globals['initialize' ],
        handle_data = script_globals['handle_data']
    )

if __name__ == '__main__':
    main()