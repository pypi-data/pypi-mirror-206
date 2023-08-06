from src.messaging.Mailer import MyMailer

config="../config.ini"
domain="example.fr"
mockup_response='[{"id": "blocklist_de", "name": "Blocklist.de", "detected": "True"}, {"id": "plonkatronix", "name": "Plonkatronix", "detected": "True"}, {"id": "s5h", "name": "S5h Blacklist", "detected": "True"}]'

mailer=MyMailer(config,domain,"provider-1")
mailer.send_alert_report(mockup_response)
mailer.send_regular_report()

def testType(number:int)->str:
    print(number)
    return number

testType("toto")