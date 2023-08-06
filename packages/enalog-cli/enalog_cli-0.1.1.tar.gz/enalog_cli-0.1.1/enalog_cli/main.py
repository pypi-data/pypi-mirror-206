import json

from pathlib import Path
import typer
import requests


app = typer.Typer(pretty_exceptions_show_locals=False)

config = {}


class MissingRequiredData(Exception):
    """Thrown when required keys are missing from the data object"""

    pass


def get_config_file():
    app_dir = typer.get_app_dir("enalog")
    config_path: Path = Path(app_dir) / "config.json"

    if not config_path.is_file():
        with open("sample.json", "w") as config_file:
            config_json = json.dumps(config)
            config_file.write(config_json)

@app.callback()
def main():
    """
    EnaLog CLI
    """


@app.command()
def push(api_token: str = typer.Option(...), event: str = typer.Option(...)):
    """
    Push an event to EnaLog
    """
    event_dict = json.loads(event)

    required_keys = ("project", "name", "push")
    if not all(key in event_dict for key in required_keys):
        missing_keys = set(required_keys) - event_dict.keys()

        missing_keys_res = ""

        last_items = list(missing_keys)[-1]

        for miss in missing_keys:
            if miss == last_items:
                missing_keys_res += f"{miss}"
            else:
                missing_keys_res += f"{miss}, "

        raise MissingRequiredData(
            f"The {missing_keys_res} key(s) are missing from the event data"
        )
    try:
        res = requests.post(
            "https://api.enalog.app/v1/events",
            json=event_dict,
            headers={"Authorization": f"Bearer {api_token}"},
        )

        res.raise_for_status()

        if res.status_code == 200:
            typer.echo("Event successfully sent to EnaLog")
    except requests.exceptions.HTTPError as ex:
        error_message = typer.style(ex.response.text, fg=typer.colors.RED)
        typer.echo(error_message)
    except requests.exceptions.RequestException as ex:
        error_message = typer.style("Internal server error", fg=typer.colors.RED)
        typer.echo(error_message)
