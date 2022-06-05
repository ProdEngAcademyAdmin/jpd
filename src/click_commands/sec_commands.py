import click
from src.modules.security import Security


@click.group()
def sec():
    """Commands to secure the JFrog Platform"""


sec.add_command(Security.get_users)
sec.add_command(Security.get_user_lock_policy)
sec.add_command(Security.set_user_lock_policy)
sec.add_command(Security.get_password_expiration_policy)
sec.add_command(Security.set_password_expiration_policy)