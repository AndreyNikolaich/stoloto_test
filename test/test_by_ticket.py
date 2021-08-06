
def test_by_ticket(app):
    app.by_ticket.go_to_wallet()
    app.by_ticket.fill_ticket_lottery_7x49()
    app.by_ticket.go_to_pay()

