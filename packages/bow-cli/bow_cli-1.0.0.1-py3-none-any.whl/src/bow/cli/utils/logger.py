import mcfc


def success(*objects):
    mcfc.echo("&a✔&r", *objects, "\n")

def info(*objects):
    mcfc.echo("&bℹ&r", *objects, "\n")

def error(*objects):
    mcfc.echo("&c✖&r", *objects, "\n")

def warn(*objects):
    mcfc.echo("&e⚠&r", *objects, "\n")