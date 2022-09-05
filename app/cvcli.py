import click

from app.cv import get_output_preset, get_output_variable
from app.pdfcreator import createpdf

VERSION = '1.0.0'
@click.group(chain=True, invoke_without_command=True)
@click.option('--debug', '-d', is_flag=True, show_default=True, default=False, help="Enables console log output.")
@click.option('--version', '-v', is_flag=True, show_default=True, default=False, help="Show current version.")
def cli(debug, version):
    """
    \b
    CV CLI
    This cli gives the option to give different information about me in different output formats.
    """
    if version:
        click.echo(VERSION)
    if debug:
        click.echo('Debug Log:')
    pass

@cli.command('file')
@click.option('--path', '-p', required=True, help="Set path to cv json file.")
@click.option('--output-format', '-o', show_default=True, default='pdf', help="Get output format: pdf, txt, md")
def file_output(path, output_format):
    """File
    Saving of CV/Resume in defined format.
    """
    print(f'Creating output with format: {output_format}')
    createpdf(path)

@cli.command('print-info-variable')
@click.option('--path', '-p', required=True, help="Set path to cv json file.")
def print_info_variable(path):
    """Print Info Variable
    Console output of variable parts of the CV/Resume.
    Required: Path to the json CV/Resume
    """
    click.echo('Printing information:')
    click.echo(get_output_variable(path))


@cli.command('print-info-preset-values')
@click.option('--path', '-p', required=True, help="Set path to cv json file.")
@click.option('--urls', '-u', is_flag=True, show_default=True, default=False, help="Get urls in output.")
@click.option('--projects', '-r', is_flag=True, show_default=True, default=False, help="Get projects in output.")
@click.option('--info', '-i', is_flag=True, show_default=True, default=False, help="Get short info in output")
@click.option('--skills', '-s', is_flag=True, show_default=True, default=False, help="Get skills in output")
@click.option('--contact', '-c', is_flag=True, show_default=True, default=False, help="Get contact in output")
@click.option('--education', '-e', is_flag=True, show_default=True, default=False, help="Get education in output.")
def print_info(path, urls, projects, info, skills, contact, education):
    """Print Info Preset Values
    Console output of defined parts of the CV/Resume.
    Required: Path to the json CV/Resume
    """
    flags = {
        'urls': urls,
        'projects': projects,
        'info': info,
        'skills': skills,
        'contact': contact,
        'education': education
    }
    click.echo('Printing information:')
    click.echo(get_output_preset(path, flags))
