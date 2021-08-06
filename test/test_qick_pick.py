
def test_payment_page(app):
    app.session.logout()
    app.by_one_click.choice_ticket()



