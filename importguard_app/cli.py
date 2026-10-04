import typer
from rich.console import Console
from importguard_app.parser import extract_imports, extract_calls
from importguard_app.checker import check_module, check_method, check_chain

app = typer.Typer()
console = Console()


@app.callback()
def main():
    """importguard: catch AI-hallucinated imports and calls."""


@app.command()
def check(file_path: str):
    imports = extract_imports(file_path)
    calls = extract_calls(file_path)

    console.print("\n[bold underline]IMPORT CHECK[/bold underline]")
    for module in imports:
        status = check_module(module)
        if status == "missing":
            console.print(f"[red]✗ {module}: not found (possible fake package)[/red]")
        else:
            console.print(f"[green]✓ {module}: {status}[/green]")

    console.print("\n[bold underline]CALL CHECK[/bold underline]")
    for call in calls:
        module = call["module"]
        attrs = call["attrs"]
        line = call["line"]
        full_name = module + "." + ".".join(attrs)

        if check_module(module) in ("stdlib", "installed"):
            exists = check_chain(module, attrs)
            if exists is False:
                console.print(f"[red]✗ Line {line}: {full_name}() does not exist![/red]")
            else:
                console.print(f"[green]✓ Line {line}: {full_name}()[/green]")
        else:
            console.print(f"[yellow]? Line {line}: {module} not installed, cannot verify[/yellow]")


if __name__ == "__main__":
    app()