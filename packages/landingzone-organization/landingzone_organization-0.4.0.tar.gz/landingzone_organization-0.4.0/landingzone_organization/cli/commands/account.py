import click

from landingzone_organization.cli import Context


@click.group()
def cli():
    """Perform account operations"""
    pass


@cli.command()
@click.argument("account-id")
@click.pass_obj
def view(ctx: Context, account_id: str):
    """List all workloads"""
    account = ctx.organization.by_account_id(account_id)

    if account:
        click.echo(f"Account ID  : {account.account_id}")
        click.echo(f"Name        : {account.name}")
        click.echo(f"Environment : {account.environment}")
    else:
        click.echo(f"The {account_id} is not known to this organization.")
