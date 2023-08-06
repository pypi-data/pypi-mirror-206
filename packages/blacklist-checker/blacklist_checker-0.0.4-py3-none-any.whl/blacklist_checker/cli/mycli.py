import typer
import sys
from requester.Black_list_checker import BlackListListChecker
from messaging.Mailer import MyMailer
app = typer.Typer()

@app.command()
def checkdns(domain:str = typer.Option("", help=("domain to test")),config:str=typer.Option("",help=("Configuration file")),reporting:bool=typer.Option(False,help=("If set a reporting is sent ")),provider:str=typer.Option("",help=("provider file"))):
    try:
        if config=="":
            config_file="config.ini"
        else:
            config_file=config
        mailer=MyMailer(config_file,domain,provider)
        checker= BlackListListChecker(config_file)
        result=checker.check(domain)
        if not result:
            if reporting:
                mailer.send_regular_report()
            print(f"Domain {domain} is not blacklisted")
        else:
            if reporting:
                print("reporting enabled for alert ")
                mailer.send_alert_report(result)
            print(f"Domain {domain} is  blacklisted")
            exit(2)
    except Exception as e:
        print(e)


@app.command()
def check_web_site(domain:str = typer.Option("", help=("domain to test"))):
    pass

def main():
    app()

if __name__ == "__main__":
    sys.exit(main())